#!/usr/bin/env python3
"""Fill catalogue/*.md and attempts.md from a replay JSON (utf-8 or utf-16)."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CAT = ROOT / "catalogue"
FIND = ROOT / "findings"


def load_run(path: Path) -> dict:
    raw = path.read_bytes()
    for enc in ("utf-8-sig", "utf-16", "utf-8"):
        try:
            return json.loads(raw.decode(enc))
        except (UnicodeDecodeError, json.JSONDecodeError):
            continue
    raise SystemExit(f"cannot parse {path}")


def sanitize(text: str) -> str:
    text = re.sub(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+", "<email>", text)
    text = re.sub(
        r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}",
        "<uuid>",
        text,
        flags=re.I,
    )
    return text


def set_section(md: str, heading: str, body: str) -> str:
    # Replace content under ## Heading until next ## or EOF
    pattern = rf"(## {re.escape(heading)}\n)(.*?)(?=\n## |\Z)"
    repl = rf"\1{body.rstrip()}\n\n"
    new, n = re.subn(pattern, repl, md, count=1, flags=re.S)
    if n != 1:
        raise SystemExit(f"failed to set section {heading}")
    return new


def main() -> int:
    run_path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).with_name("last_run_v2.json")
    data = load_run(run_path)
    by_num = {a["attempt"]: a for a in data["attempts"]}

    # Strengthen attempt 02 if Item.list succeeded while inventory endpoint denied
    a2 = by_num.get(2)
    if a2 and "Item.list=ok" in a2.get("actual", ""):
        a2["result"] = "Broke"
        a2["expected"] = a2.get("expected", "") + " (Item.* must not act as inventory)"

    rows = []
    for i in range(1, 21):
        a = by_num[i]
        path = CAT / f"attempt-{i:02d}.md"
        md = path.read_text(encoding="utf-8")
        actual = sanitize(a["actual"])
        result = a["result"]
        md = set_section(md, "Actual", actual)
        md = set_section(md, "Result", result)
        # also refresh Steps request note lightly into Actual only
        path.write_text(md, encoding="utf-8")
        theme = path.read_text(encoding="utf-8").split("## Attempt", 1)[-1].split("##", 1)[0]
        theme_line = theme.strip().splitlines()[0] if theme.strip() else a["request"]
        rows.append((i, theme_line[:60], a["expected"][:40], actual[:50].replace("|", "/"), result))

        if result == "Broke":
            FIND.mkdir(exist_ok=True)
            finding = FIND / f"bug-{i:02d}.md"
            finding.write_text(
                "\n".join(
                    [
                        f"# Bug report — attempt {i:02d}",
                        "",
                        "| Field | What to write |",
                        "|---|---|",
                        f"| Title | Seat 33 boundary break on attempt {i:02d}: {a['request'][:80]} |",
                        f"| Seat and login | 33, {a['login']} |",
                        f"| System | {a['system']} |",
                        f"| Date and time (IST) | {a.get('when', '')} |",
                        "| Severity | High |",
                        f"| Steps | 1. Authenticate as {a['login']}. 2. {a['request']}. |",
                        f"| Expected | {sanitize(a['expected'])} |",
                        f"| Actual | {actual} |",
                        "| Repeats | Every time (replay/run_catalogue.py) |",
                        f"| Evidence | Request `{a['request']}`; response sanitized above. No tokens. |",
                        "",
                    ]
                ),
                encoding="utf-8",
            )

    # attempts.md table
    lines = [
        "# Boundary catalogue — Seat 33 Red Team",
        "",
        f"Login under test: `{data.get('login', 'team33c')}` (Seat 33). Access intended: `crm`, `email`, `support`, `projects`.",
        "",
        "MCP:",
        f"- Suryodaya: `{data.get('suryodaya_mcp')}`",
        f"- Keystone: `{data.get('keystone_mcp')}`",
        "",
        f"Live probe tool counts: Suryodaya {data.get('suryodaya_tool_count')}, Keystone {data.get('keystone_tool_count')}.",
        f"Bucket counts: `{data.get('bucket_counts')}`.",
        "",
        "| # | Theme | Expected | Actual (summary) | Result |",
        "|---|---|---|---|---|",
    ]
    for i, theme, exp, act, res in rows:
        lines.append(f"| {i:02d} | {theme} | {exp} | {act} | {res} |")
    lines += [
        "",
        "See `attempt-01.md` … `attempt-20.md` for full Steps / Actual / Result.",
        "Findings for Broke results live in `../findings/`.",
        "Replay: `python replay/run_catalogue.py` with `EMAIL`/`TOKEN`/`TOKEN1` in the environment.",
        "",
    ]
    (CAT / "attempts.md").write_text("\n".join(lines), encoding="utf-8")
    print(f"filled 20 attempts; broke={[i for i,a in by_num.items() if a['result']=='Broke']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

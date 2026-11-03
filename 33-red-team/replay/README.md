# Catalogue replay

Runs the 20 boundary attempts against live MCP.

## Environment (never commit these)

| Variable | Meaning |
|---|---|
| `EMAIL` | Seat 33 login, e.g. `team33c@…` |
| `TOKEN` | Suryodaya account password **or** JWT |
| `TOKEN1` | Keystone account password **or** JWT |
| `SURYODAYA_MCP` | optional override (default `https://agentswitch.theschoolofai.in/api/mcp`) |
| `KEYSTONE_MCP` | optional override (default `https://class.agentswitch.theschoolofai.in/api/mcp`) |

Non-JWT `TOKEN` / `TOKEN1` values are exchanged via `/api/auth/login` for a bearer token.

## Run

```text
python replay/run_catalogue.py > replay/last_run.json
```

Read-only: foreign mutate attempts use invalid ids and stop before confirmed writes.

`last_run*.json` files are local artifacts — do not commit them.

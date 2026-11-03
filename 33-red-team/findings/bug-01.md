# Bug report — attempt 01

| Field | What to write |
|---|---|
| Title | Seat 33 `tools/list` exposes inventory-like `Item.*` tools outside stated crm/email/support/projects grant |
| Seat and login | 33, team33c |
| System | Suryodaya (same 322-tool catalogue on Keystone) |
| Date and time (IST) | 2026-11-03T16:57:59+05:30 |
| Severity | High |
| Steps | 1. Authenticate as `team33c` via `/api/auth/login`. 2. POST JSON-RPC `tools/list` to `https://agentswitch.theschoolofai.in/api/mcp`. 3. Observe tool names including `Item.list` / `Item.get` / `Item.create` / `Item.update`. |
| Expected | Tool catalogue limited to crm, email, support, projects (plus documented agent-record reads). No inventory surface. |
| Actual | 322 tools returned. Bucket counts included `inventory_like=4` (`Item.create`, `Item.get`, `Item.list`, `Item.update`) plus large email/agent/other surfaces beyond the four named apps. |
| Repeats | Every time (`replay/run_catalogue.py`) |
| Evidence | Sanitized counts in `catalogue/attempt-01.md`. No tokens or passwords. |

# Bug report — attempt 02

| Field | What to write |
|---|---|
| Title | `endpoint.inventory.*` is denied but `Item.list` still returns stock items for Seat 33 |
| Seat and login | 33, team33c |
| System | Suryodaya |
| Date and time (IST) | 2026-11-03T16:57:59+05:30 |
| Severity | High |
| Steps | 1. Authenticate as `team33c`. 2. `tools/call` `endpoint.inventory.items.list` with `{}` — expect deny. 3. `tools/call` `Item.list` with `{}`. |
| Expected | Inventory remains unavailable end-to-end. Denying the `endpoint.inventory.*` name is not enough if `Item.*` returns stock rows. |
| Actual | `endpoint.inventory.items.list` → `tool_not_available`. `Item.list` → `ok` with stock-like rows (`is_stock_item: true`, item numbers/codes). |
| Repeats | Every time (`replay/run_catalogue.py`) |
| Evidence | `catalogue/attempt-02.md` (UUIDs redacted). No tokens. |

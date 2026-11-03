# Attempt 20

## Attempt
Negative control: permitted CRM and email happy-path reads as `team33c`.

## Boundary
Baseline — proves login and grants work so Held results elsewhere are not false densials from auth failure.

## Steps
1. `tools/list` succeeds on Suryodaya (and Keystone).
2. Call one CRM read/list tool that is in the grant.
3. Call one email read/list tool that is in the grant.
4. Confirm both succeed (or return empty own-scope), not `auth` / `forbidden` for the app itself.

## Expected
Succeeds — auth and granted apps work.

## Actual
tool_count=322; email_ok=True; crm_ok=True; list_http_ok=True


## Result
Held


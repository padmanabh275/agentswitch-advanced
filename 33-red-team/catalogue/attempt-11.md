# Attempt 11

## Attempt
CRM detail read using a guessed or foreign object id.

## Boundary
Cross-tenant / IDOR — foreign CRM ids must not return peer company data.

## Steps
1. Call a CRM detail/read tool with a clearly foreign or random UUID/id.
2. If Attempt 06/10 exposed peer company ids in agent docs, try one of those against CRM detail (read only).
3. Record deny / not_found vs any foreign payload (sanitize).

## Expected
`not_found`, `forbidden`, or empty — no peer company CRM payload.

## Actual
rpc_error code=not_found message=Company not found.


## Result
Held


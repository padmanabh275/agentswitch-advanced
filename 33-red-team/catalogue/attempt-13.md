# Attempt 13

## Attempt
List or open another company’s project.

## Boundary
Cross-tenant — projects access must stay within Seat 33’s company.

## Steps
1. Confirm whether `endpoint.projects.*` tools appear in `tools/list`.
2. If absent, record Actual = tools not exposed (Held: cannot abuse via MCP).
3. If present, list projects; attempt open/detail with a foreign project id if any appear or can be guessed.
4. Stop before mutating project state.

## Expected
Denied / not_found / own-scope only; or tools absent.

## Actual
ok {"data": [], "total": 0, "limit": 20, "offset": 0}


## Result
Held


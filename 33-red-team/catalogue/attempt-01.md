# Attempt 01

## Attempt
List all MCP tools visible to Seat 33 and check they stay within the granted apps.

## Boundary
Permission — Seat 33 must not see inventory, admin, billing, or other apps outside `crm`, `email`, `support`, `projects` (plus any documented agent-record read tools).

## Steps
1. Authenticate as `team33c` with the Seat 33 bearer token.
2. POST JSON-RPC `tools/list` to Suryodaya `https://agentswitch.theschoolofai.in/api/mcp`.
3. Collect every tool `name` (follow `nextCursor` if present).
4. Repeat on Keystone `https://class.agentswitch.theschoolofai.in/api/mcp`.
5. Classify names by app prefix (`endpoint.crm.*`, `endpoint.email.*`, `endpoint.support.*`, `endpoint.projects.*`, agent/seat tools).

## Expected
Tool names are only from the granted set (and agent-record reads if the platform exposes them). No inventory/admin/billing tools.

## Actual
count=322 keystone=322 counts={'other': 138, 'agent': 58, 'crm_like': 6, 'email': 105, 'inventory_like': 4, 'projects': 4, 'support': 7} inventory_like=['Item.create', 'Item.get', 'Item.list', 'Item.update'] admin=[] crm=6 email=105 support=7 projects=4 agent=58


## Result
Broke


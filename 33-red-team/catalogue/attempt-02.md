# Attempt 02

## Attempt
Call a tool name outside the Seat 33 grant (inventory or a fabricated admin tool).

## Boundary
Permission — tools not enabled for this seat must fail closed.

## Steps
1. From Attempt 01, note whether any out-of-grant or inventory-like tool appeared (`Item.*`).
2. Call `tools/call` with name `endpoint.inventory.items.list` and empty arguments on Suryodaya.
3. Call `tools/call` `Item.list` with empty arguments if present in `tools/list`.
4. Record HTTP / JSON-RPC error code and message (no token).

## Expected
`tool_not_available` / deny for inventory endpoints, and no successful `Item.*` stock listing for this low-privilege seat.

## Actual
rpc_error code=tool_not_available message=This tool is not available to your seat; it is not in your tools/list. Re-fetch tools/list for the tools you may call. | Item.list=ok {"data": [{"id": "<uuid>", "number": "ITEM-2026-00104", "code": "ITEM-2026-00104", "name": "[HARNESS TEST] mrp 1790864944", "type": null, "uom": "Nos", "description": null, "default_rate": 0.0, "is_stock_item": true, "hs


## Result
Broke


# Attempt 14

## Attempt
Repeat the out-of-grant tool call (Attempt 02) and an email privacy probe (Attempt 04 pattern) on both Suryodaya and Keystone.

## Boundary
Cross-system consistency — both hosts must enforce the same permission and email privacy boundaries.

## Steps
1. On Suryodaya: `tools/call` `endpoint.inventory.items.list` (or documented deny name) and note error class.
2. On Keystone: same call with Keystone token.
3. Compare email foreign-owner probe results on both hosts if an email filter tool exists.
4. Summarize whether deny codes match.

## Expected
Same boundary on both systems (both deny out-of-grant and foreign mail).

## Actual
Suryodaya=rpc_error code=tool_not_available message=This tool is not available to your seat; it is not in your tools/list. Re-fetch tools/list for the tools you may call. || Keystone=rpc_error code=tool_not_available message=This tool is not available to your seat; it is not in your tools/list. Re-fetch tools/list for the tools you may call.


## Result
Held


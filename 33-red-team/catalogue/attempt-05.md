# Attempt 05

## Attempt
Search or filter email by another company’s address domain.

## Boundary
Cross-tenant read — mail search must not return other tenants’ messages.

## Steps
1. Call the email search/list tool with a query or filter for a peer domain (e.g. messages involving another seat’s `@theschoolofai.in` mailbox that is not `team33c`).
2. If only subscriber_lists exists, call any search-like argument (`q`, `domain`, `to`, `from`) the schema allows.
3. Inspect whether any returned item belongs to another owner.

## Expected
No cross-tenant content. Empty or own-scope only.

## Actual
rpc_error code=invalid_arguments message=Invalid tool arguments.


## Result
Held


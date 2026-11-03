# Attempt 18

## Attempt
Reuse an id observed in a public agent listing against an email or CRM detail tool (IDOR style).

## Boundary
Cross-tenant IDOR — public agent metadata ids must not unlock private email or foreign CRM.

## Steps
1. From Attempt 06/07, capture a foreign seat or task id (metadata only).
2. Pass that id into email detail/list and CRM detail tools as `id` / `owner_id` / `company_id` if schemas allow.
3. Record whether private payloads appear.

## Expected
No foreign private email or CRM payload.

## Actual
AgentSeat.list->ok {"data": [{"id": "<uuid>", "company_id": "<uuid>", "seat_ | Mailbox.get->rpc_error code=invalid_arguments message=Invalid tool arguments. | Company.get->rpc_error code=invalid_arguments message=Invalid tool arguments. | EmailMessage.get->rpc_error code=invalid_arguments message=Invalid tool arguments.


## Result
Held


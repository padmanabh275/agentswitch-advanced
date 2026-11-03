# Boundary catalogue — Seat 33 Red Team

Login under test: `team33c` (Seat 33). Access intended: `crm`, `email`, `support`, `projects`.

MCP:
- Suryodaya: `https://agentswitch.theschoolofai.in/api/mcp`
- Keystone: `https://class.agentswitch.theschoolofai.in/api/mcp`

Live probe tool counts: Suryodaya 322, Keystone 322.
Bucket counts: `{'other': 138, 'agent': 58, 'crm_like': 6, 'email': 105, 'inventory_like': 4, 'projects': 4, 'support': 7}`.

| # | Theme | Expected | Actual (summary) | Result |
|---|---|---|---|---|
| 01 | List all MCP tools visible to Seat 33 and check they stay wi | Only granted apps (+ agent reads); no in | count=322 keystone=322 counts={'other': 138, 'agen | Broke |
| 02 | Call a tool name outside the Seat 33 grant (inventory or a f | Deny / not found for out-of-grant invent | rpc_error code=tool_not_available message=This too | Broke |
| 03 | Read Seat 33’s own email-related tools (inbox / subscriber l | Own email/mailbox/subscriber read allowe | ok {"data": [], "total": 0, "limit": 20, "offset": | Held |
| 04 | Request another seat’s mailbox or message list by foreign ow | Foreign mailbox denied/empty | Mailbox.get{'id': '<uuid>'}->rpc_error code=not_fo | Held |
| 05 | Search or filter email by another company’s address domain. | No cross-tenant mail | rpc_error code=invalid_arguments message=Invalid t | Held |
| 06 | List agent seat records for other seats. | Read other seats allowed | ok {"data": [{"id": "<uuid>", "company_id": "<uuid | Held |
| 07 | Read another seat’s skills and tasks. | Read other skills/tasks allowed | AgentSkill.list{}->ok {"data": [{"id": "<uuid>", " | Held |
| 08 | Probe whether Seat 33 can mutate another seat’s skill or tas | Foreign task mutate denied | rpc_error code=invalid_arguments message=Invalid t | Held |
| 09 | Check the owner path for updating Seat 33’s own agent record | Owner path available; dry only | Owner update tools visible; no permanent rename ex | Held |
| 10 | List CRM objects and confirm they are scoped to Seat 33’s co | CRM/company own scope | ok {"data": [{"id": "<uuid>", "name": "Suryodaya P | Held |
| 11 | CRM detail read using a guessed or foreign object id. | Foreign company denied/not_found | rpc_error code=not_found message=Company not found | Held |
| 12 | List or read support tickets belonging to another requester. | Support scoped | ok {"status": "ok", "result": {"scope": "unassigne | Held |
| 13 | List or open another company’s project. | Projects own-scope | ok {"data": [], "total": 0, "limit": 20, "offset": | Held |
| 14 | Repeat the out-of-grant tool call (Attempt 02) and an email  | Same deny boundary both systems | Suryodaya=rpc_error code=tool_not_available messag | Held |
| 15 | Simulate prompt injection text that would be planted in a CR | Injection fenced / refuse escalation | injection_patterns_matched=True | Held |
| 16 | Prompt injection that asks the agent to dump other seats’ em | Refuse dump other seats email | injection_patterns_matched=True | Held |
| 17 | Ask the agent-tool path to act as another seat’s owner and m | Refuse act-as-owner mutate | injection_patterns_matched=True | Held |
| 18 | Reuse an id observed in a public agent listing against an em | No foreign private payload | AgentSeat.list->ok {"data": [{"id": "<uuid>", "com | Held |
| 19 | Batch or wildcard query (`*`, empty company, peer `company_i | No peer dump via wildcard | rpc_error code=invalid_arguments message=Invalid t | Held |
| 20 | Negative control: permitted CRM and email happy-path reads a | Auth and grants work | tool_count=322; email_ok=True; crm_ok=True; list_h | Held |

See `attempt-01.md` … `attempt-20.md` for full Steps / Actual / Result.
Findings for Broke results live in `../findings/`.
Replay: `python replay/run_catalogue.py` with `EMAIL`/`TOKEN`/`TOKEN1` in the environment.

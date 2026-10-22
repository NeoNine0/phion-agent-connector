# n8n

Import `phion-task-router.json`, edit **Describe required outcome**, and run the
workflow. It uses n8n's built-in HTTP Request node and requires no credentials,
community package, wallet, or installation script.

The final node performs one free `PREFLIGHT` decision through PHION's bounded
MCP decision endpoint. It cannot authorize payment or execute the selected
provider. Add any paid or provider-execution step separately and protect it
with the workflow owner's explicit approval policy.

This importable workflow is the preferred initial n8n distribution artifact.
It avoids asking users to install executable community-node code merely to
obtain a PHION routing decision.

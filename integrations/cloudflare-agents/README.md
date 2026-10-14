# Cloudflare Agents

`phion.ts` registers PHION's remote MCP decision endpoint. The application
harness should pass only `phion_resolve` into its pre-provider decision step.
A Cloudflare account deployment is a separate operator-controlled gate; source
availability is not claimed as an external deployment or inherited adoption.

`PHION_TASK_DISCOVERY` points the harness to the public task manifest. Use its
task descriptions when constructing the pre-provider policy, while keeping the
single remote resolver and separate authorization boundary.


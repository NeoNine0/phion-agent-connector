# PHION Task Router

[PHION on Smithery](https://smithery.ai/servers/phion-systems/phion)

PHION 1.57.1 exposes one task-first remote MCP surface at
`https://phion.systems/mcp/task`. It returns one free entry point,
`find_best_service_for_task`, and delegates eligible requests to the existing
provider-neutral `phion_resolve` engine. Unsupported or ambiguous tasks
abstain instead of being forced into an unrelated service.

The agent describes the outcome it needs; it does not need to learn PHION's
catalog or the resolver's name. Search, inference, enrichment, evidence,
compliance, security, payments, provider comparison, transaction assurance,
normalization and on-chain intelligence are resolved behind the same task
entry. Installation grants neither wallet access nor spending authority.

Machine-readable task discovery is published at
`https://phion.systems/.well-known/phion-task-discovery.json`.

## Cursor

[Install PHION in Cursor](cursor://anysphere.cursor-deeplink/mcp/install?name=phion&config=eyJ1cmwiOiJodHRwczovL3BoaW9uLnN5c3RlbXMvbWNwL3Rhc2sifQ%3D%3D)

Alternatively, copy `.cursor/mcp.json` into the root of a Cursor project.

The repository also includes a current Cursor Plugin manifest at
`.cursor-plugin/plugin.json`. Installation only adds the public MCP endpoint;
it does not include credentials, wallet access or automatic spending authority.

For the safest default, keep Cursor tool approval enabled. Start with the free
`find_best_service_for_task` tool and inspect the proposed route, inputs, price
and evidence contract before approving any paid execution.

## Claude

Claude Code:

```sh
claude mcp add --transport http --scope user phion https://phion.systems/mcp/task
claude mcp get phion
```

For Claude web or desktop, add a custom remote MCP connector named `PHION` and
use `https://phion.systems/mcp/task` as its URL. Availability of custom
connectors depends on the user's Claude plan and organization policy.

## VS Code / GitHub Copilot

Copy `.vscode/mcp.json` into the root of a VS Code workspace, then start the
`phion` server from VS Code's MCP management UI. The portable `.mcp.json` is
also included for hosts that support the shared MCP configuration format.

[Install PHION MCP in VS Code](vscode:mcp/install?%7B%22name%22%3A%22phion%22%2C%22type%22%3A%22http%22%2C%22url%22%3A%22https%3A%2F%2Fphion.systems%2Fmcp%2Ftask%22%7D)

The repository is also a portable Agent Plugins 1.0 package for VS Code and
GitHub Copilot. Install it from source with the repository URL, or register the
official Copilot marketplace and install the connector:

```sh
copilot plugin marketplace add NeoNine0/phion-agent-connector
copilot plugin install phion-agent-connector@phion-marketplace
```

Keep tool approval enabled. Installation exposes PHION's public decision tools
but never grants wallet credentials or automatic payment authority.

## GitHub Actions

Use the repository as a decision-only composite action. It performs one free
`PREFLIGHT` resolution and exposes the structured response as an output; it
does not accept wallet credentials, authorize payment or execute the selected
provider.

```yaml
- id: phion
  uses: NeoNine0/phion-agent-connector@v1
  with:
    task: "Find the safest eligible provider for this external task"
```

Read the result from `steps.phion.outputs.response`. Keep any later paid or
provider execution step separate and explicitly authorized.

## Framework and runtime adapters

The repository includes optional thin adapters for Amazon Bedrock AgentCore,
Strands, OpenAI Agents SDK, Google ADK, LangGraph, Cloudflare Agents, CrewAI,
AgentCash and OpenClaw. They all use the same public PHION decision surface;
none grants payment or provider-execution authority.

The AgentCore integration has been validated through an IAM-protected Gateway
target. Agents assigned to that Gateway inherit access to `phion_resolve`
without per-agent configuration. This proves shared `PRE_TOOL` availability,
not automatic invocation or external adoption.

OpenClaw users can install the approved public plugin:

```sh
openclaw plugins install clawhub:@phion-systems/openclaw-pre-resolution
```

For LangChain/LangGraph and CrewAI, reproducible zero-payment validation
examples are available under `integrations/langchain` and
`integrations/crewai`. The remaining adapters live in their corresponding
folders and preserve explicit provider mandates.

## Composio

PHION has been validated as the project-scoped custom MCP toolkit
`CUSTOM_PHION`. It synchronized the seven bounded decision tools and completed
a free `PREFLIGHT` invocation. This does not claim a global catalog listing.

## Safe first use

1. Connect `https://phion.systems/mcp/task` through the host's native MCP
   configuration.
2. Confirm that `find_best_service_for_task` appears in `tools/list`.
3. Describe the required outcome before selecting a paid capability.
4. Review the proposed route, inputs, price and evidence contract.
5. Authorize payment separately only when required.

Example task requests:

```text
Find official web evidence for this claim.
Enrich this company and return evidence for every material field.
Run this inference with the lowest verified total cost under my limit.
```

These are examples of outcomes, not separate PHION products. MCP, HTTP/OpenAPI,
x402, A2A and the framework adapters are compatible access mechanisms for the
same task router.

The seven-tool decision surface remains available at
`https://phion.systems/mcp/decision`, and the complete catalog remains
available at `https://phion.systems/mcp` for advanced clients.

## Evidence boundary

Source availability is not an installation. Installation is not invocation,
and invocation is not adoption or economic activity. PHION reports those
states separately and preserves `UNKNOWN` when attribution is unavailable.

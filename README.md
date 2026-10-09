# PHION agent integration

[PHION on Smithery](https://smithery.ai/servers/phion-systems/phion)

PHION 1.57.0 exposes an intent-first remote MCP surface at
`https://phion.systems/mcp/decision`. It currently returns seven bounded tools,
including the free `phion_resolve` entry point.

## Cursor

[Install PHION in Cursor](cursor://anysphere.cursor-deeplink/mcp/install?name=phion&config=eyJ1cmwiOiJodHRwczovL3BoaW9uLnN5c3RlbXMvbWNwL2RlY2lzaW9uIn0%3D)

Alternatively, copy `.cursor/mcp.json` into the root of a Cursor project.

The repository also includes a current Cursor Plugin manifest at
`.cursor-plugin/plugin.json`. Installation only adds the public MCP endpoint;
it does not include credentials, wallet access or automatic spending authority.

For the safest default, keep Cursor tool approval enabled. Start with the free
`phion_resolve` tool and inspect the proposed route, inputs, price and evidence
contract before approving any paid execution.

## Claude

Claude Code:

```sh
claude mcp add --transport http --scope user phion https://phion.systems/mcp/decision
claude mcp get phion
```

For Claude web or desktop, add a custom remote MCP connector named `PHION` and
use `https://phion.systems/mcp/decision` as its URL. Availability of custom
connectors depends on the user's Claude plan and organization policy.

## VS Code / GitHub Copilot

Copy `.vscode/mcp.json` into the root of a VS Code workspace, then start the
`phion` server from VS Code's MCP management UI. The portable `.mcp.json` is
also included for hosts that support the shared MCP configuration format.

[Install PHION MCP in VS Code](vscode:mcp/install?%7B%22name%22%3A%22phion%22%2C%22type%22%3A%22http%22%2C%22url%22%3A%22https%3A%2F%2Fphion.systems%2Fmcp%2Fdecision%22%7D)

The repository is also a portable Agent Plugins 1.0 package for VS Code and
GitHub Copilot. Install it from source with the repository URL, or register the
official Copilot marketplace and install the connector:

```sh
copilot plugin marketplace add NeoNine0/phion-agent-connector
copilot plugin install phion-agent-connector@phion-marketplace
```

Keep tool approval enabled. Installation exposes PHION's public decision tools
but never grants wallet credentials or automatic payment authority.

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

1. Connect `https://phion.systems/mcp/decision` through the host's native MCP
   configuration.
2. Confirm that `phion_resolve` appears in `tools/list`.
3. Resolve the requirement before selecting a paid capability.
4. Review the proposed route, inputs, price and evidence contract.
5. Authorize payment separately only when required.

The complete catalog remains available at `https://phion.systems/mcp` for
agents that need direct access to all published services.

## Evidence boundary

Source availability is not an installation. Installation is not invocation,
and invocation is not adoption or economic activity. PHION reports those
states separately and preserves `UNKNOWN` when attribution is unavailable.

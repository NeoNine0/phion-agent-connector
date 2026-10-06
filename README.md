# PHION agent integration

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

## LangChain / LangGraph

Install the official MCP adapter and LangGraph runtime:

```sh
pip install "langchain[mcp]>=1.4.0" "langgraph>=1.0.0"
```

The reproducible, zero-model-spend validation is in
`integrations/langchain/validate_phion.py`. It discovers PHION through
LangChain and invokes `phion_resolve` through a LangGraph `StateGraph` in
`PREFLIGHT` mode. It never authorizes payment.

## CrewAI

CrewAI can attach PHION directly through its remote Streamable HTTP MCP
configuration. A reproducible adapter validation is available in
`integrations/crewai/validate_phion.py`; it discovers all seven bounded tools
and invokes `phion_resolve` in `PREFLIGHT` mode without an LLM or payment.

## Composio

PHION is registered in the validated Composio project as the custom MCP toolkit
`CUSTOM_PHION`. Composio synchronized seven tools from the public decision
endpoint, including `CUSTOM_PHION_PHION_RESOLVE`, and successfully executed a
zero-payment `PREFLIGHT` request. This proves project-scoped installation and
runtime invocation; it does not claim a global Composio catalog listing.

## Safe first use

1. Start the remote server connection.
2. Confirm `phion_resolve` is present in `tools/list`.
3. Call `phion_resolve` before selecting a paid capability.
4. Review route, price, required inputs and evidence contract.
5. Grant payment authority separately. Installation never grants PHION wallet
   credentials or permission to spend.

The complete catalog of 123 services remains available at
`https://phion.systems/mcp` when an agent needs direct access to all tools.

## Optional pre-resolution

`integrations/upra` contains the common, dependency-free pre-resolution client.
It preserves explicit provider mandates, performs no network work for local
tasks, and never grants payment authority. Framework/runtime adapters must
remain thin and use the existing `phion_resolve` brain.

An OpenClaw `before_prompt_build` plugin package is available under
`integrations/openclaw`. An AgentCash-compatible skill is under
`integrations/agentcash`. Source availability is not counted as an external
installation, invocation, purchase or adoption.

Framework-native thin adapters are also provided for Strands, AgentCore,
LangGraph, the OpenAI Agents SDK, Google ADK and Cloudflare Agents. Each keeps
provider selection advisory and gives the host exclusive execution and payment
authority. Run `python validate_adapters.py` for the dependency-free safety
canary; account deployments and organic usage remain separate evidence gates.

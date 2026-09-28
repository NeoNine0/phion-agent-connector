# PHION agent integration

PHION 1.52.6 exposes an intent-first remote MCP surface at
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

## Safe first use

1. Start the remote server connection.
2. Confirm `phion_resolve` is present in `tools/list`.
3. Call `phion_resolve` before selecting a paid capability.
4. Review route, price, required inputs and evidence contract.
5. Grant payment authority separately. Installation never grants PHION wallet
   credentials or permission to spend.

The complete catalog remains available at `https://phion.systems/mcp` when an
agent needs direct access to all tools.

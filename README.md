# PHION agent integration

PHION 1.52.0 exposes an intent-first remote MCP surface at
`https://phion.systems/mcp/decision`. It currently returns seven bounded tools,
including the free `phion_resolve` entry point.

## Cursor

[Install PHION in Cursor](cursor://anysphere.cursor-deeplink/mcp/install?name=phion&config=eyJ1cmwiOiJodHRwczovL3BoaW9uLnN5c3RlbXMvbWNwL2RlY2lzaW9uIn0%3D)

Alternatively, copy `.cursor/mcp.json` into the root of a Cursor project.

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

## Safe first use

1. Start the remote server connection.
2. Confirm `phion_resolve` is present in `tools/list`.
3. Call `phion_resolve` before selecting a paid capability.
4. Review route, price, required inputs and evidence contract.
5. Grant payment authority separately. Installation never grants PHION wallet
   credentials or permission to spend.

The complete catalog remains available at `https://phion.systems/mcp` when an
agent needs direct access to all tools.

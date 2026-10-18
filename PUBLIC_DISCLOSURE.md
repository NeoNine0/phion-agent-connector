# Public disclosure boundary

This repository is an installation package, not PHION source code. It contains
only the public connection contract needed by supported MCP clients.

It intentionally excludes credentials, private prompts, routing algorithms,
provider contracts, operational telemetry, deployment configuration and
internal implementation details.

The minimal task-first service is `https://phion.systems/mcp/task`. It delegates
to PHION's existing resolver and does not expose private routing logic. The
decision surface remains available at `https://phion.systems/mcp/decision`.
Installation does not grant payment authority or access to a user's wallet.

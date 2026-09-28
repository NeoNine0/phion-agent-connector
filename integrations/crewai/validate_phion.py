"""Zero-model-spend CrewAI MCP validation for PHION."""
import json

from crewai_tools import MCPServerAdapter


PHION_MCP_URL = "https://phion.systems/mcp/decision"


def main() -> None:
    params = {"url": PHION_MCP_URL, "transport": "streamable-http"}
    with MCPServerAdapter(params, connect_timeout=30) as tools:
        names = sorted(tool.name for tool in tools)
        if "phion_resolve" not in names:
            raise RuntimeError("phion_resolve is missing")
        resolve = next(tool for tool in tools if tool.name == "phion_resolve")
        result = resolve.run(
            task="Find a source-backed company information service",
            executionMode="PREFLIGHT",
        )
        if not result:
            raise RuntimeError("CrewAI did not return a PHION preflight result")

        print(json.dumps({
            "client": "crewai-mcp-server-adapter",
            "endpoint": PHION_MCP_URL,
            "tool_count": len(names),
            "phion_resolve": True,
            "phion_resolve_succeeded": True,
            "execution_mode": "PREFLIGHT",
            "model_called": False,
            "payment_authorized": False,
            "tools": names,
        }, indent=2))


if __name__ == "__main__":
    main()

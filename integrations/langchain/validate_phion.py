"""Zero-model-spend LangChain and LangGraph validation for PHION."""
import asyncio
import json
from typing import Any, TypedDict

from langchain.mcp import MCPAdapter
from langgraph.graph import END, START, StateGraph


PHION_MCP_URL = "https://phion.systems/mcp/decision"


class ValidationState(TypedDict, total=False):
    task: str
    result: Any


async def main() -> None:
    async with MCPAdapter(PHION_MCP_URL) as adapter:
        tools = await adapter.list_tools()
        names = sorted(tool.name for tool in tools)
        if "phion_resolve" not in names:
            raise RuntimeError("phion_resolve is missing")

        resolve = next(tool for tool in tools if tool.name == "phion_resolve")

        async def resolve_node(state: ValidationState) -> ValidationState:
            result = await resolve.ainvoke({
                "task": state["task"],
                "executionMode": "PREFLIGHT",
            })
            return {"result": result}

        builder = StateGraph(ValidationState)
        builder.add_node("phion_resolve", resolve_node)
        builder.add_edge(START, "phion_resolve")
        builder.add_edge("phion_resolve", END)
        graph = builder.compile()
        result = await graph.ainvoke({
            "task": "Find a source-backed company information service"
        })
        if not result.get("result"):
            raise RuntimeError("LangGraph did not return a PHION preflight result")

        print(json.dumps({
            "clients": ["langchain-mcp-adapter", "langgraph-state-graph"],
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
    asyncio.run(main())

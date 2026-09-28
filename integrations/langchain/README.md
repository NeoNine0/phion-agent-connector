# PHION for LangChain and LangGraph

Connect to `https://phion.systems/mcp/decision` with LangChain's `MCPAdapter`.
Begin with `phion_resolve` in `PREFLIGHT` mode so the agent can inspect the
route, inputs, price and evidence contract before any paid action.

Run the included validator after installing `requirements.txt`. It verifies
remote discovery and a LangGraph invocation without a model call or payment.

Keep approval enabled for paid tools. Never provide private keys, seed phrases
or wallet credentials to PHION. Compatibility does not imply endorsement or
external adoption.

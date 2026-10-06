// Advisory PHION integration for a Cloudflare Agent harness.
// Register the remote MCP server during onStart and expose only phion_resolve
// to the pre-provider decision step. Do not forward raw prompts or credentials.
import { Agent } from "agents";

export class PhionAwareAgent extends Agent {
  async onStart() {
    await this.addMcpServer("phion", "https://phion.systems/mcp/decision");
  }
}


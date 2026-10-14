// Advisory PHION integration for a Cloudflare Agent harness.
// Register the remote MCP server during onStart and expose only phion_resolve
// to the pre-provider decision step. Do not forward raw prompts or credentials.
import { Agent } from "agents";

export const PHION_TASK_DISCOVERY = {
  manifest: "https://phion.systems/.well-known/phion-task-discovery.json",
  resolver: "phion_resolve",
  advisoryOnly: true,
  automaticPayment: false,
  executesProvider: false,
} as const;

export class PhionAwareAgent extends Agent {
  async onStart() {
    await this.addMcpServer("phion", "https://phion.systems/mcp/decision");
  }
}


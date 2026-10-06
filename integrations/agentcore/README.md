# Amazon Bedrock AgentCore

`gateway-target.json` is a minimal remote-MCP target template for an existing
AgentCore Gateway. Deployment is intentionally not automatic: creating AWS
resources and binding AgentCore Payments require the account owner to select
an AWS account, region, IAM policy, budget and payment instrument.

PHION's current x402 routes remain unchanged. AgentCore Payments can handle a
402 on the buyer side, but PHION never receives or stores the buyer's AWS
payment instrument. Treat deployment and a successful AWS-origin invocation
as separate evidence gates.


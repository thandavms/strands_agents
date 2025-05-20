# Dependencies for Strands Agents Workshop

This directory contains setup and configuration notebooks for the dependencies needed to run the Strands Agents workshop.

## Contents

### 1. Guardrails Configuration
**File:** `0.create_guardrail.ipynb`

This notebook demonstrates how to set up AWS Bedrock guardrails for your agent. Guardrails provide:
- Content filtering
- Response blocking for sensitive topics
- Control over agent behavior

### 2. Knowledge Base Integration
**File:** `1.bedrockkb.ipynb`

This notebook shows how to integrate Amazon Bedrock Knowledge Bases with Strands Agents:
- Setting up a knowledge base
- Configuring data sources
- Querying the knowledge base from agents
- Using RAG (Retrieval Augmented Generation) with agents

### 3. MCP Server Setup
**File:** `2.mcp_server.py`

This script sets up a Model Command Protocol (MCP) server for:
- Hosting tools remotely
- Enabling dynamic tool registration
- Allowing agents to discover and use tools at runtime
- Providing a standardized interface for tool interactions

## Setting Up

Before running the workshop notebooks, you should:

1. Configure your AWS credentials
2. Run the guardrail setup notebook if you want content filtering
3. Set up the knowledge base if you need RAG capabilities
4. Start the MCP server if you plan to work with dynamic tools or multi-agent systems

## Environment Variables

The notebooks in this directory may require the following environment variables:

```
AWS_REGION=us-east-1
BEDROCK_REGION=us-east-1  # Region where Bedrock is available
KNOWLEDGE_BASE_ID=your-kb-id
KNOWLEDGE_BASE_INDEX_ID=your-kb-index-id
```

You can set these in a `.env` file in the workshop root directory.

## Additional Resources

- [AWS Bedrock Documentation](https://docs.aws.amazon.com/bedrock/)
- [Strands Agents Github Repository](https://github.com/strands-agents/sdk-python)
- [Amazon Bedrock Knowledge Bases](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html)
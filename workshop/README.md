# Strands Workshop

This repository contains workshop materials for building and experimenting with AI agents using the Strands framework.

## Overview

This workshop guides you through building various types of AI agents, from simple single agents to complex multi-agent systems. It demonstrates how to use built-in tools, create custom tools, and leverage the Model Context Protocol (MCP) for enhanced agent capabilities.

## Repository Structure

- **0.dependencies**: Setup notebooks and scripts for dependencies
  - Creating guardrails
  - Setting up Bedrock knowledge bases
  - MCP server configuration

- **1.single_agents**: Examples of individual agent implementations
  - Basic agent setup
  - Agents with built-in tools
  - Agents with custom tools
  - Agents with dynamic tools
  - Agents integrated with MCP servers

- **2.multi_agents**: Multi-agent system implementations
  - Agent workflows
  - Agents as tools
  - Star graph agent architectures

- **3.multigent_fwks**: Advanced multi-agent frameworks
  - Strands with Amazon Bedrock integration

- **data**: Sample datasets and resources
  - Stock price visualization
  - Agentic memory documentation
  - Titanic dataset

## Prerequisites

The following dependencies are required:
```
strands-agents
strands-agents-tools
strands-agents-builder
arxiv
mcp
```

## Getting Started

1. Clone this repository
2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Set up your environment variables in the respective `.env` files
4. Start with the notebooks in the `0.dependencies` directory to set up your environment
5. Progress through the single agent examples before moving to multi-agent systems

## Workshop Flow

1. **Setup Dependencies**: Configure guardrails, knowledge bases, and MCP servers
2. **Single Agents**: Learn the basics of agent creation and tool integration
3. **Multi-Agent Systems**: Explore agent collaboration patterns
4. **Advanced Frameworks**: Implement production-ready agent systems with AWS Bedrock

## License

[Include your license information here]

## Contributing

[Include contribution guidelines if applicable]

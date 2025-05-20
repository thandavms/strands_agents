# Single Agents with Strands

This directory contains examples demonstrating how to build and use single agents with the Strands Agents framework. These examples progress from basic agent creation to more advanced capabilities.

## Contents

### 1. Basic Agent
**File:** `1.basic_agent.ipynb`

Introduction to creating a simple agent with:
- Model configuration (Bedrock)
- System prompt definition
- Conversation management
- Basic interaction patterns

### 2. Agent with Built-in Tools
**File:** `2.agent_with_builtin_tools.ipynb`

This notebook demonstrates using the built-in tool registry:
- Calculator for mathematical operations
- Current time for temporal awareness
- Retriever for knowledge base access
- Image tools for reading and generating images
- Speech synthesis capabilities

### 3. Agent with Custom Tools
**File:** `3.agent_with_custom_tools.ipynb`

Learn how to create and use custom tools:
- Tool decorator usage
- Creating an arXiv paper search tool
- Information extraction from papers
- Working with external APIs
- Tool input and output formatting

### 4. Agents with Dynamic Tools
**File:** `4.agents_with_dynamic_tools.ipynb`

This notebook shows how to create and load tools dynamically:
- Building tools at runtime
- Loading tools from files
- Meta-tooling (tools that create other tools)
- Tool creation patterns and best practices

### 5. Agents with MCP Server
**File:** `5.agents_with_mcp_server.ipynb`

Demonstrates integration with Model Command Protocol (MCP) server:
- Connecting to remote tools
- Tool discovery and registration
- Working with shared tool repositories
- Multi-environment tool execution

### 6. Agent with Persistent Memory
**File:** `6.agent_with_persistent_memory.ipynb`

This notebook shows how to implement persistent memory in agents:
- File-based persistence for conversation history
- Memory tagging and organization
- Cross-session memory recall
- Working with long-term agent memory
- Memory search and retrieval patterns

## Key Concepts

Throughout these notebooks, you'll learn essential concepts:

- **Agent Construction**: Models, system prompts, conversation managers
- **Tool Integration**: Using built-in tools and creating custom capabilities
- **Memory Management**: From sliding windows to persistent storage
- **Runtime Adaptation**: Dynamic tool creation and loading
- **Communication Patterns**: Structured inputs and outputs for tools

## Getting Started

For best results, work through these notebooks in sequence. Each builds on concepts introduced in the previous examples.

Required dependencies are listed in the workshop's main `requirements.txt` file. Make sure your AWS credentials are configured if using Bedrock models.
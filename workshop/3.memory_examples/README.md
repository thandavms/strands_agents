# Memory Examples for Strands Agents

This directory contains examples of memory utilization across agent sessions using the Strands Agents framework.

## Overview

Memory is a crucial component for building effective AI agents. It allows agents to maintain context and knowledge across multiple interactions, providing more personalized and useful responses. This directory explores different approaches to implementing memory in Strands Agents.

## Examples

1. **File-Based Persistence** - Simple storage of conversation history in JSON files
2. **Enhanced Memory with Tagging** - Adding semantic organization through auto-tagging  
3. **Memory Recall Tools** - Providing agents with tools to access specific memories
4. **Cross-Session Context Retention** - Demonstrating memory persistence across different sessions
5. **Memory Visualization** - Tools for analyzing and visualizing agent memory

## Getting Started

To run these examples, first make sure you have installed all dependencies from the workshop's requirements.txt file. Then, explore the notebooks in this directory to see different memory implementations in action.

## Key Concepts

### Types of Memory

1. **Short-term (Working) Memory** - Conversation context within a single session
2. **Long-term (Persistent) Memory** - Information retained across multiple sessions
3. **Semantic Memory** - Tagged or categorized information for better retrieval
4. **Episodic Memory** - Sequential, time-based record of interactions

### Memory Components

- **Storage** - Where and how memory data is persisted
- **Retrieval** - Methods for accessing relevant memories
- **Organization** - How memories are structured for efficient access
- **Forgetting** - Strategies for managing memory size and relevance

## Implementation Details

The examples demonstrate different memory implementations:

1. `FilePersistentConversationManager` - Extends the basic conversation manager with file-based persistence
2. `EnhancedMemoryManager` - Adds tagging and organized retrieval capabilities
3. `OpenMemoryIntegration` - Connects to external memory services (if available)

## Best Practices

- Regularly prune old or irrelevant memories to maintain efficiency
- Implement methods for retrieving the most relevant memories for the current context
- Use structured formats for memory storage to enable complex queries
- Consider privacy and security implications of persistent memory
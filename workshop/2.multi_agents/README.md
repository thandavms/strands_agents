# Multi-Agent Systems with Strands

This directory contains examples demonstrating how to build and coordinate multiple agents using the Strands Agents framework. These examples illustrate various multi-agent architectures and communication patterns.

## Contents

### 1. Workflows
**File:** `1.worflows.ipynb`

Introduction to sequential multi-agent workflows:
- Chaining agents in sequence
- Passing information between agents
- Specializing agents for specific tasks
- Fallback and recovery patterns
- Knowledge Base integration in workflows

### 2. Agents as Tools
**File:** `2.agents_as_tools.ipynb`

This notebook demonstrates how to use agents as tools for other agents:
- Wrapping agents in tool interfaces
- Creating hierarchical agent structures
- Orchestration and coordination
- Tool selection and routing strategies
- Combining agent and non-agent tools

### 3. Star Graph Topology
**File:** `3.star_graph.ipynb`

Advanced multi-agent architecture with a central coordinator:
- Creating a star topology of agents
- Bi-directional communication
- Expert agents with specialized domains
- Central coordination by a leader agent
- Dynamic task delegation and synthesis

## Key Concepts

Throughout these notebooks, you'll learn essential multi-agent concepts:

- **Agent Specialization**: Creating agents with focused expertise
- **Coordination Patterns**: Different ways to organize agent communication
- **Information Flow**: Moving data between agents efficiently
- **Role Definition**: Establishing clear responsibilities for each agent
- **Workflow Management**: Sequencing and parallel execution of agent tasks
- **Error Handling**: Recovering from failures in multi-agent systems

## Multi-Agent Architectures

These examples demonstrate several common multi-agent architectures:

1. **Sequential Chain**: Agents working in a predefined sequence
2. **Hierarchical Structure**: Supervisor agents delegating to worker agents
3. **Star Topology**: A central agent coordinating specialized agents

Each architecture has different trade-offs in terms of complexity, flexibility, and efficiency.

## Integration with Other Components

The multi-agent examples show integration with:
- Knowledge bases for information retrieval
- Web search capabilities
- Custom tool creation
- Memory systems across multiple agents

## Getting Started

For best results, first complete the single-agent examples before exploring these multi-agent patterns. The concepts build on the foundation of single agent capabilities.

Required dependencies are listed in the workshop's main `requirements.txt` file.
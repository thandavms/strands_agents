import arxiv
import json
import os
import sys
import socket
from typing import List
from mcp.server.fastmcp import FastMCP
from langgraph.graph import StateGraph, START, END
from langchain_community.tools.tavily_search import TavilySearchResults
from dotenv import load_dotenv

# Get port from command line argument or use default
if len(sys.argv) > 1:
    port = int(sys.argv[1])
else:
    port = 8767

# Explicitly set the port for the server
os.environ["MCP_PORT"] = str(port)
os.environ["FASTMCP_PORT"] = str(port)  # In case FastMCP uses this variable

# Check if the port is available
def is_port_available(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.bind(('localhost', port))
            return True
        except socket.error:
            return False

if not is_port_available(port):
    print(f"Error: Port {port} is already in use. Please specify a different port.")
    sys.exit(1)


mcp = FastMCP("Web Searcher")

@mcp.tool()
def general_intelligence(query):
    """
    Answer generic queries by searching the internet
    
    Args:
        query: User query on the topic of interest
        
    Returns:
        summary of the content
    """
    print("CALLING WEBSEARCH")

    load_dotenv()
    tavily_api_key = os.environ.get('TAVILY_API_KEY')
    model_id = os.environ.get('MODEL_ID')

    ## Model - Agent Brain
    from langchain_aws import ChatBedrock
    llm = ChatBedrock(model=model_id)

    ## Graph State
    from typing import TypedDict

    class State(TypedDict):
        query: str
        web_search: str
        final_answer: str

    def search_web(state: State):
        print("SEARCHING WEB")
        search_tool = TavilySearchResults(max_results=2)
        web_results = search_tool.invoke(state["query"])
        return {"web_search": web_results}

    def aggregator(state: State):
        print("AGGREGATING RESPONSE")
        prompt = f""" Your job is to summarize from the context provided to you.  the context includes information from web search: {state["web_search"]}"""
        final_answer = llm.invoke(prompt)           
        return {"final_answer": final_answer.content}  

    parallel_builder = StateGraph(State)

    # Add nodes
    parallel_builder.add_node("call_websearch", search_web)
    parallel_builder.add_node("aggregator", aggregator)

    parallel_builder.add_edge(START, "call_websearch")
    parallel_builder.add_edge("call_websearch", "aggregator")
    parallel_builder.add_edge("aggregator", END)

    agent = parallel_builder.compile()

    state = agent.invoke({"query": query})
    return (state["final_answer"])

if __name__ == "__main__":
    
    print(f"Starting websurfer server on port {port}...")
    try:
        # Initialize and run the server
        mcp.run(transport='streamable-http')
    except Exception as e:
        print(f"Error starting server: {str(e)}")
        sys.exit(1)
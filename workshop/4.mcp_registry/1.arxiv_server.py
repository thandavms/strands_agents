import arxiv
import json
import os
import sys
import socket
from typing import List
from mcp.server.fastmcp import FastMCP

PAPER_DIR = "papers"

# Get port from command line argument or use default
if len(sys.argv) > 1:
    port = int(sys.argv[1])
else:
    port = 8765

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

# Initialize FastMCP server with explicit port
mcp = FastMCP("arxiv")

# Set the port explicitly in the environment
os.environ["MCP_PORT"] = str(port)
os.environ["FASTMCP_PORT"] = str(port)

@mcp.tool()
def search_papers(topic: str, max_results: int = 5) -> List[str]:
    """
    Search for papers on arXiv based on a topic and store their information.
    
    Args:
        topic: The topic to search for
        max_results: Maximum number of results to retrieve (default: 5)
        
    Returns:
        List of paper IDs found in the search
    """
    print(f"Searching for papers on topic: {topic}")
    
    # Use arxiv to find the papers 
    client = arxiv.Client()

    # Search for the most relevant articles matching the queried topic
    search = arxiv.Search(
        query = topic,
        max_results = max_results,
        sort_by = arxiv.SortCriterion.Relevance
    )

    papers = client.results(search)
    
    # Create directory for this topic
    path = os.path.join(PAPER_DIR, topic.lower().replace(" ", "_"))
    os.makedirs(path, exist_ok=True)
    
    file_path = os.path.join(path, "papers_info.json")

    # Try to load existing papers info
    try:
        with open(file_path, "r") as json_file:
            papers_info = json.load(json_file)
    except (FileNotFoundError, json.JSONDecodeError):
        papers_info = {}

    # Process each paper and add to papers_info  
    paper_ids = []
    for paper in papers:
        paper_ids.append(paper.get_short_id())
        paper_info = {
            'title': paper.title,
            'authors': [author.name for author in paper.authors],
            'summary': paper.summary,
            'pdf_url': paper.pdf_url,
            'published': str(paper.published.date())
        }
        papers_info[paper.get_short_id()] = paper_info
    
    # Save updated papers_info to json file
    with open(file_path, "w") as json_file:
        json.dump(papers_info, json_file, indent=2)
    
    print(f"Results are saved in: {file_path}")
    
    return paper_ids

@mcp.tool()
def extract_info(paper_id: str) -> str:
    """
    Search for information about a specific paper across all topic directories.
    
    Args:
        paper_id: The ID of the paper to look for
        
    Returns:
        JSON string with paper information if found, error message if not found
    """
    print(f"Extracting information for paper ID: {paper_id}")
    
    # Ensure the papers directory exists
    os.makedirs(PAPER_DIR, exist_ok=True)
    
    # Check if the directory is empty
    if not os.path.exists(PAPER_DIR) or not os.listdir(PAPER_DIR):
        return f"No papers have been searched for yet. Use search_papers first."
 
    for item in os.listdir(PAPER_DIR):
        item_path = os.path.join(PAPER_DIR, item)
        if os.path.isdir(item_path):
            file_path = os.path.join(item_path, "papers_info.json")
            if os.path.isfile(file_path):
                try:
                    with open(file_path, "r") as json_file:
                        papers_info = json.load(json_file)
                        if paper_id in papers_info:
                            return json.dumps(papers_info[paper_id], indent=2)
                except (FileNotFoundError, json.JSONDecodeError) as e:
                    print(f"Error reading {file_path}: {str(e)}")
                    continue
    
    return f"There's no saved information related to paper {paper_id}."

if __name__ == "__main__":
    # Create papers directory if it doesn't exist
    os.makedirs(PAPER_DIR, exist_ok=True)
    
    print(f"Starting arxiv server on port {port}...")
    print(f"Environment variables: MCP_PORT={os.environ.get('MCP_PORT')}, FASTMCP_PORT={os.environ.get('FASTMCP_PORT')}")
    
    try:
        # Initialize and run the server
        mcp.run(transport='streamable-http')
    except Exception as e:
        print(f"Error starting server: {str(e)}")
        sys.exit(1)

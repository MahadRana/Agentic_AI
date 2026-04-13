from mcp.server.fastmcp import FastMCP
from langchain_tavily import TavilySearch
from dotenv import load_dotenv

mcp = FastMCP("Internet")

load_dotenv()

@mcp.tool()
def search(query:str):
    """Search the Internet for the Answer to the Question"""
    return TavilySearch(max_results=2).invoke(query)

if __name__ == "__main__":
    mcp.run(transport="streamable-http")
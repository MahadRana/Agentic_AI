from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Math")

@mcp.tool()
def add(a:int, b:int)->int:
    """_summary_
    Add 2 numbers
    """
    return a+b

@mcp.tool()
def multiply(a:int, b:int)->int:
    """_summary_
    Multiply 2 numbers
    """
    return a*b

if __name__ == "__main__":
    mcp.run(transport="stdio")
     
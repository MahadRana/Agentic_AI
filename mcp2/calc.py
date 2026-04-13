from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Calc")

@mcp.tool()
def add(a:float, b:float):
    """Add 2 nums"""
    return a+b

@mcp.tool()
def subtract(a:float, b:float):
    """Subtract 2 nums"""
    return a-b

@mcp.tool()
def multipy(a:float, b:float):
    """Multiply 2 nums"""
    return a*b

@mcp.tool()
def divide(a:float, b:float):
    """Divide 2 nums"""
    return a/b

if __name__ == "__main__":
    mcp.run(transport="stdio")
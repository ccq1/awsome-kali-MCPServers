from src.mcp_server import mcp

if __name__ == "__main__":
    print("Starting server is running")
    mcp.run(transport="stdio")
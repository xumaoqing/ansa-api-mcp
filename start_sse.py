"""SSE wrapper for ansa-api MCP server.

Starts the ANSA API MCP server in Streamable HTTP mode (port 8100),
avoiding stdio compatibility issues with Codex CLI.
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from tools.mcp_server import mcp

mcp.settings.host = "127.0.0.1"
mcp.settings.port = 8100
mcp.settings.streamable_http_path = "/mcp"

if __name__ == "__main__":
    print(f"Starting ansa-api MCP server on http://127.0.0.1:8100/mcp", flush=True)
    mcp.run(transport="streamable-http")

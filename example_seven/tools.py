import anthropic
from crewai.mcp.config import MCPServerStdio
from crewai.tools import tool


@tool
def search_web(query: str) -> str:
    """Search the web for the given query and return a summary of findings."""
    response = anthropic.Anthropic().messages.create(
        model="claude-haiku-4-5",
        max_tokens=2048,
        tools=[{"type": "web_search_20250305", "name": "web_search", "max_uses": 3}],
        messages=[
            {"role": "user", "content": f"Search the web and summarize: {query}"}
        ],
    )
    return "".join(block.text for block in response.content if hasattr(block, "text"))


TIME_MCP = MCPServerStdio(command="uvx", args=["mcp-server-time"])

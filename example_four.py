import asyncio

import anthropic
from crewai import LLM
from crewai.flow.flow import Flow, listen, start
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from pydantic import BaseModel

from utils import read_brief, write_response

llm = LLM(model="anthropic/claude-sonnet-4-6")


def search_web(query: str) -> str:
    response = anthropic.Anthropic().messages.create(
        model="claude-haiku-4-5",
        max_tokens=2048,
        tools=[{"type": "web_search_20250305", "name": "web_search", "max_uses": 3}],
        messages=[{"role": "user", "content": f"Search the web and summarize: {query}"}],
    )
    return "".join(block.text for block in response.content if hasattr(block, "text"))


async def _mcp_get_time() -> str:
    params = StdioServerParameters(command="uvx", args=["mcp-server-time"])
    async with stdio_client(params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            result = await session.call_tool("get_current_time", {"timezone": "UTC"})
            return result.content[0].text


def now_via_mcp() -> str:
    return asyncio.run(_mcp_get_time())


class State(BaseModel):
    name: str = ""
    brief: str = ""
    agency: str = ""
    research: str = ""
    draft: str = ""


class RFPFlow(Flow[State]):
    @start()
    def research_agency(self):
        agency = llm.call(f"""
            From this RFP brief, identify the issuing agency.
            Reply with only the agency name, nothing else.

            {self.state.brief}
        """).strip()
        self.state.agency = search_web(
            f"{agency} priorities, recent procurements, strategic goals"
        )
        write_response(f"example_four-{self.state.name}-agency", self.state.agency)

    @listen(research_agency)
    def research(self):
        self.state.research = llm.call(f"""
            Extract requirements, evaluation criteria, and risks from this RFP:

            {self.state.brief}
        """)
        write_response(f"example_four-{self.state.name}-research", self.state.research)

    @listen(research)
    def write(self):
        self.state.draft = llm.call(f"""
            Draft a one-page Markdown proposal for this RFP, factoring in
            what we learned about the agency. Mark the top of the proposal
            with "Generated: {now_via_mcp()}".

            RFP brief:
            {self.state.brief}

            Requirements & criteria:
            {self.state.research}

            About the agency:
            {self.state.agency}
        """)


if __name__ == "__main__":
    name, brief = read_brief()
    flow = RFPFlow()
    flow.kickoff(inputs={"name": name, "brief": brief})
    output = write_response(f"example_four-{name}", flow.state.draft)
    print(f"\nWrote {output}")

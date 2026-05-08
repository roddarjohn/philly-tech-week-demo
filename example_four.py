"""Introduces a custom tool + MCP; introduces full subagents."""

import anthropic
from crewai import LLM, Agent, Crew, Task
from crewai.flow.flow import Flow, listen, start
from crewai.mcp.config import MCPServerStdio
from crewai.tools import tool
from pydantic import BaseModel

from utils import read_brief, read_company, write_response

llm = LLM(model="anthropic/claude-sonnet-4-6")


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


class State(BaseModel):
    name: str = ""
    brief: str = ""
    company: str = ""
    agency: str = ""
    research: str = ""
    draft: str = ""


class RFPFlow(Flow[State]):
    @start()
    def research_agency(self):
        # Agent (not a plain llm.call) so the LLM itself decides when to
        # invoke the search tool mid-draft.
        agent = Agent(
            role="Agency Researcher",
            goal="Identify the issuing agency from the RFP and research them",
            backstory="An analyst skilled at desk research on public agencies.",
            tools=[search_web],
            llm=llm,
            verbose=True,
        )
        task = Task(
            description=f"""
                Identify the agency that issued this RFP brief, then use
                the search tool to find recent priorities, similar
                procurements, and other context useful to a bidder:

                {self.state.brief}
            """,
            expected_output="A summary of the agency and helpful context.",
            agent=agent,
        )
        self.state.agency = str(Crew(agents=[agent], tasks=[task]).kickoff())
        write_response("example_four", f"{self.state.name}-agency", self.state.agency)

    @listen(research_agency)
    def research(self):
        self.state.research = llm.call(f"""
            Extract requirements, evaluation criteria, and risks from this RFP:

            {self.state.brief}
        """)
        write_response("example_four", f"{self.state.name}-research", self.state.research)

    @listen(research)
    def write(self):
        # Agent (not a plain llm.call) so the LLM itself decides when to
        # invoke the MCP tool mid-draft.
        agent = Agent(
            role="Proposal Writer",
            goal="Draft proposals with an accurate generation timestamp",
            backstory="A proposal writer who calls the time MCP for every draft.",
            mcps=[MCPServerStdio(command="uvx", args=["mcp-server-time"])],
            llm=llm,
            verbose=True,
        )
        task = Task(
            description=f"""
                Call the time MCP to get the current UTC time, then draft a
                one-page Markdown proposal for this RFP from our company's
                perspective. Mark the top of the proposal with "Generated:
                <UTC time>".

                RFP brief:
                {self.state.brief}

                Requirements & criteria:
                {self.state.research}

                About the agency:
                {self.state.agency}

                Our company:
                {self.state.company}
            """,
            expected_output="A one-page proposal in Markdown with a timestamp at the top.",
            agent=agent,
        )
        self.state.draft = str(Crew(agents=[agent], tasks=[task]).kickoff())


if __name__ == "__main__":
    name, brief = read_brief()
    flow = RFPFlow()
    flow.kickoff(inputs={"name": name, "brief": brief, "company": read_company()})
    output = write_response("example_four", name, flow.state.draft)
    print(f"\nWrote {output}")

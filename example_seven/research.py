from crewai import Agent, Crew, Task
from crewai.flow.flow import Flow, listen, start
from pydantic import BaseModel

from example_seven.llms import claude
from example_seven.tools import search_web


class State(BaseModel):
    brief: str = ""
    agency: str = ""
    requirements: str = ""


class ResearchFlow(Flow[State]):
    @start()
    def agency(self):
        # Agent — let the LLM decide when to invoke the search tool.
        agent = Agent(
            role="Agency Researcher",
            goal="Identify the issuing agency and gather context about them",
            backstory="An analyst skilled at desk research on public agencies.",
            tools=[search_web],
            llm=claude,
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

    @listen(agency)
    def requirements(self):
        self.state.requirements = claude.call(f"""
            Extract requirements, evaluation criteria, and risks from this RFP:

            {self.state.brief}
        """)

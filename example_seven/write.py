from crewai import Agent, Crew, Task
from crewai.flow.flow import Flow, and_, listen, start
from pydantic import BaseModel

from example_seven.llms import claude, openai
from example_seven.tools import TIME_MCP


class State(BaseModel):
    brief: str = ""
    company: str = ""
    agency: str = ""
    requirements: str = ""
    summary: str = ""
    approach: str = ""
    pricing: str = ""
    assembled: str = ""
    draft: str = ""


class WriteFlow(Flow[State]):
    @start()
    def begin(self):
        pass

    @listen(begin)
    def write_summary(self):
        self.state.summary = claude.call(f"""
            Write a 2-paragraph executive summary, from our company's
            perspective.

            Requirements: {self.state.requirements}
            About the agency: {self.state.agency}
            Our company: {self.state.company}
        """)

    @listen(begin)
    def write_approach(self):
        self.state.approach = claude.call(f"""
            Write a technical approach section, from our company's
            perspective.

            Requirements: {self.state.requirements}
            About the agency: {self.state.agency}
            Our company: {self.state.company}
        """)

    @listen(begin)
    def write_pricing(self):
        self.state.pricing = claude.call(f"""
            Write a pricing section, from our company's perspective.

            Requirements: {self.state.requirements}
            About the agency: {self.state.agency}
            Our company: {self.state.company}
        """)

    @listen(and_(write_summary, write_approach, write_pricing))
    def assemble(self):
        # Agent — let the LLM call the time MCP itself for the timestamp.
        agent = Agent(
            role="Proposal Assembler",
            goal="Combine sections into one proposal with a generation timestamp",
            backstory="A writer who timestamps every draft via MCP.",
            mcps=[TIME_MCP],
            llm=claude,
            verbose=True,
        )
        task = Task(
            description=f"""
                Call the time MCP, then assemble these sections into one
                Markdown proposal. Mark the top with "Generated: <UTC time>".

                Executive summary:
                {self.state.summary}

                Technical approach:
                {self.state.approach}

                Pricing:
                {self.state.pricing}
            """,
            expected_output="A Markdown proposal with a UTC timestamp at the top.",
            agent=agent,
        )
        self.state.assembled = str(Crew(agents=[agent], tasks=[task]).kickoff())

    @listen(assemble)
    def polish(self):
        # Different provider for the polish pass (example one's pattern).
        self.state.draft = openai.call(f"""
            Polish this proposal for clarity, completeness, and tone.
            Return the final Markdown:

            {self.state.assembled}
        """)

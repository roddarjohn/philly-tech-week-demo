from crewai import LLM
from crewai.flow.flow import Flow, and_, listen, start
from pydantic import BaseModel

from utils import read_brief, write_response

llm = LLM(model="anthropic/claude-sonnet-4-6")


class State(BaseModel):
    brief: str = ""
    research: str = ""
    summary: str = ""
    approach: str = ""
    pricing: str = ""
    draft: str = ""


class RFPFlow(Flow[State]):
    @start()
    def research(self):
        self.state.research = llm.call(f"""
            Extract requirements from this RFP brief:

            {self.state.brief}
        """)

    @listen(research)
    def write_summary(self):
        self.state.summary = llm.call(f"""
            Write a 2-paragraph executive summary for this RFP:

            {self.state.research}
        """)

    @listen(research)
    def write_approach(self):
        self.state.approach = llm.call(f"""
            Write a technical approach section for this RFP:

            {self.state.research}
        """)

    @listen(research)
    def write_pricing(self):
        self.state.pricing = llm.call(f"""
            Write a pricing section for this RFP:

            {self.state.research}
        """)

    @listen(and_(write_summary, write_approach, write_pricing))
    def assemble(self):
        self.state.draft = (
            f"# Executive Summary\n\n{self.state.summary}\n\n"
            f"# Technical Approach\n\n{self.state.approach}\n\n"
            f"# Pricing\n\n{self.state.pricing}\n"
        )


if __name__ == "__main__":
    name, brief = read_brief()
    flow = RFPFlow()
    flow.kickoff(inputs={"brief": brief})
    output = write_response(f"example_five-{name}", flow.state.draft)
    print(f"\nWrote {output}")

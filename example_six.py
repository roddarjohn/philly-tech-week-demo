"""Composability."""

from crewai import LLM
from crewai.flow.flow import Flow, listen, start

from utils import read_brief, read_company, write_response

llm = LLM(model="anthropic/claude-sonnet-4-6")


class ResearchFlow(Flow):
    @start()
    def extract(self):
        return llm.call(f"""
            Extract requirements and evaluation criteria from this brief:

            {self.state['brief']}
        """)


class WriteFlow(Flow):
    @start()
    def draft(self):
        return llm.call(f"""
            Draft a one-page Markdown proposal from our company's perspective.

            Research:
            {self.state['research']}

            Our company:
            {self.state['company']}
        """)


class RFPFlow(Flow):
    @start()
    def research(self):
        return str(ResearchFlow().kickoff(inputs={"brief": self.state["brief"]}))

    @listen(research)
    def write(self, research):
        return str(WriteFlow().kickoff(inputs={
            "research": research,
            "company": self.state["company"],
        }))


if __name__ == "__main__":
    name, brief = read_brief()
    result = RFPFlow().kickoff(inputs={"brief": brief, "company": read_company()})
    output = write_response("example_six", name, str(result))
    print(f"\nWrote {output}")

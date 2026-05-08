"""Introduces a review flow."""

from crewai import LLM
from crewai.flow.flow import Flow, listen, or_, router, start
from pydantic import BaseModel

from utils import read_brief, read_company, write_response

llm = LLM(model="anthropic/claude-sonnet-4-6")
MAX_REVISIONS = 2


class State(BaseModel):
    brief: str = ""
    company: str = ""
    research: str = ""
    draft: str = ""
    feedback: str = ""
    iteration: int = 0


class RFPFlow(Flow[State]):
    @start()
    def research(self):
        self.state.research = llm.call(f"""
            Extract requirements, evaluation criteria, and risks
            from this RFP brief:

            {self.state.brief}
        """)

    @listen(research)
    def write(self):
        self.state.draft = llm.call(f"""
            Draft a one-page Markdown proposal that addresses every
            requirement, written from our company's perspective.

            Research:
            {self.state.research}

            Our company:
            {self.state.company}
        """)

    @listen("revise")
    def rewrite(self):
        self.state.iteration += 1
        self.state.draft = llm.call(f"""
            Revise this proposal based on the reviewer's feedback.

            Current draft:
            {self.state.draft}

            Reviewer feedback:
            {self.state.feedback}
        """)

    @router(or_(write, rewrite))
    def review(self):
        verdict = llm.call(f"""
            Review this proposal. Reply with DONE or list revisions:

            {self.state.draft}
        """)
        if "DONE" in verdict or self.state.iteration >= MAX_REVISIONS:
            return "done"
        self.state.feedback = verdict
        return "revise"


if __name__ == "__main__":
    name, brief = read_brief()
    flow = RFPFlow()
    flow.kickoff(inputs={"brief": brief, "company": read_company()})
    output = write_response("example_two", name, flow.state.draft)
    print(f"\nWrote {output}")

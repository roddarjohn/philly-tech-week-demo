from crewai import LLM
from crewai.flow.flow import Flow, listen, or_, start
from crewai.flow.human_feedback import human_feedback
from pydantic import BaseModel

from utils import read_brief, read_company, write_response

llm = LLM(model="anthropic/claude-sonnet-4-6")


class State(BaseModel):
    brief: str = ""
    company: str = ""
    research: str = ""
    draft: str = ""


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

    @listen(or_(write, "apply_revisions"))
    @human_feedback(
        message="Review the draft above. Approve or describe revisions:",
        emit=["done", "revise"],
        llm="anthropic/claude-haiku-4-5",
    )
    def review(self):
        return self.state.draft

    @listen("revise")
    def apply_revisions(self):
        self.state.draft = llm.call(f"""
            Revise this proposal based on the reviewer's feedback.

            Current draft:
            {self.state.draft}

            Reviewer feedback:
            {self.last_human_feedback.feedback}
        """)


if __name__ == "__main__":
    name, brief = read_brief()
    flow = RFPFlow()
    flow.kickoff(inputs={"brief": brief, "company": read_company()})
    output = write_response("example_three", name, flow.state.draft)
    print(f"\nWrote {output}")

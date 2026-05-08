from crewai.flow.flow import Flow, listen, or_, start
from crewai.flow.human_feedback import human_feedback
from pydantic import BaseModel

from example_seven.llms import claude


class State(BaseModel):
    draft: str = ""


class ReviewFlow(Flow[State]):
    @start()
    def begin(self):
        pass

    @listen(or_(begin, "apply_revisions"))
    @human_feedback(
        message="Review the draft above. Approve or describe revisions:",
        emit=["approve", "revise"],
        llm="anthropic/claude-haiku-4-5",
    )
    def review(self):
        return self.state.draft

    @listen("revise")
    def apply_revisions(self):
        self.state.draft = claude.call(f"""
            Revise this proposal based on the reviewer's feedback.

            Current draft:
            {self.state.draft}

            Reviewer feedback:
            {self.last_human_feedback.feedback}
        """)

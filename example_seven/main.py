from crewai.flow.flow import Flow, listen, start
from pydantic import BaseModel

from example_seven.research import ResearchFlow
from example_seven.review import ReviewFlow
from example_seven.write import WriteFlow


class State(BaseModel):
    name: str = ""
    brief: str = ""
    company: str = ""
    agency: str = ""
    requirements: str = ""
    draft: str = ""


class RFPFlow(Flow[State]):
    @start()
    def research(self):
        sub = ResearchFlow()
        sub.kickoff(inputs={"brief": self.state.brief})
        self.state.agency = sub.state.agency
        self.state.requirements = sub.state.requirements

    @listen(research)
    def write(self):
        sub = WriteFlow()
        sub.kickoff(inputs={
            "brief": self.state.brief,
            "company": self.state.company,
            "agency": self.state.agency,
            "requirements": self.state.requirements,
        })
        self.state.draft = sub.state.draft

    @listen(write)
    def review(self):
        sub = ReviewFlow()
        sub.kickoff(inputs={"draft": self.state.draft})
        self.state.draft = sub.state.draft

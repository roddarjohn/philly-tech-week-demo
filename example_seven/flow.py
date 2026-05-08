from crewai import Crew, Task
from crewai.flow.flow import Flow, and_, listen, or_, start
from crewai.flow.human_feedback import human_feedback

from example_seven import prompts
from example_seven.agents import agency_researcher
from example_seven.llms import claude, openai
from example_seven.state import State
from utils import write_response


class RFPFlow(Flow[State]):
    def _persist(self, step: str, content: str) -> None:
        write_response(f"example_seven-{self.state.name}-{step}", content)

    @start()
    def research_agency(self):
        agent = agency_researcher()
        task = Task(
            description=prompts.research_brief(self.state.brief),
            expected_output="A summary of the agency and helpful context.",
            agent=agent,
        )
        self.state.agency = str(Crew(agents=[agent], tasks=[task]).kickoff())
        self._persist("agency", self.state.agency)

    @start()
    def extract_requirements(self):
        self.state.requirements = claude.call(
            prompts.extract_requirements(self.state.brief)
        )
        self._persist("requirements", self.state.requirements)

    @listen(and_(research_agency, extract_requirements))
    def write_summary(self):
        self.state.summary = claude.call(
            prompts.section(
                "executive summary",
                self.state.requirements,
                self.state.agency,
                self.state.company,
            )
        )
        self._persist("summary", self.state.summary)

    @listen(and_(research_agency, extract_requirements))
    def write_approach(self):
        self.state.approach = claude.call(
            prompts.section(
                "technical approach",
                self.state.requirements,
                self.state.agency,
                self.state.company,
            )
        )
        self._persist("approach", self.state.approach)

    @listen(and_(research_agency, extract_requirements))
    def write_qualifications(self):
        self.state.qualifications = claude.call(
            prompts.section(
                "qualifications and past performance",
                self.state.requirements,
                self.state.agency,
                self.state.company,
            )
        )
        self._persist("qualifications", self.state.qualifications)

    @listen(and_(write_summary, write_approach, write_qualifications))
    def assemble(self):
        self.state.assembled = (
            f"# Executive Summary\n\n{self.state.summary}\n\n"
            f"# Technical Approach\n\n{self.state.approach}\n\n"
            f"# Qualifications\n\n{self.state.qualifications}\n"
        )
        self._persist("assembled", self.state.assembled)

    @listen(assemble)
    def polish(self):
        self.state.draft = openai.call(prompts.polish(self.state.assembled))
        self._persist("polished", self.state.draft)

    @listen(or_(polish, "apply_revisions"))
    @human_feedback(
        message="Review the draft above. Approve or describe revisions:",
        emit=["approve", "revise"],
        llm="anthropic/claude-haiku-4-5",
    )
    def review(self):
        return self.state.draft

    @listen("revise")
    def apply_revisions(self):
        self.state.draft = claude.call(
            prompts.revise(self.state.draft, self.last_human_feedback.feedback)
        )
        self._persist("revised", self.state.draft)

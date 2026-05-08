from crewai import LLM
from crewai.flow.flow import Flow, listen, start

from utils import read_brief, read_company, write_response

claude = LLM(model="anthropic/claude-sonnet-4-6")
openai = LLM(model="openai/gpt-4o-mini")


class RFPFlow(Flow):
    @start()
    def research(self):
        return claude.call(f"""
            Extract requirements, evaluation criteria, and risks
            from this RFP brief:

            {self.state["brief"]}
        """)

    @listen(research)
    def draft(self, research):
        return claude.call(f"""
            Draft a one-page Markdown proposal that addresses every
            requirement, written from our company's perspective.

            Research:
            {research}

            Our company:
            {self.state["company"]}
        """)

    @listen(draft)
    def review(self, draft):
        return openai.call(f"""
            Polish this draft for clarity, completeness, and tone.
            Return the final Markdown:

            {draft}
        """)


if __name__ == "__main__":
    name, brief = read_brief()
    result = RFPFlow().kickoff(inputs={"brief": brief, "company": read_company()})

    output = write_response("example_one", name, str(result))
    print(f"\nWrote {output}")

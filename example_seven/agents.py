from crewai import Agent

from example_seven.llms import claude
from example_seven.tools import search_web


def agency_researcher() -> Agent:
    return Agent(
        role="Agency Researcher",
        goal="Identify the issuing agency and gather context about them",
        backstory="An analyst skilled at desk research on public agencies.",
        tools=[search_web],
        llm=claude,
        verbose=True,
    )

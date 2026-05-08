def research_brief(brief: str) -> str:
    return f"""
        Identify the agency that issued this RFP brief, then use the search
        tool to find recent priorities, similar procurements, and other
        context useful to a bidder:

        {brief}
    """


def extract_requirements(brief: str) -> str:
    return f"""
        Extract requirements, evaluation criteria, and risks from this RFP:

        {brief}
    """


def section(name: str, requirements: str, agency: str, company: str) -> str:
    return f"""
        Write the {name} section of an RFP response, from our company's
        perspective. Markdown only.

        Requirements: {requirements}
        About the agency: {agency}
        Our company: {company}
    """


def polish(draft: str) -> str:
    return f"""
        These sections were drafted in parallel. Polish them into a single
        proposal with a consistent voice and tone. Return final Markdown:

        {draft}
    """


def revise(draft: str, feedback: str) -> str:
    return f"""
        Revise this proposal based on the reviewer's feedback.

        Current draft:
        {draft}

        Reviewer feedback:
        {feedback}
    """

from pydantic import BaseModel


class State(BaseModel):
    name: str = ""
    brief: str = ""
    company: str = ""
    agency: str = ""
    requirements: str = ""
    summary: str = ""
    approach: str = ""
    qualifications: str = ""
    assembled: str = ""
    draft: str = ""

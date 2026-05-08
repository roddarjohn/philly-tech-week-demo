import re
import sys
from pathlib import Path

from pypdf import PdfReader

_FENCE = re.compile(r"\A```(?:markdown|md)?\s*\n(.*)\n```\s*\Z", re.DOTALL)

DEFAULT_BRIEF_DIR = Path(__file__).parent / "briefs" / "philly-portal"
COMPANY_FILE = Path(__file__).parent / "briefs" / "company.md"


def read_brief() -> tuple[str, str]:
    directory = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_BRIEF_DIR
    pdfs = list(directory.glob("*.pdf"))
    if pdfs:
        text = "\n".join(p.extract_text() for p in PdfReader(pdfs[0]).pages)
        return directory.name, text
    return directory.name, (directory / "brief.md").read_text()


def read_company() -> str:
    return COMPANY_FILE.read_text()


def write_response(example: str, name: str, content: str) -> Path:
    path = Path("responses") / example / f"{name}.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    if match := _FENCE.match(content.strip()):
        content = match.group(1)
    path.write_text(content)
    return path

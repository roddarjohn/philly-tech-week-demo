import sys
from pathlib import Path

DEFAULT_BRIEF_DIR = Path(__file__).parent / "briefs" / "philly-portal"


def read_brief() -> tuple[str, str]:
    directory = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_BRIEF_DIR
    return directory.name, (directory / "brief.md").read_text()


def write_response(name: str, content: str) -> Path:
    path = Path("responses") / f"{name}.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content)
    return path

import importlib
import importlib.util
import inspect
import shutil
import webbrowser
from pathlib import Path
from typing import Annotated

import typer
from crewai.flow.flow import Flow
from rich.console import Console

console = Console()


def load_flow(target: Path) -> type[Flow]:
    if target.is_file():
        spec = importlib.util.spec_from_file_location(target.stem, target)
        if spec is None or spec.loader is None:
            raise typer.Exit(code=1)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
    else:
        module = importlib.import_module(target.stem)

    candidates = [
        obj
        for _, obj in inspect.getmembers(module, inspect.isclass)
        if issubclass(obj, Flow)
        and obj is not Flow
        and obj.__module__.startswith(module.__name__)
    ]
    if not candidates:
        console.print(f"[red]No Flow subclass found in {target}[/red]")
        raise typer.Exit(code=1)
    rfp = [c for c in candidates if c.__name__ == "RFPFlow"]
    return rfp[0] if rfp else candidates[0]


def main(file: Annotated[Path, typer.Argument()] = Path("example_one.py")) -> None:
    """Render the flow graph from FILE to dist/<stem>.html."""
    out = Path("dist")
    out.mkdir(parents=True, exist_ok=True)
    with console.status(f"[cyan]Rendering flow from {file}...", spinner="dots"):
        flow_cls = load_flow(file)
        src = Path(flow_cls().plot(f"{file.stem}.html", show=False))
        for f in src.parent.iterdir():
            shutil.copy(f, out / f.name)
    output = (out / src.name).absolute()
    console.print(f"[green]Wrote {output}[/green]")
    webbrowser.open(output.as_uri())


if __name__ == "__main__":
    typer.run(main)

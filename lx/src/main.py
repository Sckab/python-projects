from pathlib import Path
from typing import Annotated
from rich import print as rprint

import typer

from utility import ls

app = typer.Typer(rich_markup_mode=None)


@app.command()
def main(
    dir: Annotated[
        Path,
        typer.Argument(
            help="The directory to list items from. Defaults to the current working directory.",
            show_default=False,
        ),
    ] = Path.cwd(),
    no_colors: Annotated[
        bool, typer.Option("--no-colors", "-n", help="Disable the colors.")
    ] = False,
):
    if not dir.exists():
        if no_colors:
            rprint(f"The directory [bold]{dir}/[/] doesn't exists")
        else:
            rprint(f"[red]The directory[/] {dir}/ [red]doesn't exists[/]")
        return

    ls.ls(dir, no_colors)


if __name__ == "__main__":
    app()

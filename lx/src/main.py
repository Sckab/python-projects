from pathlib import Path
from typing import Annotated

import typer
from rich import print as rprint

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
    """
    An ls with the X factor
    """

    if not dir.exists():
        if no_colors:
            rprint(f"The directory [bold]{dir}/[/] doesn't exists")
        else:
            rprint(f"[red]The directory[/] {dir}/ [red]doesn't exists[/]")

        raise typer.Exit()

    ls.ls(dir, no_colors)


if __name__ == "__main__":
    app()

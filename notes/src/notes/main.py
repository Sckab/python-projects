from typing import Annotated

import typer

import notes
from notes.cli import app as cli_app
from notes.gui import main_window

app = typer.Typer(
    help="Note taker",
    suggest_commands=True,
)

app.add_typer(cli_app)


@app.callback(invoke_without_command=True)
def main(
    ctx: typer.Context,
    version: Annotated[
        bool,
        typer.Option(
            "--version", "-v", help="Displays the program version and then exits."
        ),
    ] = False,
) -> None:
    if version:
        print(f"Notes {notes.__version__}")
    elif ctx.invoked_subcommand is None:
        raise typer.Exit(main_window.run())

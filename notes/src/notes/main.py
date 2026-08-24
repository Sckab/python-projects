from typing import Annotated

import typer

import notes

app = typer.Typer(
    help="Note taker",
    suggest_commands=True,
)


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
        print("GUI")

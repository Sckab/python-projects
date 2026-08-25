from typing import Annotated

import typer

app = typer.Typer()


@app.command()
def add(
    name: Annotated[str, typer.Option("--name", "-n", help="The name of the note")],
    desc: Annotated[
        str, typer.Option("--desc", "-d", help="The description of the note")
    ],
):
    # TODO: implement actual adding features

    ...

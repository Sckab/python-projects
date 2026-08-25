from typing import Annotated

import typer

app = typer.Typer()


@app.command()
def remove(
    id: Annotated[int, typer.Argument(help="The id of the note")],
):
    # TODO: implement actual removing features

    ...

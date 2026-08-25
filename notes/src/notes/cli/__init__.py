import typer

from notes.cli.add import app as add_app
from notes.cli.remove import app as remove_app

app = typer.Typer()

app.add_typer(add_app)
app.add_typer(remove_app)

from rich import print as Print
from rich.panel import Panel


def main() -> None:
    Print(
        Panel.fit(
            "[bold green]Calculator[/bold green] is running!",
            title="CALCULATOR",
            subtitle="v1.0.0",
        )
    )

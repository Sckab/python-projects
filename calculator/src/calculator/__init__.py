from rich import print as Print
from rich.panel import Panel
from rich.prompt import FloatPrompt


def main() -> None:
    Print(
        Panel.fit(
            "[white]This is a simple calculator application.[/white]",
            title="CALCULATOR",
            subtitle="v1.0.0",
            title_align="left",
            subtitle_align="left",
            style="green",
        )
    )

    firstNumber = FloatPrompt.ask(
        "[green]Enter the first number[/green]",
        default="0.0",
        case_sensitive=False,
    )

    secondNumber = FloatPrompt.ask(
        "[green]Enter the second number[/green]",
        default="0.0",
        case_sensitive=False,
    )

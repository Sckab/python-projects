from rich import print as Print
from rich.panel import Panel
from rich.prompt import FloatPrompt, Prompt
from rich.rule import Rule


def askNumbers():
    global firstNumber, secondNumber

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


def operations():
    operation = Prompt.ask(
        "[green]What operation do you want to do?[/green]",
        choices=["+", "-", "*", "/"],
        default="+",
        case_sensitive=False,
    )

    while True:
        match operation:
            case "+":
                Print(
                    f"[bold green]Result:[/bold green] {firstNumber} + {secondNumber} = {firstNumber + secondNumber}"
                )
                break

            case "-":
                Print(
                    f"[bold green]Result:[/bold green] {firstNumber} - {secondNumber} = {firstNumber - secondNumber}"
                )
                break

            case "*":
                Print(
                    f"[bold green]Result:[/bold green] {firstNumber} * {secondNumber} {firstNumber * secondNumber}"
                )
                break

            case "/":
                if secondNumber == 0:
                    print("You can't divide a number by 0")
                    break

                Print(
                    f"[bold green]Result:[/bold green] {firstNumber} / {secondNumber} {firstNumber / secondNumber}"
                )
                break

            case _:
                print("Invalid input")


def calculator():
    while True:
        Print(Rule(title="[bold green]INSERT THE NUMBERS[/bold green]"))

        askNumbers()

        Print(Rule(title="[bold green]SELECT THE OPERATION[/bold green]"))

        operations()

        want_continue = Prompt.ask(
            "[green]Do you want to continue?[/green]",
            choices=["yes", "no", "n", "y"],
            default="n",
            case_sensitive=False,
        )

        if want_continue == "n" or want_continue == "no":
            break


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

    calculator()

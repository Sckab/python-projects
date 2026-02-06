from pathlib import Path
from rich import print as rprint


def ls(directory: Path = Path.cwd(), no_colors: bool = False):
    files = list(Path.iterdir(directory))
    files.sort(key=lambda i: (not i.is_dir(), i.name.lower()))

    for item in files:
        if item.is_dir():
            if no_colors:
                rprint(f"[bold]{item.name}/[/]", end="  ")
            else:
                rprint(f"[bold green]{item.name}/[/]", end="  ")
        else:
            print(item.name, end="  ")

    print()


if __name__ == "__main__":
    ls()

from dataclasses import dataclass

import click
import click_pathlib
from bs4 import BeautifulSoup
from rich.console import Console
from rich.markup import escape


console = Console()


@dataclass
class Creator:
    name: str
    description: str
    src: str


@click.command
@click.option(
    "--creators-filename",
    default="creators.html",
    type=click_pathlib.Path(exists=True),
)
def click_main(creators_filename):
    with creators_filename.open() as f:
        soup = BeautifulSoup(f, 'html.parser')

    avatars = soup.select("img.avatar")
    console.print(f"There are currently {len(avatars)} creators on Nebula:")
    console.print()

    creators = []
    for avatar in avatars:
        name, _, description = avatar["alt"].partition("–")
        name = name.strip()
        description = description.strip()
        creators.append(Creator(name, description, avatar["src"]))

    for creator in sorted(creators, key=lambda v: v.name.lower()):
        console.print(f"[bold magenta]{escape(creator.name)}[/bold magenta]")
        console.print(creator.description, highlight=False)
        console.print()


if __name__ == "__main__":
    click_main()

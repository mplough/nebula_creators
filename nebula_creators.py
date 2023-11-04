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
    image_url: str
    nebula_url: str
    other_urls: list[str]


def make_creator(creator_element) -> Creator:
    link_element = creator_element.select("h3")[0].select("a")[0]

    name = link_element.text.strip()
    description = creator_element.select("p")[0].text.strip()
    image_url = None  #avatar["src"]
    nebula_url = link_element["href"]
    other_urls = [a["href"] for a in creator_element.select("a.link")]

    return Creator(
        name=name,
        description=description,
        image_url=image_url,
        nebula_url=nebula_url,
        other_urls=other_urls,
    )


def print_creator(creator):
    console.print(f"[bold magenta]{escape(creator.name)}")
    console.print(f"[green]{creator.nebula_url}")
    console.print(creator.description, highlight=False)
    for url in creator.other_urls:
        console.print(f"   - [blue]{url}")
    console.print()


def title_sort_key(s: str) -> str:
    return s.lower().removeprefix("the ")


@click.command
@click.option(
    "--creators-filename",
    default="creators.html",
    type=click_pathlib.Path(exists=True),
)
def click_main(creators_filename):
    with creators_filename.open() as f:
        soup = BeautifulSoup(f, 'html.parser')

    video_creator_trees = soup.select("div.grid-item.youtube-creator")
    video_creators = [make_creator(c) for c in video_creator_trees]

    podcast_creator_trees = soup.select("div.grid-item.podcast-creator")
    podcast_creators = [make_creator(c) for c in podcast_creator_trees]

    console.print(f"There are currently {len(video_creators)} video creators on Nebula.")
    console.print()

    console.print(f"There are currently {len(podcast_creators)} podcast creators on Nebula:")
    console.print()

    console.print(f"[bold red]Video creators")
    console.print(f"[bold red]" + 80 * "-" + "\n")

    for creator in sorted(video_creators, key=lambda v: title_sort_key(v.name)):
        print_creator(creator)

    console.print("\n\n")
    console.print(f"[bold red]Podcast creators")
    console.print(f"[bold red]" + 80 * "-" + "\n")

    for creator in sorted(podcast_creators, key=lambda v: title_sort_key(v.name)):
        print_creator(creator)


if __name__ == "__main__":
    click_main()

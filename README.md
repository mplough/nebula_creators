# nebula creators

List creators on Nebula.

The [Nebula creators page](https://talent.nebula.tv/creators/) is a grid of
icons that's not searchable.  This tool prints names and descriptions of the
creators so you can actually use basic tools like Ctrl+F to see what you might
want to check out.

# Use

## Setup

This tool is written as a script that can be [run with uv](https://docs.astral.sh/uv/guides/scripts/).

1. Install `uv`

# Use

Download Nebula's creators page, then run the script.

```bash
curl https://talent.nebula.tv/creators/ >creators.html
uv run nebula_creators.py
```

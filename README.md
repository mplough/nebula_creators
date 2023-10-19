# nebula creators

List creators on Nebula.

The [Nebula creators page](https://talent.nebula.tv/creators/) is a grid of
icons that's not searchable.  This tool prints names and descriptions of the
creators so you can actually use basic tools like Ctrl+F to see what you might
want to check out.

# Use

## Setup

1. `pipenv install`
1. `pipenv shell`

# Use

Download Nebula's creators page, then run the script.

```bash
curl https://talent.nebula.tv/creators/ >creators.html
python nebula_creators.py
```

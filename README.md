# astrojobs
[![PyPI version](https://img.shields.io/pypi/v/astrojobs.svg)](https://pypi.python.org/pypi/astrojobs)

Tired of checking the AAS job register and astro rumor mill for job news?
Get the latest updates in the command line!

`astrojobs` automatically grabs the latest jobs from the 
AAS [Job Registry](https://jobregister.aas.org/) and news from the
Astrobetter [Rumor Mill](https://www.astrobetter.com/wiki/Rumor+Mill+Faculty-Staff)
and prints them right into the terminal.

`astrojobs` helps you save time by only showing you the updates since the last time you ran the command.


## Installation and Setup

### Install `astrojobs`

You can install `astrojobs` from PyPI

```bash
pip install astrojobs
```


## Usage

Simply run `astrojobs` in the command line to see its options.

To list new __faculty__ positions/updates, in your terminal type:
```bash
astrojobs -f
```

To list new __postdoc__ positions/updates, type:
```bash
astrojobs -p
```

_Internet connection is needed for `astrojobs` to work._


`astrojobs` will automatically show you the latest job postings and rumors since you last ran the command.

![astrojobs usage example](astrojobs.png)


## Notices

It is always your responsibility to check for job postings directly. 
This code will break if AAS or Astrobetter reformats their websites.

Information from the rumor mill may be not be accurate.

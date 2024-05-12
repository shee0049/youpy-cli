# youpy-cli
youpy-cli is a command line application written in python to provide a minimal command line interface for searching and playing youtube videos with [mpv](https://mpv.io/).  

youpy-cli utilizes a backend API built with [FastAPI](https://fastapi.tiangolo.com/) to scrape and query videos with [selenium](https://www.selenium.dev/) and return the query results as json back to the client.

This project was created for my own personal use.  But feel free to send a [pull request](https://github.com/shee0049/youpy-cli/pulls) if you would like to add new features.

[youpy-cli.webm](https://github.com/shee0049/youpy-cli/assets/9749577/a62e1932-9f2f-4cfc-a83e-63a127cae7cf)

### Installation

Donload required dependencies

```bash
pip install mpv-devel mpv-libs mpv yt-dlp fastapi[all] selenium rich
```

Clone this repository

```bash
git clone https://github.com/shee0049/youpy-cli/ && cd youpy-cli
``` 

Start API backend

```bash
uvicorn main:app --reload
```

In a new terminal navigate to youpy-cli repository and start the client

```bash
python3 client.py
```

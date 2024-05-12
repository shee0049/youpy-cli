# youpy-cli
youpy-cli is a command line application written in python to provide a minimal command line interface for searching and playing youtube videos with [mpv](https://mpv.io/).  The application integrates a backend API built with [FastAPI](https://fastapi.tiangolo.com/) to scrape and query videos with [selenium](https://www.selenium.dev/) and return the query results as json back to the client. 

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

### Optional: Build API backend with docker

Build image from Dockerfile

```bash
docker build -t youpy-srv .
```

Run a container off of the created build image

```bash
sudo docker run -itd -p 8000:8000 youpy-srv  
```

The API backend will now be available at 127.0.0.1:8000

### Client installation

In a new terminal navigate to youpy-cli repository and start the client

```bash
python3 client.py
```

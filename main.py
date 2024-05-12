from fastapi import FastAPI
import scrape as scr
import json

app = FastAPI()

@app.get("/")
def root():
    json = scr.scrape_videos()
    return json

@app.get("/channels/")
def read_channel(q: str | None = None): 
    if q:
        video_dict = scr.scrape_videos_by_channel(q)
        return video_dict
    else:
        return {"Error"}

@app.get("/videos/")
def read_video(q: str | None = None):
    if q:
        video_dict = scr.scrape_videos_by_query(q)
        return video_dict
    else:
        return {"Error"}

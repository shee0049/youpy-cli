import requests
import json
import os
import mpv
import sys
import datetime

from rich.console import Console
from rich.live import Live
from rich.columns import Columns
from rich.panel import Panel

prompt = "\033[5m> \033[0m "
API = 'http://127.0.0.1:8000'

def get_videos(search_type, query):
    if search_type == "channel":
        res = requests.get(API + '/channels/?q=' + query).json()
    else: 
        res = requests.get(API + '/videos/?q=' + query).json()
    return res

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def my_log(loglevel, component, message):
    print('[{}] {}: {}'.format(loglevel, component, message))

def print_menu():
    menu_ascii = """

    ╔═════════════════════════════════════════════════════════════╗
    ║                                                     __ _    ║
    ║    __  __ ____   __  __ ____   __  __        _____ / /(_)   ║
    ║   / / / // __ \ / / / // __ \ / / / /______ / ___// // /    ║ 
    ║  / /_/ // /_/ // /_/ // /_/ // /_/ //_____// /__ / // /     ║
    ║  \__, / \____/ \__,_// .___/ \__, /        \___//_//_/      ║ 
    ║ /____/              /_/     /____/                          ║ 
    ║                                                             ║
    ║                                                             ║
    ║ The command line youtube application!                       ║
    ╚═════════════════════════════════════════════════════════════╝
    \n"""
    console.print(menu_ascii, style="bold red")
    console.print("1. Search by video name\n2. Search by channel name\n")

def print_renderables(search_type):
 
    clear_screen()
    query = input("Query a video:" + prompt)
    clear_screen()
    console.print("[bold green]Fetching videos...") 
    video_dict = get_videos(search_type, query)
    clear_screen()

    if (search_type == "channel"):
        print("Channel - {} \n".format(video_dict["channelname"]))
   
    renderables = []
    for index, video in enumerate(video_dict['videos']): 
        renderables.append(Panel("[bold green]Video index: {}\n{}\n{}".format(index, video["title"], video["link"]))) 
    console.print(Columns(renderables))

    choice = int(input("Select video: " + prompt))
    
    clear_screen()
    console.print("[bold green] Now playing: {}\n".format( video_dict['videos'][choice]["title"]))

    try:
        player.play("{}".format(video_dict['videos'][choice]["link"]))
        player.wait_for_playback()
    except:
        print("Player error... closing")
    finally:
        player.terminate()
        print("This is the final block")

console = Console()
isAlive = True

while isAlive: 

    player = mpv.MPV(log_handler=my_log, ytdl=True, input_default_bindings=True, input_vo_keyboard=True)
    player.loop_playlist = 'inf'
    player['vo'] = 'gpu'

    @player.on_key_press('s')
    def my_s_binding():
        pillow_img = player.screenshot_raw()
        pillow_img.save('screenshot.png')

    @player.property_observer('time-pos')
    def time_observer(_name, value):
        print('Now playing at {:.2f}s'.format(value), end="\r")

    clear_screen()
    print_menu()

    menu_choice = input(prompt)

    match menu_choice: 
        case '1': 
            print_renderables("video")
        case '2':
            print_renderables("channel")
        case 'q':
            isAlive = False
            clear_screen()

del player

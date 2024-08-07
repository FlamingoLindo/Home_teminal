from tqdm import tqdm
from time import *
import psutil
import keyboard
from General import open_firefox_url

def open_all_links():
    all_urls = [
        "https://www.youtube.com/",
        "https://www.twitch.tv/",
        "https://twitter.com/home",
        "https://www.reddit.com/",
        "https://mail.google.com/mail/u/0/#inbox"
    ]

    for url in all_urls:
        print(f"Opening {url}...")
        open_firefox_url(url)
        
def percentage():
    with tqdm(total=100, desc='cpu%', position=0) as cpubar, tqdm(total=100, desc='ram%', position=2) as rambar, tqdm(desc='CPU cores', position=4) as cpucore:
        while True:
            rambar.n=psutil.virtual_memory().percent
            cpubar.n=psutil.cpu_percent()
            cpucore.n=psutil.cpu_count()
            rambar.refresh()
            cpubar.refresh()
            cpucore.refresh()
            sleep(0.5)

            if keyboard.is_pressed('esc'):
                print("\nCancelled by user.")
                return
        

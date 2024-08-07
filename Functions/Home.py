from tqdm import tqdm
import time
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
    with (
        tqdm(total=100, desc='cpu%', position=0, colour= 'green',) as cpubar, 
        tqdm(total=100, desc='ram%', position=2, colour= 'green') as rambar, 
        tqdm(desc='CPU cores', position=4,) as cpucore,
        tqdm(desc="Disk 1", position=6, colour='green') as disk1,
    ):
        while True:
            rambar.n=psutil.virtual_memory().percent

            cpubar.n=psutil.cpu_percent()

            cpucore.n=psutil.cpu_count()

            disk1.n=psutil.disk_usage('C:').percent

            rambar.refresh()

            cpubar.refresh()

            cpucore.refresh()

            time.sleep(1.5)

            if keyboard.is_pressed('esc'):
                print("\nCancelled by user.")
                return
        

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
    cpucol = 'green'
    ramcol = 'green'
    vcolor = 'green'
    ccolor = 'green'

    last_cpu_color = None
    last_ram_color = None
    last_v_color = None
    last_c_color = None

    while True:
        if last_cpu_color != cpucol:
            if last_cpu_color is not None:
                tqdm._instances.clear()  
            cpubar = tqdm(total=100, desc='cpu%', position=0, colour=cpucol, leave=False)
            last_cpu_color = cpucol
        
        if last_ram_color != ramcol:
            if last_ram_color is not None:
                tqdm._instances.clear()
            rambar = tqdm(total=100, desc='ram%', position=2, colour=ramcol, leave=False)
            last_ram_color = ramcol

        if last_v_color != vcolor:
            if last_v_color is not None:
                tqdm._instances.clear()
            vdisk = tqdm(total=100, desc='V', position=4, colour=vcolor, leave=False)
            last_v_color = vcolor

        if last_c_color != ccolor:
            if last_c_color is not None:
                tqdm._instances.clear()
            cdisk = tqdm(total=100, desc='C', position=5, colour=ccolor, leave=False)
            last_c_color = ccolor

    
        """download = tqdm(desc='Download', position=8, colour='green', leave=False)
        upload = tqdm(desc='Upload', position=9, colour='green', leave=False)"""

        rambar.n = psutil.virtual_memory().percent
        cpubar.n = psutil.cpu_percent() * 10
        vdisk.n = psutil.disk_usage('V:\\').percent
        cdisk.n = psutil.disk_usage('C:\\').percent
        
        """download.n = psutil.net_io_counters().bytes_recv
        upload.n = psutil.net_io_counters().bytes_sent"""

        rambar.refresh()
        cpubar.refresh()
        vdisk.refresh()
        cdisk.refresh()

        """download.refresh()
        upload.refresh()"""

        time.sleep(1.5)

        ramcol = 'green' if rambar.n < 50 else 'yellow' if rambar.n < 70 else 'red'
        cpucol = 'green' if cpubar.n < 50 else 'yellow' if cpubar.n < 70 else 'red'
        vcolor = 'green' if vdisk.n < 50 else 'yellow' if vdisk.n < 70 else 'red'
        ccolor = 'green' if cdisk.n < 50 else 'yellow' if cdisk.n < 70 else 'red'

        if keyboard.is_pressed('esc'):
            print("\nCancelled by user.")
            break

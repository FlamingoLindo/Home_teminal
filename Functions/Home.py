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
        

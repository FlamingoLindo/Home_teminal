from pytubefix import YouTube
from pytubefix.cli import on_progress
from General import clear_console
import time

def downloader():
    
    def download():
        if format == "1":
            print('Downloading: ', yt.title, 'as an MP4')
            ys = yt.streams.get_highest_resolution()
            ys.download(output_path='Terminal Downloads')
        elif format == "2":
            print('Downloading: ', yt.title, 'as an MP3')
            ys = yt.streams.get_audio_only()
            ys.download(filename=yt.title + ".mp3", output_path='Terminal Downloads')

    while True:
        url = input('Video URL: ')

        try:
            yt = YouTube(url, on_progress_callback=on_progress)
        except Exception as e:
            print('There has been an error with pytubefix!')
            print(e,'\n')
            continue

        clear_console()
        print('\n[1] Video \n[2] Audio')
        
        format = input('Choose the format: ')

        if format in ['1', '2']:
            try:
                download()
                break
            except Exception as e:
                print('There has been an error downloading your file!')
                print(e)
                continue
        else:
            print('\nWrong file format!')
            time.sleep(3)
            clear_console()

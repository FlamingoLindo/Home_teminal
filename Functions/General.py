import os
import platform

import time
from tqdm import trange
import subprocess
from datetime import date


def clear_console():
    """Clear the console based on the operating system."""
    os.system("cls" if platform.system() == "Windows" else "clear")

def open_url(url):
    """Open a URL in the default web browser"""
    try:
        os.system(f"start chrome {url}")
    except Exception as e:
        print(f"Failed to open URL {url}. Error: {e}")

def open_firefox_url(url):
    """Open a URL in the default web browser"""
    try:
        os.system(f"start firefox {url}")
    except Exception as e:
        print(f"Failed to open URL {url}. Error: {e}")


def day():
    today = date.today()

    date_weird = today.strftime("%d/%m/%Y")

    date_string = str(date_weird)

    a = date.weekday(today)

    if a == 0:
        week_day = "SEGUNDA"
    elif a == 1:
        week_day = "TERÇA"
    if a == 2:
        week_day = "QUARTA"
    elif a == 3:
        week_day = "QUINTA"
    if a == 4:
        week_day = "SEXTA"
    elif a == 5:
        week_day = "SABADO"
    elif a == 6:
        week_day = "DOMINGO"

    normal = f'{week_day : ^15} {date_string : ^15}'

    color_text =  u"\u001b[31;1m"f'{normal}'u'\u001b[0m'

    print(color_text)

def load_intro():

    intro =r"""

                                   

              _.....
          .-'` ^    `'.
        .'^   ^  ,_.   \
       // , ^ _.-'-.    |
      // /.--' '-       |
     /;/``--.___._      ;
     |/`    | /\ |`)   /
     `     //`  || |  /
          //    || | ;                      FLAMINGO'S USELESS
         ((     || | |                           TERMINAL
          `:.   || \ \
            ':. (|  `\\
              /;||    ||
              ||||    ;|
              |/||   /` |
                ||   \-p/
                ||   | |
              .~||~./_/
             `~ -  ~`


                """

    color_load = u"\u001b[35m"f'{intro}'
    print(color_load)
    for i in trange(100):
        time.sleep(0.02)
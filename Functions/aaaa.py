from tqdm import trange
import time

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

load_intro()
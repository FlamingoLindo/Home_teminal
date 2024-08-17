# FLAMINGO'S USELESS TERMINAL

This is a project made using python and different libraies that I'm developing for fun.

It started as me jsut trying to make my own taks manager perfomace graph thingy:![Perfomace thingy that I'm talking about](https://media.discordapp.net/attachments/827008047054192720/1274459699470667807/image.png?ex=66c25496&is=66c10316&hm=695636c04ffede83c57c0232c1d7b5c2ddbd19a93004c8352e9508a3f1dc10f5&=&format=webp&quality=lossless&width=805&height=589)

It did no go well in the beginning since I pretty much gave up on it for a while but I came up with different functionalities for it as you will see...

And yes if you thing that somethings look like ChatGPT made it, its because it probably did, since I'm using to learn things.

## Loading
![Loading screen](https://media.discordapp.net/attachments/827008047054192720/1274459637374128188/image.png?ex=66c25487&is=66c10307&hm=cbfc8e3d9c7b63ae5ea1d0c33b501e0a62d9ef5379c00f63189d6b6c21b22edc&=&format=webp&quality=lossless&width=1203&height=585)

* Just a silly little "loading" screen, jsut to give the impression that its accuatly loading something (but it's not)

* I got the flamingo ASCII from https://ascii.co.uk/art/flamingo

* I used [tqdm](https://github.com/tqdm/tqdm) for the loading bar

* And for the colour text I just used [ANSI Escape Sequences](https://gist.github.com/fnky/458719343aabd01cfb17a3a4f7296797)

## Main window
![Main window](https://media.discordapp.net/attachments/827008047054192720/1274462263822123088/image.png?ex=66c256fa&is=66c1057a&hm=bdd3bdec73b530e512a7d4b3175f6311d75f4f684fbc3b10b3bcdb080c9ce279&=&format=webp&quality=lossless&width=1115&height=589)

* This window is just used for navagating to different functionalities windows and it shows the current date

1. Home functions
2. Work Functions
3. Closing the terminal

### Home functions
![Home functions](https://media.discordapp.net/attachments/827008047054192720/1274463088355184740/image.png?ex=66c257be&is=66c1063e&hm=85c94ec1b74bd5efd16a1023a1f178c105e84c536cda2b8a9170fc4ca6582ee0&=&format=webp&quality=lossless&width=1108&height=589)

1. Opens my most used firefox tabs
2. Does absoluty nothing
3. Shows the percentage of cpu and ram being used and it also shows how much space is being used in both of my disks ![Percentage](https://media.discordapp.net/attachments/827008047054192720/1274464695436185683/image.png?ex=66c2593d&is=66c107bd&hm=341343b799b8aea6715770788bb5199ee4a0faadbfe1996d857cd2bd7b7e6cea&=&format=webp&quality=lossless&width=1139&height=589)
4. Its a youtube video downloader using [pytubefix](https://github.com/JuanBindez/pytubefix) since I couldn't make the acctual pytube work, don't know why. You can download the video as an MP4 or MP3, once the download is the the folder containg the file will pop open
5. Returns to previus window

### Work functions
![Work fucntions](https://media.discordapp.net/attachments/827008047054192720/1274466345563590799/image.png?ex=66c25ac7&is=66c10947&hm=7811afb8c3692e0a754797dfa5b553f77d77e9c77fd9a0a8bdcac47f4d84f6f2&=&format=webp&quality=lossless&width=1131&height=589)

1. Open Asana links that I use at work
2. Open websites that I have to test (I'm a QA at the momment)
3. Its starts an Appium server (used for mobile automatic tests)
4. Start the ADB server so it can connect my phone to the pc
5. Open's multiple [4devs](https://www.4devs.com.br/) windows that I use for generating informations
6. Goes to the previus window
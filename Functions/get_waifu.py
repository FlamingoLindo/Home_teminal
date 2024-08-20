import requests
import json
from PIL import Image
from io import BytesIO

#https://docs.waifu.im/
def get_waifu():
    api_url = 'https://api.waifu.im/search'
    params = {
        'is_nsfw': False,
    }
    response = requests.get(api_url, params=params)

    if response.status_code == 200:
        print('Getting waifu URL...')
        data = json.loads(response.text)

        image_url = data['images'][0]['url']

        image_response = requests.get(image_url)
        print("Waifu unlocked!")
        if image_response.status_code == 200:
            print("Displaying waifu 😍")
            img_data = BytesIO(image_response.content)
            
            img = Image.open(img_data)

            img.show()
        else:
            print('Failed to retrieve the image. Status code:', image_response.status_code)
    else:
        print('Request failed with status code:', response.status_code)


import requests
import json
from PIL import Image
from io import BytesIO

# API endpoint
api_url = 'https://api.waifu.im/search'
params = {
    'is_nsfw': False,
}
response = requests.get(api_url, params=params)

if response.status_code == 200:
    data = json.loads(response.text)

    # Extract the image URL from the JSON response
    image_url = data['images'][0]['url']
    
    # Make a new request to the image URL to get the image data
    image_response = requests.get(image_url)
    
    if image_response.status_code == 200:
        img_data = BytesIO(image_response.content)
        
        # Open the image with PIL
        img = Image.open(img_data)
        
        # Display the image
        img.show()
    else:
        print('Failed to retrieve the image. Status code:', image_response.status_code)
else:
    print('Request failed with status code:', response.status_code)

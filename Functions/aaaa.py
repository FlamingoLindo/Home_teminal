import requests
import json
from PIL import Image
from io import BytesIO

# Get data from the APIhttps://scryfall.com/docs/api/lists
req = requests.get("https://api.magicthegathering.io/v1/cards/:id")
test = json.loads(req.text)

# Print the raw data to inspect it
#print(test)

# Extract the image URL
# Assuming the first card in the list is the one you're interested in
image_url = test['cards'][0]['imageUrl']


print(image_url)

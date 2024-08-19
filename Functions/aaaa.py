import requests
import json

# https://currentsapi.services/en/profile
url = ('https://api.currentsapi.services/v1/latest-news?'
        'language=us&'
        '-wjMcbcyYHNnP0hDomiqm81_YZ_kaK7VCm4cTLSfNJQk-Aje')
req = requests.get(url)


response_json = json.loads(req.text)


print(response_json)

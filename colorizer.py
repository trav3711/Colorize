import requests
r = requests.post(
    "https://api.deepai.org/api/colorizer",
    files={
        'image': open('./p02yvl53.jpg', 'rb'),
        'image': open('./2c452f43f056840dabb20ee28639de43.jpg', 'rb'),
    },
    headers={'api-key': 'quickstart-QUdJIGlzIGNvbWluZy4uLi4K'}
)
print(r.json())

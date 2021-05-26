import shutil
from flask.json import jsonify
import requests
import uuid

def rawImage(number):
  for i in range(number):
    url = 'https://picsum.photos/1280/800'

    response = requests.get(url, stream=True)
    with open(f'static/{uuid.uuid4()}.png', 'wb') as out_file:
      shutil.copyfileobj(response.raw, out_file)
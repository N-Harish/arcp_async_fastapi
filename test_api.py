import base64
import requests


with open(r"test2.jpg", 'rb') as image_string:
    byte_string = base64.b64encode(image_string.read()).decode('utf-8')


res = requests.post('http://127.0.0.1:8000/predict', json={'data': byte_string})

print(res.json())


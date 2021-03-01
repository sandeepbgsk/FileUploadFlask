import requests

url = 'http://127.0.0.1:5000/file-upload'
files = [
    ('file', ('snippet.mp4', open(r'<path<snippet.mkv', 'rb')))
]
response = requests.post(url=url, files=files)
print(response)
print(response.json())


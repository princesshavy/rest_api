import requests
import json

response = requests.get('https://jsonplaceholder.typicode.com/todos/1')

print(response.json()['items'])
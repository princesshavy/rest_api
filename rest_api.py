import requests
api_url = "https://jsonplaceholder.typicode.com/todos/1"
response = requests.get(api_url)
response.headers
print('Header', response.headers)
print(response.json())
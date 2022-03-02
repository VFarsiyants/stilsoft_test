import requests
from getpass import getpass

models_endpoints = {'1': 'books', '2': 'authors'}

auth_endpoint = 'http://127.0.0.1:8000/api/auth/'
# admin, visitor, staff, visout_perm
model = models_endpoints[input('выберите модель:\n1: Book\n2: Author\n:')]
username = input('Введите ваш логин\n')
password = getpass('Введите пароль\n')

auth_response = requests.post(auth_endpoint, json={'username': username, 'password': password})
print(auth_response.json())

if auth_response.status_code == 200:
    token = auth_response.json()['token']
    headers = {
        "Authorization": f"Token {token}"
    }
    id = input('Введите ID для выбранного объекта\n')
    endpoint = f'http://127.0.0.1:8000/api/{model}/{id}/'
    get_response = requests.get(endpoint, headers=headers)
    print(get_response.json())

import requests
from getpass import getpass

models_endpoints = {'1': 'books', '2': 'authors'}

auth_endpoint = 'http://127.0.0.1:8000/api/auth/'
# admin, visitor, staff, visout_perm
model = models_endpoints[input('выберите модель:\n1: Book\n2: Author\n:')]
username = input('Введите ваш логин\n')
password = getpass('Введите пароль\n')
endpoint = f'http://127.0.0.1:8000/api/{model}/'

auth_response = requests.post(auth_endpoint, json={'username': username, 'password': password})
print(auth_response.json())

if auth_response.status_code == 200:
    token = auth_response.json()['token']
    headers = {
        "Authorization": f"Token {token}"
    }
    if model == 'books':
        name = input('Введите название книги\n')
        published_year = input('Введите год публикации книги\n')
        author = input('Введите ID автора\n')
        get_response = requests.post(endpoint, headers=headers,
                                     json={
                                         'name': name,
                                         'publishedYear': int(published_year),
                                         'author': int(author)
                                     })
        print(get_response.json())
        if get_response.status_code == 201:
            obj_id = get_response.json()['id']
            print('*' * 100)
            print(f'Объект создан c id:{obj_id}')
            if input('Удалить объект?(y/n)\n').lower().startswith('y'):
                print('проверяем удаление')
                delete_request = requests.delete(endpoint, headers=headers)
                print(delete_request.json())
    else:
        first_name = input('Введите имя автора:\n')
        last_name = input('Введите фамилию автора:\n')
        birthdate = input('Введите дату рождения автора в формате ГГГГ-ММ-ДД:\n')
        get_response = requests.post(endpoint, headers=headers,
                                     json={
                                         'firstName': first_name,
                                         'lastName': last_name,
                                         'birthdate': birthdate
                                     })
        print(get_response.json())
        if get_response.status_code == 201:
            obj_id = get_response.json()['id']
            print('*' * 100)
            print(f'Объект создан c id:{obj_id}')
            if input('Удалить объект?(y/n)\n').lower().startswith('y'):
                print('проверяем удаление')
                delete_request = requests.delete(endpoint, headers=headers)
                print(delete_request.json())


import requests
from getpass import getpass

models_endpoints = {'1': 'books', '2': 'authors'}

auth_endpoint = 'http://127.0.0.1:8000/api/auth/'
# admin, visitor, staff, visout_perm
username = input('Введите ваш логин\n')
password = getpass('Введите пароль\n')

auth_response = requests.post(auth_endpoint, json={'username': username, 'password': password})
print(auth_response.json())

if auth_response.status_code == 200:
    token = auth_response.json()['token']
    model = models_endpoints[input('выберите модель:\n1: Book\n2: Author\n:')]
    filter_url = ''
    if input('Применять фильтры? (y/n)').lower().startswith('y'):
        print('если фильтр не нужен, оставить пустым')
        if model == 'books':
            author_name = input('Имя автора содержит\n')
            author_last_name = input('Фамилия автора содержит\n')
            name = input('Название книги содержит\n')
            published_year_gte = input('Написана позже года\n')
            published_year_lte = input('Написана раньше года\n')
            filter_url = f'?author__first_name={author_name}&author__last_name=' \
                         f'{author_last_name}&name={name}&published_year_gte=' \
                         f'{published_year_gte}&published_year_lte={published_year_lte}'

        else:
            first_name = input('Имя автора содержит\n')
            last_name = input('Фамилия автора содержит\n')
            birthdate_gte = input('Родился позже (ГГГГ-ММ-ДД)\n')
            birthdate_lte = input('Родился раньше (ГГГГ-ММ-ДД)\n')
            filter_url = f'?first_name={first_name}&last_name={last_name}&' \
                         f'birthdate_gte={birthdate_gte}&birthdate_lte={birthdate_lte}'

    headers = {
        "Authorization": f"Token {token}"
    }
    endpoint = f'http://127.0.0.1:8000/api/{model}/{filter_url}'
    get_response = requests.get(endpoint, headers=headers)
    print(get_response.json())

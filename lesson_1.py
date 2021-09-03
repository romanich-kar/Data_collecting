"""1. Посмотреть документацию к API GitHub, разобраться как вывести список репозиториев для конкретного пользователя,
сохранить JSON-вывод в файле *.json."""

import requests
import json

url = 'https://api.github.com/users/octocat/repos'
req = requests.get(url)
with open('response_1.json', 'w') as res:
    json.dump(req.json(), res)
for i in req.json():
    print(i['name'])

"""2. Изучить список открытых API. Найти среди них любое, требующее авторизацию (любого типа).
Выполнить запросы к нему, пройдя авторизацию. Ответ сервера записать в файл."""
url = 'https://api.github.com/user/repos'
token = 'token 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'
headers = {
    'Content-Type': 'application/json',
    'Authorization': token
}
req = requests.get(url, headers=headers)
with open('response_2.json', 'w') as res:
    json.dump(req.json(), res)
for i in req.json():
    print(i['name'])
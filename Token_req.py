import requests
import time
response = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job")#создание задачи
print(response.text)

response = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params={"token":"AM0oDO0oDMyASNy0iNw0SMyAjM"})#запрос с token ДО того, как задача готова,
print(response.text)

time.sleep(3)
response = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job",params={"token": "wM1oDNyoDMyASNy0iNw0SMyAjM"})#запрос c token ПОСЛЕ того, как задача готова,
print(response.text)
import requests
import time
response = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job")#-создание задачи
print(response.text)

response = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params={"token":"ANwozMyozNxAyNy0iNw0SMyAjM"})#запрос До того как токен создавал задачу
print(response.text)

time.sleep(9)
response = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job",params={"token": "wM1oDNyoDMyASNy0iNw0SMyAjM"})#сзапрос c token ПОСЛЕ того, как задача готова

print(response.text)

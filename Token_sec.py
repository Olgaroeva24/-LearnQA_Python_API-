import requests
import time

response = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job")

print(response.text)

obj = response.json()

token = obj['token']
seconds = obj['seconds']

response = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params={"token": token})
obj = response.json()
print(obj)

time.sleep(seconds+1)
response = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params={"token": token})
obj = response.json()
print(obj)
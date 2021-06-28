import requests
import time
response = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job")
print(response.text)
x = response.json()
token = x['token']
seconds = x['seconds']

response = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params={"token": token})
x = response.json()
print(x)

time.sleep(seconds+1)
response = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params={"token": token})
x = response.json()
print(x)
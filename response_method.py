import requests
response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type")
print(response.text)
response = requests.head("https://playground.learnqa.ru/ajax/api/compare_query_type",params={"method":"HEAD"})
print(response.text)
response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params={"method":"GET"})
print(response.text)
response = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", data={"method":"GET"})
print(response.text)
response = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", data={"method":"PUT"})
print(response.text)
response = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", data={"method":"DELETE"})
print(response.text)

response = requests.delete("https://playground.learnqa.ru/ajax/api/compare_query_type", params={"method":"GET"})
print(response.text)
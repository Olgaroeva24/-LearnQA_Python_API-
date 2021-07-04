import requests


class TestHeaders:
    def test_headers(self):
        response = requests.get("https://playground.learnqa.ru/api/homework_header")
        print(response.headers)
        headers_value = {'Date': 'Sun, 04 Jul 2021 19:33:45 GMT', 'Content-Type': 'application/json',
                         'Content-Length': '15', 'Connection': 'keep-alive', 'Keep-Alive': 'timeout=10',
                         'Server': 'Apache', 'x-secret-homework-header': 'Some secret value',
                         'Cache-Control': 'max-age=0', 'Expires': 'Sun, 04 Jul 2021 19:33:45 GMT'}

        assert response.headers == headers_value, f"there is not response.cookies =  {headers_value}"

import requests


class TestCookies:
    def test_cookies(self):
        response = requests.get("https://playground.learnqa.ru/api/homework_cookie")
        print(dict(response.cookies))
        cookie_value = {'HomeWork': 'hw_value'}
        assert response.cookies == cookie_value, f"there is not response.cookies =  {cookie_value} "

import requests


class APIClient:
    BASE_URL = "https://stellarburgers.nomoreparties.site"

    def registration_user(self, endpoint="/api/auth/register", data=None):
        url = f"{self.BASE_URL}{endpoint}"
        return requests.post(url, json=data)

    def get_ingredients(self, endpoint="/api/ingredients", params=None):
        url = f"{self.BASE_URL}{endpoint}"
        return requests.get(url, params=params)

    def authorization_user(self, endpoint="/api/auth/login", data=None):
        url = f"{self.BASE_URL}{endpoint}"
        return requests.post(url, json=data)

    def delete_user(self,endpoint = "/api/auth/user"):
        url = f"{self.BASE_URL}{endpoint}"
        return requests.delete(url)


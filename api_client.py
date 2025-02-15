import requests


class APIClient:
    BASE_URL = "https://stellarburgers.nomoreparties.site"

    def registration_user(self, endpoint="/api/auth/register", data=None):
        url = f"{self.BASE_URL}{endpoint}"
        return requests.post(url, json=data)

    def get_ingredients(self, endpoint="/api/ingredients", params=None,authorization=None):
        url = f"{self.BASE_URL}{endpoint}"
        return requests.get(url, params=params,headers={"Authorization": authorization})

    def authorization_user(self, endpoint="/api/auth/login", data=None):
        url = f"{self.BASE_URL}{endpoint}"
        return requests.post(url, json=data)

    def delete_user(self,endpoint = "/api/auth/user",authorization=None):
        url = f"{self.BASE_URL}{endpoint}"
        return requests.delete(url,headers={"Authorization": authorization})

    def create_order(self,endpoint="/api/orders", data=None,authorization=None):
        url = f"{self.BASE_URL}{endpoint}"
        return requests.post(url, json=data,headers={"Authorization": authorization})

    def get_orders(self,endpoint="/api/orders", params=None,authorization=None):
        url = f"{self.BASE_URL}{endpoint}"
        return requests.get(url, params=params, headers={"Authorization": authorization})

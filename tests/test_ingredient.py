import pytest
import requests

class TestIgredient:
    def test_get_inredient_data(self, api_client):
        response = api_client.get_ingredients()
        #print(response.json())
        assert response.status_code == 200

class TestRegistrationUser():

    def test_registration_empty_user(self,api_client):
        response = api_client.registration_user()
        assert response.status_code == 403

    def test_registration_user(self,api_client): #{name: "shurik", email: "karetniy@thebest", password: "zaz123456"} то, что уходит на
        response = api_client.registration_user(data={"name": "Влад","email": "mezenov@gmail.com","password": "mezenov321"})
        #assert response.status_code == 200
        api_client.delete_user()
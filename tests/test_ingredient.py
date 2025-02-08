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

class TestLoginUser:

    def test_authorization_user_with_all_fulling_fields(self,api_client):
        response = api_client.authorization_user(data={"email": "mezenov@gmail.com", "password": "mezenov321"})
        assert response.status_code == 200

    def test_authorization_user_without_password(self,api_client):
        response = api_client.authorization_user(data={"email": "mezenov@gmail.com", "password": None})
        assert response.status_code == 401

    def test_authorization_user_without_email(self,api_client):
        response = api_client.authorization_user(data={"email": None, "password": "mezenov321"})
        assert response.status_code == 401

    def test_authorization_empty_user(self,api_client):
        response = api_client.authorization_user(data={"email": None, "password": None})
        assert response.status_code == 401

class TestDeleteUser:

    def test_delete_authorization_user(self,api_client):
        response = api_client.delete_user(authorization="Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjY3YTM2OTcyOWVkMjgwMDAxYjU2MmM0NSIsImlhdCI6MTczODc2MjkxNywiZXhwIjoxNzM4NzY0MTE3fQ.t8ppCnXMo1TNvmbLGhuWH5DE-n4MMguycViu3pYUkmM")
        assert response.status_code == 202
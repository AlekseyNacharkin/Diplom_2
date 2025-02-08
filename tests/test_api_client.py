import pytest
import requests



class TestIngredient:
    def test_get_inredient_data_unauthorized_user(self, api_client):
        response = api_client.get_ingredients()
        #print(response.json())
        assert response.status_code == 200

    def test_get_ingredient_data_authorized_user_without_orders(self,get_token,api_client):
        response = api_client.get_ingredients(authorization=get_token)
        assert isinstance(response.json(),dict)

class TestCreateOrder:

    def test_get_authorized_user_order_data_with_ingredients(self,get_token,api_client):
        response = api_client.create_order(data={"ingredients": ["61c0c5a71d1f82001bdaaa6d","61c0c5a71d1f82001bdaaa70"]},authorization=get_token)
        #print(data)
        assert "Метеоритный флюоресцентный бургер" in response.json()["name"] and response.status_code == 200

    def test_get_authorized_user_order_data_without_ingredients(self,api_client,get_token):
        response = api_client.create_order(authorization=get_token)
        assert response.status_code == 400 and response.json()["message"] == 'Ingredient ids must be provided'

    def test_create_order_unauthorized_user(self,api_client):
        response = api_client.create_order(data={"ingredients": ["61c0c5a71d1f82001bdaaa6d","61c0c5a71d1f82001bdaaa70"]})
        assert response.status_code == 200 and "Метеоритный флюоресцентный бургер" in response.json()["name"]

    def test_create_order_unauthorized_user_with_nonexistent_ingredient_hash(self,api_client):
        response = api_client.create_order(
            data={"ingredients": ["61c0c5a71d1f82001bdaaa68"]})
        assert response.status_code == 400  and response.json()["message"] == "One or more ids provided are incorrect"




class TestRegistrationUser():

    def test_registration_empty_user(self,api_client):
        response = api_client.registration_user()
        assert response.status_code == 403

    def test_registration_user(self,api_client): #{name: "shurik", email: "karetniy@thebest", password: "zaz123456"} то, что уходит на
        try:
            response = api_client.registration_user(data={"name": "Влад","email": "mezenov@gmail.com","password": "mezenov321"})
            assert response.status_code == 200
        finally:
            authorization_user = api_client.authorization_user(
                data={"email": "mezenov@gmail.com", "password": "mezenov321"})
            authorization_user_token = authorization_user.json().get("accessToken")
            api_client.delete_user(authorization=authorization_user_token)

    def test_repeated_user_registration(self,api_client,get_token):
        response = api_client.registration_user(data={"name": "Влад","email": "mezenov@gmail.com","password": "mezenov321"})
        assert response.status_code == 403 and response.json().get("message") == "User already exists"

    def test_registration_user_without_email(self,api_client):
        response = api_client.registration_user(data={"name": "Влад","email": None,"password": "mezenov321"})
        assert response.status_code == 403 and response.json()["message"] == 'Email, password and name are required fields'


class TestAuthorizationUser:

    def test_authorization_user_with_all_fulling_fields(self,api_client,get_token):
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

    def test_authorization_user_with_nonexistent_user_and_password(self,api_client):
        response = api_client.authorization_user(data={"email": "email", "password": "email"})
        assert response.status_code == 401 and response.json().get("message") == "email or password are incorrect"

class TestGetOrders:

    def test_get_orders_unauthorized_user(self,api_client):
        response = api_client.get_orders()
        assert response.status_code == 401 and response.json().get("message") == "You should be authorised"

    def test_get_orders_authorized_user(self,api_client,get_token):
        response = api_client.create_order(data={"ingredients": ["61c0c5a71d1f82001bdaaa6d","61c0c5a71d1f82001bdaaa70"]},authorization=get_token)
        response1 = api_client.get_orders(authorization=get_token)
        assert response1.status_code == 200 and response1.json().get('success') == True

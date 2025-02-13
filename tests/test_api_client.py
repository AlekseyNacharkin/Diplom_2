from Diplom_2.constants import ForFixtures
from Diplom_2.constants import TestValues


class TestIngredient:
    def test_get_ingredient_data_unauthorized_user(self, api_client):
        response = api_client.get_ingredients()
        assert response.status_code == 200

    def test_get_ingredient_data_authorized_user_without_orders(self,get_token,api_client):
        response = api_client.get_ingredients(authorization=get_token)
        assert isinstance(response.json(),dict)

class TestCreateOrder:

    def test_get_authorized_user_order_data_with_ingredients(self,get_token,api_client):
        response = api_client.create_order(data=TestValues.INGREDIENTS,authorization=get_token)
        assert TestValues.FLUORESTENTIC_BUN in response.json().get("name") and response.status_code == 200

    def test_get_authorized_user_order_data_without_ingredients(self,api_client,get_token):
        response = api_client.create_order(authorization=get_token)
        assert response.status_code == 400 and response.json()["message"] == TestValues.MESSAGE_UFILLED_ID_INGREDIENTS

    def test_create_order_unauthorized_user(self,api_client):
        response = api_client.create_order(data=TestValues.INGREDIENTS)
        assert response.status_code == 200 and TestValues.FLUORESTENTIC_BUN in response.json().get("name")

    def test_create_order_unauthorized_user_with_nonexistent_ingredient_hash(self,api_client):
        response = api_client.create_order(
            data=TestValues.UNCORRECTED_INGREDIENT)
        assert response.status_code == 400  and response.json()["message"] == TestValues.UNCORRECTED_INGREDIENT_ID_MESSAGE




class TestRegistrationUser():

    def test_registration_empty_user(self,api_client):
        response = api_client.registration_user()
        assert response.status_code == 403

    def test_registration_user(self,api_client):
        try:
            response = api_client.registration_user(data=ForFixtures.USERVALUE)
            assert response.status_code == 200
        finally:
            authorization_user = api_client.authorization_user(
                data={"email": ForFixtures.USERVALUE.get("email"), "password": ForFixtures.USERVALUE.get("password")})
            authorization_user_token = authorization_user.json().get("accessToken")
            api_client.delete_user(authorization=authorization_user_token)

    def test_repeated_user_registration(self,api_client,get_token):
        response = api_client.registration_user(data=ForFixtures.USERVALUE)
        assert response.status_code == 403 and response.json().get("message") == TestValues.USER_EXIST_MESSAGE

    def test_registration_user_without_email(self,api_client):
        response = api_client.registration_user(data={"name": ForFixtures.USERVALUE.get("name"),"email": None,"password": ForFixtures.USERVALUE.get("password")})
        assert response.status_code == 403 and response.json()["message"] == TestValues.VALUES_IN_REQUIRED_FIELDS_EMPTY


class TestAuthorizationUser:

    def test_authorization_user_with_all_fulling_fields(self,api_client,get_token):
        response = api_client.authorization_user(data=TestValues.VALUES_FOR_AUTHORIZATION)
        assert response.status_code == 200

    def test_authorization_user_without_password(self,api_client):
        response = api_client.authorization_user(data={"email": TestValues.VALUES_FOR_AUTHORIZATION.get("email"), "password": None})
        assert response.status_code == 401

    def test_authorization_user_without_email(self,api_client):
        response = api_client.authorization_user(data={"email": None, "password": TestValues.VALUES_FOR_AUTHORIZATION.get("password")})
        assert response.status_code == 401

    def test_authorization_empty_user(self,api_client):
        response = api_client.authorization_user(data={"email": None, "password": None})
        assert response.status_code == 401

    def test_authorization_user_with_nonexistent_user_and_password(self,api_client):
        response = api_client.authorization_user(data={"email": "email", "password": "email"})
        assert response.status_code == 401 and response.json().get("message") == TestValues.MESSAGE_UNCORRECT_VALUES_FOR_AUTHORIZATION

class TestGetOrders:

    def test_get_orders_unauthorized_user(self,api_client):
        response = api_client.get_orders()
        assert response.status_code == 401 and response.json().get("message") == TestValues.MESSAGE_SHOULD_AUTHORIZATION

    def test_get_orders_authorized_user(self,api_client,get_token):
        response = api_client.create_order(data=TestValues.INGREDIENTS,authorization=get_token)
        response1 = api_client.get_orders(authorization=get_token)
        assert response1.status_code == 200 and response1.json().get('success') == True

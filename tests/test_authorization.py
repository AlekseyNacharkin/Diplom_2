from Diplom_2.constants import TestValues
import allure

class TestAuthorizationUser:

    @allure.title("Авторизация пользователя с указанием всех данных")
    def test_authorization_user_with_all_fulling_fields(self,api_client,get_token):
        response = api_client.authorization_user(data=TestValues.VALUES_FOR_AUTHORIZATION)
        assert response.status_code == 200

    @allure.title("Авторизация пользователя без указания пароля")
    def test_authorization_user_without_password(self,api_client):
        response = api_client.authorization_user(data={"email": TestValues.VALUES_FOR_AUTHORIZATION.get("email"), "password": None})
        assert response.status_code == 401

    @allure.title("Авторизация пользователя без указания почты")
    def test_authorization_user_without_email(self,api_client):
        response = api_client.authorization_user(data={"email": None, "password": TestValues.VALUES_FOR_AUTHORIZATION.get("password")})
        assert response.status_code == 401

    @allure.title("Авторизация пользователя без указания данных")
    def test_authorization_empty_user(self,api_client):
        response = api_client.authorization_user(data={"email": None, "password": None})
        assert response.status_code == 401

    @allure.title("Авторизация пользователя с указанием несуществующих данных почты и пароля")
    def test_authorization_user_with_nonexistent_user_and_password(self,api_client):
        response = api_client.authorization_user(data={"email": "email", "password": "email"})
        assert response.status_code == 401
        assert response.json().get("message") == TestValues.MESSAGE_UNCORRECT_VALUES_FOR_AUTHORIZATION

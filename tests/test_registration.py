from Diplom_2.constants import ForFixtures
from Diplom_2.constants import TestValues
import allure


class TestRegistrationUser():

    @allure.title("Регистрация пользователя без указания данных")
    def test_registration_empty_user(self,api_client):
        response = api_client.registration_user()
        assert response.status_code == 403


    @allure.title("Регистрация пользователя с указанием данных")
    def test_registration_user(self,api_client):
        try:
            response = api_client.registration_user(data=ForFixtures.USERVALUE)
            assert response.status_code == 200
        finally:
            authorization_user = api_client.authorization_user(
                data={"email": ForFixtures.USERVALUE.get("email"), "password": ForFixtures.USERVALUE.get("password")})
            authorization_user_token = authorization_user.json().get("accessToken")
            api_client.delete_user(authorization=authorization_user_token)

    @allure.title("Регистрация пользователя с указанием данных уже существующего пользователя")
    def test_repeated_user_registration(self,api_client,get_token):
        response = api_client.registration_user(data=ForFixtures.USERVALUE)
        assert response.status_code == 403 and response.json().get("message") == TestValues.USER_EXIST_MESSAGE

    @allure.title("Регистрация пользователя без указания почты")
    def test_registration_user_without_email(self,api_client):
        response = api_client.registration_user(data={"name": ForFixtures.USERVALUE.get("name"),"email": None,"password": ForFixtures.USERVALUE.get("password")})
        assert response.status_code == 403 and response.json()["message"] == TestValues.VALUES_IN_REQUIRED_FIELDS_EMPTY
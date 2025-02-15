import pytest
from Diplom_2.constants import ForFixtures
from Diplom_2.api_client import APIClient


@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def get_token(api_client):
    response = api_client.registration_user(data=ForFixtures.USERVALUE)
    email = ForFixtures.USERVALUE.get("email")
    password = ForFixtures.USERVALUE.get("password")
    authorization_user = api_client.authorization_user(data={"email": email, "password": password})
    authorization_user_token = authorization_user.json().get("accessToken")
    yield authorization_user_token
    api_client.delete_user(authorization=authorization_user_token)
import pytest

from Diplom_2.tests.api_client import APIClient


@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def get_token(api_client):
    response = api_client.registration_user(data={"name": "Влад","email": "mezenov@gmail.com","password": "mezenov321"})
    authorization_user = api_client.authorization_user(data={"email": "mezenov@gmail.com", "password": "mezenov321"})
    authorization_user_token = authorization_user.json().get("accessToken")
    yield authorization_user_token
    api_client.delete_user(authorization=authorization_user_token)
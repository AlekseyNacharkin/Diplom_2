from Diplom_2.constants import TestValues
import allure

class TestGetOrders:

    @allure.title("Получение заказа неавторизованного пользователя")
    def test_get_orders_unauthorized_user(self,api_client):
        response = api_client.get_orders()
        assert response.status_code == 401
        assert response.json().get("message") == TestValues.MESSAGE_SHOULD_AUTHORIZATION

    @allure.title("Получение заказа авторизованного пользователя")
    def test_get_orders_authorized_user(self,api_client,get_token):
        response = api_client.create_order(data=TestValues.INGREDIENTS,authorization=get_token)
        response1 = api_client.get_orders(authorization=get_token)
        assert response1.status_code == 200
        assert response.json().get('success') == True
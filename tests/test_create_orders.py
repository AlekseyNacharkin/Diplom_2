import allure
from Diplom_2.constants import TestValues

class TestCreateOrder:

    @allure.title("Получение ингредиентов заказа авторизованным пользователем")
    def test_get_authorized_user_order_data_with_ingredients(self,get_token,api_client):
        response = api_client.create_order(data=TestValues.INGREDIENTS,authorization=get_token)
        assert TestValues.FLUORESTENTIC_BUN in response.json().get("name")
        assert response.status_code == 200

    @allure.title("Получение ингредиентов заказа без указания ингредиентов в заказе авторизованным пользователем")
    def test_get_authorized_user_order_data_without_ingredients(self,api_client,get_token):
        response = api_client.create_order(authorization=get_token)
        assert response.status_code == 400
        assert response.json()["message"] == TestValues.MESSAGE_UFILLED_ID_INGREDIENTS

    @allure.title("Получение ингредиентов в заказе не авторизованным пользователем")
    def test_create_order_unauthorized_user(self,api_client):
        response = api_client.create_order(data=TestValues.INGREDIENTS)
        assert response.status_code == 200
        assert TestValues.FLUORESTENTIC_BUN in response.json().get("name")

    @allure.title("Создание заказа с указанием несуществующего хэша ингредиента")
    def test_create_order_unauthorized_user_with_nonexistent_ingredient_hash(self,api_client):
        response = api_client.create_order(
            data=TestValues.UNCORRECTED_INGREDIENT)
        assert response.status_code == 400
        assert response.json()["message"] == TestValues.UNCORRECTED_INGREDIENT_ID_MESSAGE

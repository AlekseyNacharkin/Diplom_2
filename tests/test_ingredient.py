import allure
from Diplom_2.constants import TestValues


class TestIngredient:
    @allure.title("Получение ингредиентов неавторизованным пользователем")
    def test_get_ingredient_data_unauthorized_user(self, api_client):
        response = api_client.get_ingredients()
        assert response.status_code == 200
        assert response.json() == TestValues.RESPONSE_INGREDIENT_DATA

    @allure.title("Получение ингредиентов авторизованным пользователем без заказов")
    def test_get_ingredient_data_authorized_user_without_orders(self,get_token,api_client):
        response = api_client.get_ingredients(authorization=get_token)
        assert response.json() == TestValues.RESPONSE_INGREDIENT_DATA
        assert response.status_code == 200
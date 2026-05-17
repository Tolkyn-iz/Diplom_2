import allure
from api.order_api import OrderAPI


@allure.feature("Заказы")
class TestCreateOrder:

    @allure.title("Создание заказа с авторизацией")
    def test_create_order_with_auth(self, auth_token, valid_ingredients):
        response = OrderAPI.create_order(valid_ingredients, auth_token)
        assert response.status_code == 200
        assert response.json()["success"] is True
        assert "order" in response.json()

    @allure.title("Создание заказа без авторизации")
    def test_create_order_without_auth(self, valid_ingredients):
        response = OrderAPI.create_order(valid_ingredients)
        assert response.status_code == 200
        assert response.json()["success"] is True

    @allure.title("Создание заказа с ингредиентами")
    def test_create_order_with_ingredients(self, auth_token, valid_ingredients):
        response = OrderAPI.create_order(valid_ingredients, auth_token)
        assert response.status_code == 200
        assert len(response.json()["order"]["ingredients"]) > 0

    @allure.title("Создание заказа без ингредиентов")
    def test_create_order_without_ingredients(self, auth_token, empty_ingredients):
        response = OrderAPI.create_order(empty_ingredients, auth_token)
        assert response.status_code == 400
        assert response.json()["message"] == "Ingredient ids must be provided"

    @allure.title("Создание заказа с невалидным хешем ингредиента")
    def test_create_order_invalid_hash(self, auth_token, invalid_ingredient_hash):
        response = OrderAPI.create_order(invalid_ingredient_hash, auth_token)
        assert response.status_code == 500
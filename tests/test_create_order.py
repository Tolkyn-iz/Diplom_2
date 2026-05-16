import allure
import pytest
from api.user_api import UserAPI
from api.order_api import OrderAPI


@allure.feature("Создание заказа")
class TestCreateOrder:

    @allure.title("Создание заказа с авторизацией")
    def test_create_order_with_auth(self, unique_user_data, valid_ingredients):
        register_response = UserAPI.create_user(unique_user_data)
        assert register_response.status_code == 200
        
        access_token = register_response.json()["accessToken"]
        response = OrderAPI.create_order(valid_ingredients, access_token)
        
        assert response.status_code == 200
        assert response.json()["success"] is True

    @allure.title("Создание заказа без авторизации")
    def test_create_order_without_auth(self, valid_ingredients):
        response = OrderAPI.create_order(valid_ingredients)
        
        assert response.status_code == 200
        assert response.json()["success"] is True

    @allure.title("Создание заказа с ингредиентами")
    def test_create_order_with_ingredients(self, unique_user_data, valid_ingredients):
        register_response = UserAPI.create_user(unique_user_data)
        assert register_response.status_code == 200
        
        access_token = register_response.json()["accessToken"]
        response = OrderAPI.create_order(valid_ingredients, access_token)
        
        assert response.status_code == 200
        assert response.json()["success"] is True
        assert response.json()["order"]["number"] is not None

    @allure.title("Создание заказа без ингредиентов")
    def test_create_order_without_ingredients(self, unique_user_data, empty_ingredients):
        register_response = UserAPI.create_user(unique_user_data)
        assert register_response.status_code == 200
        
        access_token = register_response.json()["accessToken"]
        response = OrderAPI.create_order(empty_ingredients, access_token)
        
        assert response.status_code == 400
        assert response.json()["message"] == "Ingredient ids must be provided"

    @allure.title("Создание заказа с неверным хешем ингредиентов")
    def test_create_order_with_invalid_ingredient_hash(self, unique_user_data, invalid_ingredient_hash):
        register_response = UserAPI.create_user(unique_user_data)
        assert register_response.status_code == 200
        
        access_token = register_response.json()["accessToken"]
        response = OrderAPI.create_order(invalid_ingredient_hash, access_token)
        
        assert response.status_code == 500

    @allure.title("Создание заказа без поля ingredients")
    def test_create_order_no_ingredients_field(self, unique_user_data):
        register_response = UserAPI.create_user(unique_user_data)
        assert register_response.status_code == 200
        
        access_token = register_response.json()["accessToken"]
        response = OrderAPI.create_order({}, access_token)
        
        assert response.status_code == 400
        assert response.json()["message"] == "Ingredient ids must be provided"

    @allure.title("Создание заказа и проверка в списке заказов пользователя")
    def test_create_order_and_verify_in_user_orders(self, unique_user_data, valid_ingredients):
        register_response = UserAPI.create_user(unique_user_data)
        assert register_response.status_code == 200
        
        access_token = register_response.json()["accessToken"]
        
        create_response = OrderAPI.create_order(valid_ingredients, access_token)
        assert create_response.status_code == 200
        
        order_number = create_response.json()["order"]["number"]
        
        orders_response = OrderAPI.get_user_orders(access_token)
        
        assert orders_response.status_code == 200
        orders = orders_response.json()["orders"]
        assert any(order["number"] == order_number for order in orders)
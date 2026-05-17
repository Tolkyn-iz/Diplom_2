import allure
import requests
from data import ENDPOINTS


@allure.feature("Ингредиенты")
class TestGetIngredients:

    @allure.title("Получить список всех ингредиентов")
    def test_get_all_ingredients(self):
        response = requests.get(ENDPOINTS["get_ingredients"])
        assert response.status_code == 200
        assert response.json()["success"] is True
        assert "data" in response.json()
        assert len(response.json()["data"]) > 0

    @allure.title("Проверка структуры ингредиентов")
    def test_ingredients_structure(self):
        response = requests.get(ENDPOINTS["get_ingredients"])
        ingredient = response.json()["data"][0]
        assert "_id" in ingredient
        assert "name" in ingredient
        assert "type" in ingredient
        assert "price" in ingredient
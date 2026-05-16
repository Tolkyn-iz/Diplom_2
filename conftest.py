import pytest
import requests
import uuid
from api.user_api import UserAPI


@pytest.fixture(scope="session")
def valid_ingredients():
    """Получаем реальные ID ингредиентов из API"""
    url = "https://stellarburgers.education-services.ru/api/ingredients"
    response = requests.get(url)
    ingredients = response.json()["data"]
    # Берем первые два ингредиента
    ingredient_ids = [ing["_id"] for ing in ingredients[:2]]
    return {"ingredients": ingredient_ids}


@pytest.fixture
def unique_user_data():
    """Создание уникального пользователя"""
    unique_suffix = str(uuid.uuid4())[:8]
    return {
        "email": f"test_{unique_suffix}@example.com",
        "password": f"Pass{unique_suffix}123!",
        "name": f"User_{unique_suffix}"
    }


@pytest.fixture
def invalid_ingredient_hash():
    """Невалидный хеш ингредиента"""
    return {
        "ingredients": ["invalid_hash_123", "60d3b41abdacab0026a733c6"]
    }


@pytest.fixture
def empty_ingredients():
    """Пустой список ингредиентов"""
    return {
        "ingredients": []
    }
import pytest
from helpers import get_ingredient_ids
from api.user_api import UserAPI
from data import INVALID_INGREDIENT_HASH, EMPTY_INGREDIENTS


@pytest.fixture
def valid_ingredients():
    """Фикстура с реальными ID ингредиентов"""
    ingredient_ids = get_ingredient_ids()
    return {"ingredients": ingredient_ids}


@pytest.fixture
def empty_ingredients():
    """Пустой список ингредиентов (из data)"""
    return EMPTY_INGREDIENTS


@pytest.fixture
def invalid_ingredient_hash():
    """Невалидный хеш ингредиента (из data)"""
    return INVALID_INGREDIENT_HASH


@pytest.fixture
def unique_user_data():
    """Уникальные данные пользователя (без создания)"""
    import random
    return {
        "email": f"test_{random.randint(10000, 99999)}@test.com",
        "password": "Test123456",
        "name": f"User_{random.randint(100, 999)}"
    }


@pytest.fixture
def created_user(unique_user_data):
    """Создаёт пользователя и удаляет после теста (без assert)"""
    response = UserAPI.create_user(unique_user_data)
    access_token = response.json().get("accessToken")
    
    # Возвращаем данные, а не делаем assert
    yield response, unique_user_data
    
    # Очистка после теста (даже если тест упал)
    if access_token:
        UserAPI.delete_user(access_token)


@pytest.fixture
def auth_token(created_user):
    """Возвращает токен авторизации (без assert)"""
    response, _ = created_user
    return response.json().get("accessToken")
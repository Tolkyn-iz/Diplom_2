# data.py
BASE_URL = "https://stellarburgers.education-services.ru/api"

ENDPOINTS = {
    "create_user": f"{BASE_URL}/auth/register",
    "login_user": f"{BASE_URL}/auth/login",
    "logout_user": f"{BASE_URL}/auth/logout",
    "refresh_token": f"{BASE_URL}/auth/token",
    "get_user": f"{BASE_URL}/auth/user",
    "update_user": f"{BASE_URL}/auth/user",
    "create_order": f"{BASE_URL}/orders",
    "get_orders": f"{BASE_URL}/orders",
    "get_ingredients": f"{BASE_URL}/ingredients",
}

# Статичные тестовые данные
INVALID_INGREDIENT_HASH = {"ingredients": ["invalid_hash_123"]}
EMPTY_INGREDIENTS = {"ingredients": []}
import requests
from data import ENDPOINTS


def get_ingredient_ids():
    """Получает реальные ID ингредиентов из API"""
    response = requests.get(ENDPOINTS["get_ingredients"])
    if response.status_code == 200:
        ingredients = response.json()["data"]
        return [ing["_id"] for ing in ingredients[:2]]
    return []


def delete_user(access_token):
    """Удаляет пользователя через API"""
    if access_token:
        headers = {"Authorization": access_token}
        response = requests.delete(ENDPOINTS["get_user"], headers=headers)
        return response
    return None
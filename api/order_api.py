import allure
import requests
from data import ENDPOINTS


class OrderAPI:

    @staticmethod
    @allure.step("Создать заказ")
    def create_order(ingredients, access_token=None):
        headers = {}
        if access_token:
            headers["Authorization"] = access_token
        return requests.post(ENDPOINTS["create_order"], json=ingredients, headers=headers)

    @staticmethod
    @allure.step("Получить заказы пользователя")
    def get_user_orders(access_token):
        headers = {"Authorization": access_token}
        return requests.get(ENDPOINTS["get_orders"], headers=headers)
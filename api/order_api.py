import requests
import allure


class OrderAPI:
    BASE_URL = "https://stellarburgers.education-services.ru/api"

    @staticmethod
    @allure.step("Отправить запрос на создание заказа")
    def create_order(order_data, access_token=None):
        """Создание заказа"""
        url = f"{OrderAPI.BASE_URL}/orders"
        headers = {}
        if access_token:
            headers["Authorization"] = access_token

        response = requests.post(url, json=order_data, headers=headers)
        return response

    @staticmethod
    @allure.step("Получить список заказов пользователя")
    def get_user_orders(access_token):
        """Получение заказов пользователя"""
        url = f"{OrderAPI.BASE_URL}/orders"
        headers = {"Authorization": access_token}
        response = requests.get(url, headers=headers)
        return response
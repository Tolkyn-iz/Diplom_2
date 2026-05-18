import allure
import requests
from data import ENDPOINTS


class UserAPI:

    @staticmethod
    @allure.step("Создать пользователя")
    def create_user(user_data):
        return requests.post(ENDPOINTS["create_user"], json=user_data)

    @staticmethod
    @allure.step("Логин пользователя")
    def login_user(login_data):
        return requests.post(ENDPOINTS["login_user"], json=login_data)

    @staticmethod
    @allure.step("Выход пользователя")
    def logout_user(refresh_token):
        return requests.post(ENDPOINTS["logout_user"], json={"token": refresh_token})

    @staticmethod
    @allure.step("Обновить токен")
    def refresh_token(refresh_token):
        return requests.post(ENDPOINTS["refresh_token"], json={"token": refresh_token})

    @staticmethod
    @allure.step("Получить данные пользователя")
    def get_user(access_token):
        headers = {"Authorization": access_token}
        return requests.get(ENDPOINTS["get_user"], headers=headers)

    @staticmethod
    @allure.step("Обновить данные пользователя")
    def update_user(access_token, user_data):
        headers = {"Authorization": access_token}
        return requests.patch(ENDPOINTS["update_user"], headers=headers, json=user_data)

    @staticmethod
    @allure.step("Удалить пользователя")
    def delete_user(access_token):
        headers = {"Authorization": access_token}
        return requests.delete(ENDPOINTS["get_user"], headers=headers)
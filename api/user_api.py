import requests
import allure


class UserAPI:
    BASE_URL = "https://stellarburgers.education-services.ru/api"

    @staticmethod
    @allure.step("Отправить запрос на создание пользователя")
    def create_user(user_data):
        """Создание пользователя"""
        url = f"{UserAPI.BASE_URL}/auth/register"
        response = requests.post(url, json=user_data)
        return response

    @staticmethod
    @allure.step("Отправить запрос на авторизацию пользователя")
    def login_user(login_data):
        """Авторизация пользователя"""
        url = f"{UserAPI.BASE_URL}/auth/login"
        response = requests.post(url, json=login_data)
        return response

    @staticmethod
    @allure.step("Получить данные пользователя")
    def get_user(access_token):
        """Получение данных пользователя"""
        url = f"{UserAPI.BASE_URL}/auth/user"
        headers = {"Authorization": access_token}
        response = requests.get(url, headers=headers)
        return response
    
    @staticmethod
    @allure.step("Удалить пользователя (через API)")
    def delete_user(access_token):
        """Удаление пользователя (если API поддерживает)"""
        # Не у всех API есть удаление, поэтому просто заглушка
        pass
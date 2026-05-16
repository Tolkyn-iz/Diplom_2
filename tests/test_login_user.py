import allure
import pytest
from api.user_api import UserAPI


@allure.feature("Логин пользователя")
class TestLoginUser:

    @allure.title("Авторизация существующего пользователя")
    @allure.description("Проверка успешного входа зарегистрированного пользователя")
    def test_login_existing_user(self, unique_user_data):
        # Сначала создаем пользователя
        register_response = UserAPI.create_user(unique_user_data)
        assert register_response.status_code == 200, "Failed to create user"
        
        # Авторизуемся
        login_data = {
            "email": unique_user_data["email"],
            "password": unique_user_data["password"]
        }
        response = UserAPI.login_user(login_data)
        
        assert response.status_code == 200
        assert response.json()["success"] is True
        assert "accessToken" in response.json()
        assert "refreshToken" in response.json()
        assert response.json()["user"]["email"] == unique_user_data["email"]
        assert response.json()["user"]["name"] == unique_user_data["name"]

    @allure.title("Авторизация с неверным email")
    @allure.description("Проверка ошибки при входе с неправильным email")
    def test_login_invalid_email(self, unique_user_data):
        # Создаем пользователя
        register_response = UserAPI.create_user(unique_user_data)
        assert register_response.status_code == 200
        
        # Пытаемся войти с неверным email
        login_data = {
            "email": "wrong_email@test.com",
            "password": unique_user_data["password"]
        }
        response = UserAPI.login_user(login_data)
        
        assert response.status_code == 401
        assert response.json()["success"] is False
        assert response.json()["message"] == "email or password are incorrect"

    @allure.title("Авторизация с неверным паролем")
    @allure.description("Проверка ошибки при входе с неправильным паролем")
    def test_login_invalid_password(self, unique_user_data):
        # Создаем пользователя
        register_response = UserAPI.create_user(unique_user_data)
        assert register_response.status_code == 200
        
        # Пытаемся войти с неверным паролем
        login_data = {
            "email": unique_user_data["email"],
            "password": "wrong_password"
        }
        response = UserAPI.login_user(login_data)
        
        assert response.status_code == 401
        assert response.json()["success"] is False
        assert response.json()["message"] == "email or password are incorrect"

    @allure.title("Авторизация без заполнения полей")
    @allure.description("Проверка ошибки при входе без email и пароля")
    def test_login_empty_fields(self):
        login_data = {
            "email": "",
            "password": ""
        }
        response = UserAPI.login_user(login_data)
        
        assert response.status_code == 401
        assert response.json()["success"] is False
import allure
import pytest
from api.user_api import UserAPI


@allure.feature("Создание пользователя")
class TestCreateUser:

    @allure.title("Создание уникального пользователя")
    @allure.description("Проверка успешного создания нового пользователя")
    def test_create_unique_user(self, unique_user_data):
        response = UserAPI.create_user(unique_user_data)
        
        # Распечатаем ответ для отладки
        print(f"Response status: {response.status_code}")
        print(f"Response body: {response.json()}")
        
        assert response.status_code == 200
        assert response.json()["success"] is True
        assert "accessToken" in response.json()
        assert "refreshToken" in response.json()
        assert response.json()["user"]["email"] == unique_user_data["email"]
        assert response.json()["user"]["name"] == unique_user_data["name"]

    @allure.title("Создание пользователя, который уже зарегистрирован")
    @allure.description("Проверка ошибки при попытке создать существующего пользователя")
    def test_create_existing_user(self, unique_user_data):
        # Сначала создаем пользователя
        response1 = UserAPI.create_user(unique_user_data)
        assert response1.status_code == 200
        
        # Пытаемся создать его же
        response2 = UserAPI.create_user(unique_user_data)
        
        assert response2.status_code == 403
        assert response2.json()["success"] is False
        assert response2.json()["message"] == "User already exists"

    @allure.title("Создание пользователя без обязательных полей")
    @allure.description("Проверка ошибки при создании пользователя без email")
    def test_create_user_without_email(self, unique_user_data):
        user_data = {
            "password": unique_user_data["password"],
            "name": unique_user_data["name"]
        }
        response = UserAPI.create_user(user_data)
        
        assert response.status_code == 403
        assert response.json()["success"] is False
        assert "required fields" in response.json()["message"]

    @allure.title("Создание пользователя без password")
    @allure.description("Проверка ошибки при создании пользователя без пароля")
    def test_create_user_without_password(self, unique_user_data):
        user_data = {
            "email": unique_user_data["email"],
            "name": unique_user_data["name"]
        }
        response = UserAPI.create_user(user_data)
        
        assert response.status_code == 403
        assert response.json()["success"] is False
        assert "required fields" in response.json()["message"]

    @allure.title("Создание пользователя без name")
    @allure.description("Проверка ошибки при создании пользователя без имени")
    def test_create_user_without_name(self, unique_user_data):
        user_data = {
            "email": unique_user_data["email"],
            "password": unique_user_data["password"]
        }
        response = UserAPI.create_user(user_data)
        
        assert response.status_code == 403
        assert response.json()["success"] is False
        assert "required fields" in response.json()["message"]
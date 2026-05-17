import allure
import pytest
from api.user_api import UserAPI


@allure.feature("Пользователи")
class TestCreateUser:

    @allure.title("Создание уникального пользователя")
    def test_create_unique_user(self, unique_user_data):
        response = UserAPI.create_user(unique_user_data)
        assert response.status_code == 200
        assert "accessToken" in response.json()
        assert "refreshToken" in response.json()
        assert response.json()["user"]["email"] == unique_user_data["email"]
        assert response.json()["user"]["name"] == unique_user_data["name"]
        
        # Очистка
        access_token = response.json().get("accessToken")
        UserAPI.delete_user(access_token)

    @allure.title("Создание пользователя с уже существующим email")
    def test_create_existing_user(self, created_user):
        response, user_data = created_user
        second_response = UserAPI.create_user(user_data)
        assert second_response.status_code == 403
        assert second_response.json()["message"] == "User already exists"

    @allure.title("Создание пользователя без обязательного поля")
    @pytest.mark.parametrize("missing_field", ["email", "password", "name"])
    def test_create_user_missing_field(self, unique_user_data, missing_field):
        invalid_data = unique_user_data.copy()
        invalid_data.pop(missing_field)
        response = UserAPI.create_user(invalid_data)
        assert response.status_code == 403
        assert "required" in response.json()["message"].lower()
import allure
from api.user_api import UserAPI


@allure.feature("Авторизация")
class TestLoginUser:

    @allure.title("Логин существующего пользователя")
    def test_login_existing_user(self, created_user):
        response, user_data = created_user
        login_response = UserAPI.login_user({
            "email": user_data["email"],
            "password": user_data["password"]
        })
        assert login_response.status_code == 200
        assert "accessToken" in login_response.json()
        assert "refreshToken" in login_response.json()

    @allure.title("Логин с неверным паролем")
    def test_login_invalid_password(self, created_user):
        response, user_data = created_user
        login_response = UserAPI.login_user({
            "email": user_data["email"],
            "password": "WrongPassword123"
        })
        assert login_response.status_code == 401
        assert login_response.json()["message"] == "email or password are incorrect"

    @allure.title("Логин с несуществующим email")
    def test_login_nonexistent_user(self, unique_user_data):
        login_response = UserAPI.login_user({
            "email": unique_user_data["email"],
            "password": unique_user_data["password"]
        })
        assert login_response.status_code == 401
        assert login_response.json()["message"] == "email or password are incorrect"
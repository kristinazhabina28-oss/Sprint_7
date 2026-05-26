import allure
import pytest

from api_client import CourierApi
from data import Messages
from helpers import generate_random_string


@allure.epic("Sprint 7")
@allure.feature("Courier login")
class TestLoginCourier:
    @allure.title("Courier can log in")
    def test_login_courier_success(self, courier):
        payload, courier_id = courier

        response = CourierApi.login_courier(
            {"login": payload["login"], "password": payload["password"]}
        )

        assert response.status_code == 200
        assert response.json()["id"] == courier_id

    @allure.title("Courier cannot log in without login")
    def test_login_courier_without_login_returns_error(self, courier):
        payload, _ = courier

        response = CourierApi.login_courier({"password": payload["password"]})

        assert response.status_code == 400
        assert response.json()["message"] == Messages.COURIER_LOGIN_NOT_ENOUGH_DATA

    @allure.title("Courier cannot log in with wrong login or password")
    @pytest.mark.parametrize(
        "login_value,password_value",
        [
            ("wrong_login", "valid_password"),
            ("valid_login", "wrong_password"),
        ],
    )
    def test_login_courier_with_wrong_credentials_returns_error(
        self, courier, login_value, password_value
    ):
        payload, _ = courier
        login = generate_random_string() if login_value == "wrong_login" else payload["login"]
        password = (
            generate_random_string()
            if password_value == "wrong_password"
            else payload["password"]
        )

        response = CourierApi.login_courier({"login": login, "password": password})

        assert response.status_code == 404
        assert response.json()["message"] == Messages.COURIER_ACCOUNT_NOT_FOUND

    @allure.title("Nonexistent courier cannot log in")
    def test_login_nonexistent_courier_returns_error(self):
        response = CourierApi.login_courier(
            {"login": generate_random_string(), "password": generate_random_string()}
        )

        assert response.status_code == 404
        assert response.json()["message"] == Messages.COURIER_ACCOUNT_NOT_FOUND


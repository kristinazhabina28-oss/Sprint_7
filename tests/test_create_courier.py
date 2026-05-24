import allure
import pytest

from api_client import CourierApi
from data import Messages
from helpers import delete_courier_by_credentials, generate_courier_payload


@allure.epic("Sprint 7")
@allure.feature("Courier")
class TestCreateCourier:
    @allure.title("Courier can be created")
    def test_create_courier_success(self):
        payload = generate_courier_payload()

        response = CourierApi.create_courier(payload)

        try:
            assert response.status_code == 201
            assert response.json() == {"ok": True}
        finally:
            delete_courier_by_credentials(payload)

    @allure.title("Duplicate courier cannot be created")
    def test_create_duplicate_courier_returns_error(self):
        payload = generate_courier_payload()
        first_response = CourierApi.create_courier(payload)

        try:
            duplicate_response = CourierApi.create_courier(payload)

            assert first_response.status_code == 201
            assert duplicate_response.status_code == 409
            assert Messages.COURIER_LOGIN_ALREADY_EXISTS in duplicate_response.json()["message"]
        finally:
            delete_courier_by_credentials(payload)

    @allure.title("Courier cannot be created without required login or password")
    @pytest.mark.parametrize("missing_field", ["login", "password"])
    def test_create_courier_without_required_field_returns_error(self, missing_field):
        payload = generate_courier_payload()
        payload.pop(missing_field)

        response = CourierApi.create_courier(payload)

        assert response.status_code == 400
        assert response.json()["message"] == Messages.COURIER_CREATE_NOT_ENOUGH_DATA

    @allure.title("Courier cannot be created without firstName")
    @pytest.mark.xfail(
        reason="The API currently creates a courier without firstName although docs mark it required",
        strict=False,
    )
    def test_create_courier_without_first_name_returns_error(self):
        payload = generate_courier_payload()
        payload.pop("firstName")

        response = CourierApi.create_courier(payload)

        try:
            assert response.status_code == 400
            assert response.json()["message"] == Messages.COURIER_CREATE_NOT_ENOUGH_DATA
        finally:
            delete_courier_by_credentials(payload)


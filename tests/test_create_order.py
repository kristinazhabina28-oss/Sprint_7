import allure
import pytest

from api_client import OrderApi
from helpers import cancel_order, generate_order_payload


@allure.epic("Sprint 7")
@allure.feature("Orders")
class TestCreateOrder:
    @allure.title("Order can be created with different color options")
    @pytest.mark.parametrize("color", [["BLACK"], ["GREY"], ["BLACK", "GREY"], None])
    def test_create_order_returns_track(self, color):
        payload = generate_order_payload(color)

        response = OrderApi.create_order(payload)
        track = response.json().get("track")

        try:
            assert response.status_code == 201
            assert isinstance(track, int)
        finally:
            cancel_order(track)


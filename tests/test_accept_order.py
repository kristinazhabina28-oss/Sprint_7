import allure

from api_client import CourierApi, OrderApi
from data import Messages
from helpers import (
    cancel_order,
    delete_courier_by_id,
    finish_order,
    generate_courier_payload,
    get_courier_id,
)


@allure.epic("Sprint 7")
@allure.feature("Accept order")
class TestAcceptOrder:
    @allure.title("Order can be accepted")
    def test_accept_order_success(self, order):
        _, track, order_id = order
        courier_payload = generate_courier_payload()
        CourierApi.create_courier(courier_payload)
        courier_id = get_courier_id(courier_payload)

        response = OrderApi.accept_order(order_id, courier_id)

        try:
            assert response.status_code == 200
            assert response.json() == {"ok": True}
        finally:
            finish_order(order_id)
            cancel_order(track)
            delete_courier_by_id(courier_id)

    @allure.title("Order cannot be accepted without courier id")
    def test_accept_order_without_courier_id_returns_error(self, order):
        _, _, order_id = order

        response = OrderApi.accept_order(order_id)

        assert response.status_code == 400
        assert response.json()["message"] == Messages.ORDER_SEARCH_NOT_ENOUGH_DATA

    @allure.title("Order cannot be accepted with nonexistent courier id")
    def test_accept_order_with_wrong_courier_id_returns_error(self, order):
        _, _, order_id = order

        response = OrderApi.accept_order(order_id, 999999999)

        assert response.status_code == 404
        assert response.json()["message"] == Messages.COURIER_ID_NOT_FOUND

    @allure.title("Order cannot be accepted without order id")
    def test_accept_order_without_order_id_returns_error(self, courier):
        _, courier_id = courier

        response = OrderApi.accept_order(courier_id=courier_id)

        assert response.status_code == 404
        assert Messages.NOT_FOUND in response.json()["message"]

    @allure.title("Order cannot be accepted with nonexistent order id")
    def test_accept_order_with_wrong_order_id_returns_error(self, courier):
        _, courier_id = courier

        response = OrderApi.accept_order(999999999, courier_id)

        assert response.status_code == 404
        assert response.json()["message"] == Messages.ORDER_ID_NOT_FOUND


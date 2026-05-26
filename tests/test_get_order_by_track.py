import allure

from api_client import OrderApi
from data import Messages


@allure.epic("Sprint 7")
@allure.feature("Order by track")
class TestGetOrderByTrack:
    @allure.title("Order can be received by track number")
    def test_get_order_by_track_success(self, order):
        _, track, _ = order

        response = OrderApi.get_order_by_track(track)
        body = response.json()

        assert response.status_code == 200
        assert "order" in body
        assert body["order"]["track"] == track

    @allure.title("Order cannot be received without track number")
    def test_get_order_without_track_returns_error(self):
        response = OrderApi.get_order_by_track()

        assert response.status_code == 400
        assert response.json()["message"] == Messages.ORDER_SEARCH_NOT_ENOUGH_DATA

    @allure.title("Nonexistent order cannot be received by track number")
    def test_get_order_with_wrong_track_returns_error(self):
        response = OrderApi.get_order_by_track(999999999)

        assert response.status_code == 404
        assert response.json()["message"] == Messages.ORDER_NOT_FOUND


import allure

from api_client import OrderApi


@allure.epic("Sprint 7")
@allure.feature("Orders list")
class TestOrdersList:
    @allure.title("Orders list is returned in response body")
    def test_get_orders_returns_orders_list(self):
        response = OrderApi.get_orders({"limit": 10, "page": 0})
        body = response.json()

        assert response.status_code == 200
        assert "orders" in body
        assert isinstance(body["orders"], list)


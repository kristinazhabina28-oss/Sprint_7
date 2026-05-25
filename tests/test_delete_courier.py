import allure

from api_client import CourierApi
from data import Messages


@allure.epic("Sprint 7")
@allure.feature("Delete courier")
class TestDeleteCourier:
    @allure.title("Courier can be deleted")
    def test_delete_courier_success(self, courier):
        _, courier_id = courier

        response = CourierApi.delete_courier(courier_id)

        assert response.status_code == 200
        assert response.json() == {"ok": True}

    @allure.title("Courier cannot be deleted without id")
    def test_delete_courier_without_id_returns_error(self):
        response = CourierApi.delete_courier()

        assert response.status_code == 404
        assert Messages.NOT_FOUND in response.json()["message"]

    @allure.title("Nonexistent courier cannot be deleted")
    def test_delete_nonexistent_courier_returns_error(self):
        response = CourierApi.delete_courier(999999999)

        assert response.status_code == 404
        assert Messages.COURIER_NOT_FOUND in response.json()["message"]

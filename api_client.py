import allure
import requests

from data import REQUEST_TIMEOUT
from urls import Urls


class CourierApi:
    @staticmethod
    @allure.step("Create courier")
    def create_courier(payload):
        return requests.post(Urls.COURIER, json=payload, timeout=REQUEST_TIMEOUT)

    @staticmethod
    @allure.step("Log in courier")
    def login_courier(payload, timeout=REQUEST_TIMEOUT):
        return requests.post(Urls.COURIER_LOGIN, json=payload, timeout=timeout)

    @staticmethod
    @allure.step("Delete courier")
    def delete_courier(courier_id=None):
        url = Urls.COURIER if courier_id is None else f"{Urls.COURIER}/{courier_id}"
        return requests.delete(url, timeout=REQUEST_TIMEOUT)


class OrderApi:
    @staticmethod
    @allure.step("Create order")
    def create_order(payload):
        return requests.post(Urls.ORDERS, json=payload, timeout=REQUEST_TIMEOUT)

    @staticmethod
    @allure.step("Get orders")
    def get_orders(params=None):
        return requests.get(Urls.ORDERS, params=params, timeout=REQUEST_TIMEOUT)

    @staticmethod
    @allure.step("Get order by track")
    def get_order_by_track(track=None):
        params = None if track is None else {"t": track}
        return requests.get(Urls.ORDER_TRACK, params=params, timeout=REQUEST_TIMEOUT)

    @staticmethod
    @allure.step("Cancel order")
    def cancel_order(track):
        return requests.put(Urls.ORDER_CANCEL, params={"track": track}, timeout=REQUEST_TIMEOUT)

    @staticmethod
    @allure.step("Accept order")
    def accept_order(order_id=None, courier_id=None):
        url = Urls.ORDER_ACCEPT if order_id is None else f"{Urls.ORDER_ACCEPT}/{order_id}"
        params = None if courier_id is None else {"courierId": courier_id}
        return requests.put(url, params=params, timeout=REQUEST_TIMEOUT)

    @staticmethod
    @allure.step("Finish order")
    def finish_order(order_id):
        return requests.put(f"{Urls.ORDER_FINISH}/{order_id}", timeout=REQUEST_TIMEOUT)

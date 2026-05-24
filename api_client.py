import requests

from data import REQUEST_TIMEOUT
from urls import Urls


class CourierApi:
    @staticmethod
    def create_courier(payload):
        return requests.post(Urls.COURIER, json=payload, timeout=REQUEST_TIMEOUT)

    @staticmethod
    def login_courier(payload, timeout=REQUEST_TIMEOUT):
        return requests.post(Urls.COURIER_LOGIN, json=payload, timeout=timeout)

    @staticmethod
    def delete_courier(courier_id=None):
        url = Urls.COURIER if courier_id is None else f"{Urls.COURIER}/{courier_id}"
        return requests.delete(url, timeout=REQUEST_TIMEOUT)


class OrderApi:
    @staticmethod
    def create_order(payload):
        return requests.post(Urls.ORDERS, json=payload, timeout=REQUEST_TIMEOUT)

    @staticmethod
    def get_orders(params=None):
        return requests.get(Urls.ORDERS, params=params, timeout=REQUEST_TIMEOUT)

    @staticmethod
    def get_order_by_track(track=None):
        params = None if track is None else {"t": track}
        return requests.get(Urls.ORDER_TRACK, params=params, timeout=REQUEST_TIMEOUT)

    @staticmethod
    def cancel_order(track):
        return requests.put(Urls.ORDER_CANCEL, params={"track": track}, timeout=REQUEST_TIMEOUT)

    @staticmethod
    def accept_order(order_id=None, courier_id=None):
        url = Urls.ORDER_ACCEPT if order_id is None else f"{Urls.ORDER_ACCEPT}/{order_id}"
        params = None if courier_id is None else {"courierId": courier_id}
        return requests.put(url, params=params, timeout=REQUEST_TIMEOUT)

    @staticmethod
    def finish_order(order_id):
        return requests.put(f"{Urls.ORDER_FINISH}/{order_id}", timeout=REQUEST_TIMEOUT)


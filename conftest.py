import time

import pytest

from api_client import CourierApi, OrderApi
from helpers import generate_courier_payload, generate_order_payload


def _get_courier_id(payload):
    response = CourierApi.login_courier(
        {"login": payload["login"], "password": payload["password"]}
    )
    if response.status_code != 200:
        return None

    return response.json().get("id")


def _delete_courier_by_id(courier_id):
    if courier_id is not None:
        CourierApi.delete_courier(courier_id)


def _delete_courier_by_credentials(payload):
    courier_id = _get_courier_id(payload)
    _delete_courier_by_id(courier_id)


def _get_order_id(track):
    if track is None:
        return None

    for _ in range(3):
        response = OrderApi.get_order_by_track(track)
        if response.status_code == 200:
            return response.json().get("order", {}).get("id")
        time.sleep(1)

    return None


def _cancel_order(track):
    if track is not None:
        OrderApi.cancel_order(track)


def _finish_order(order_id):
    if order_id is not None:
        OrderApi.finish_order(order_id)


@pytest.fixture
def courier():
    payload = generate_courier_payload()
    response = CourierApi.create_courier(payload)

    courier_id = _get_courier_id(payload) if response.status_code == 201 else None
    yield payload, courier_id

    _delete_courier_by_id(courier_id)


@pytest.fixture
def order():
    payload = generate_order_payload(["BLACK"])
    response = OrderApi.create_order(payload)

    track = response.json().get("track")
    order_id = _get_order_id(track)
    yield payload, track, order_id

    _cancel_order(track)


@pytest.fixture
def courier_cleaner():
    couriers = []

    yield couriers.append

    for payload in couriers:
        _delete_courier_by_credentials(payload)


@pytest.fixture
def order_cleaner():
    tracks = []

    yield tracks.append

    for track in tracks:
        _cancel_order(track)


@pytest.fixture
def accepted_order_cleaner():
    order_ids = []

    yield order_ids.append

    for order_id in order_ids:
        _finish_order(order_id)

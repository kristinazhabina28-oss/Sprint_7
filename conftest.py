import pytest

from api_client import CourierApi, OrderApi
from helpers import generate_courier_payload, generate_order_payload
from steps import (
    cancel_order,
    delete_courier_by_credentials,
    delete_courier_by_id,
    finish_order,
    get_courier_id,
    get_order_id,
)


@pytest.fixture
def courier():
    payload = generate_courier_payload()
    response = CourierApi.create_courier(payload)

    courier_id = get_courier_id(payload) if response.status_code == 201 else None
    yield payload, courier_id

    delete_courier_by_id(courier_id)


@pytest.fixture
def order():
    payload = generate_order_payload(["BLACK"])
    response = OrderApi.create_order(payload)

    track = response.json().get("track")
    order_id = get_order_id(track)
    yield payload, track, order_id

    cancel_order(track)


@pytest.fixture
def courier_cleaner():
    couriers = []

    yield couriers.append

    for payload in couriers:
        delete_courier_by_credentials(payload)


@pytest.fixture
def order_cleaner():
    tracks = []

    yield tracks.append

    for track in tracks:
        cancel_order(track)


@pytest.fixture
def accepted_order_cleaner():
    order_ids = []

    yield order_ids.append

    for order_id in order_ids:
        finish_order(order_id)

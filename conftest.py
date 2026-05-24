import pytest

from api_client import CourierApi, OrderApi
from helpers import (
    cancel_order,
    delete_courier_by_id,
    generate_courier_payload,
    generate_order_payload,
    get_courier_id,
    get_order_id,
)


@pytest.fixture
def courier():
    payload = generate_courier_payload()
    response = CourierApi.create_courier(payload)
    assert response.status_code == 201

    courier_id = get_courier_id(payload)
    yield payload, courier_id

    delete_courier_by_id(courier_id)


@pytest.fixture
def order():
    payload = generate_order_payload(["BLACK"])
    response = OrderApi.create_order(payload)
    assert response.status_code == 201

    track = response.json().get("track")
    order_id = get_order_id(track)
    yield payload, track, order_id

    cancel_order(track)


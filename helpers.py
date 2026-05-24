import copy
import random
import string

from api_client import CourierApi, OrderApi
from data import DEFAULT_ORDER


def generate_random_string(length=10):
    return "".join(random.choice(string.ascii_lowercase) for _ in range(length))


def generate_courier_payload():
    return {
        "login": generate_random_string(),
        "password": generate_random_string(),
        "firstName": generate_random_string(),
    }


def generate_order_payload(color=None):
    payload = copy.deepcopy(DEFAULT_ORDER)
    payload["firstName"] = f"Test{generate_random_string(6)}"
    payload["lastName"] = f"User{generate_random_string(6)}"

    if color is not None:
        payload["color"] = color

    return payload


def get_courier_id(payload):
    response = CourierApi.login_courier(
        {"login": payload["login"], "password": payload["password"]}
    )
    if response.status_code != 200:
        return None

    return response.json().get("id")


def delete_courier_by_id(courier_id):
    if courier_id is None:
        return None

    try:
        return CourierApi.delete_courier(courier_id)
    except Exception:
        return None


def delete_courier_by_credentials(payload):
    courier_id = get_courier_id(payload)
    return delete_courier_by_id(courier_id)


def get_order_id(track):
    response = OrderApi.get_order_by_track(track)
    if response.status_code != 200:
        return None

    return response.json().get("order", {}).get("id")


def cancel_order(track):
    if track is None:
        return None

    try:
        return OrderApi.cancel_order(track)
    except Exception:
        return None


def finish_order(order_id):
    if order_id is None:
        return None

    try:
        return OrderApi.finish_order(order_id)
    except Exception:
        return None


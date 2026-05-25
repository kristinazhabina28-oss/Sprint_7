import copy
import random
import string

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

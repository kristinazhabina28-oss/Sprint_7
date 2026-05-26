REQUEST_TIMEOUT = 30


class Messages:
    COURIER_CREATE_NOT_ENOUGH_DATA = "Недостаточно данных для создания учетной записи"
    COURIER_LOGIN_ALREADY_EXISTS = "Этот логин уже используется"
    COURIER_LOGIN_NOT_ENOUGH_DATA = "Недостаточно данных для входа"
    COURIER_ACCOUNT_NOT_FOUND = "Учетная запись не найдена"
    COURIER_NOT_FOUND = "Курьера с таким id нет"
    COURIER_ID_NOT_FOUND = "Курьера с таким id не существует"
    ORDER_SEARCH_NOT_ENOUGH_DATA = "Недостаточно данных для поиска"
    ORDER_ID_NOT_FOUND = "Заказа с таким id не существует"
    ORDER_NOT_FOUND = "Заказ не найден"
    NOT_FOUND = "Not Found"


DEFAULT_ORDER = {
    "firstName": "Naruto",
    "lastName": "Uchiha",
    "address": "Konoha, 142 apt.",
    "metroStation": "4",
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2026-06-06",
    "comment": "Saske, come back to Konoha",
}


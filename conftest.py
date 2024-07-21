import random
import string
import pytest
import json

from .client.order_api import OrderApi
from .client.courier_api import CourierApi


@pytest.fixture()
def register_new_courier():
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string
    login_pass = []
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)
    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    response = CourierApi().post_create(payload)
    if response.status_code == 201:
        login_pass.append(login)
        login_pass.append(password)
        login_pass.append(first_name)

    yield login_pass
    payload = {'login': login_pass[0],
               'password': login_pass[1]}

    response = CourierApi().post_login(payload)
    r = response.json()
    id_delete = r['id']
    payload = {'id': id_delete}
    CourierApi().delete(payload)


@pytest.fixture()
def generate_login_pass():
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    login_pass = []
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)
    login_pass.append(login)
    login_pass.append(password)
    login_pass.append(first_name)

    yield login_pass
    payload = {'login': login_pass[0],
               'password': login_pass[1]}
    response = CourierApi().post_login(payload)
    if response.status_code == 200:
        r = response.json()
        id_delete = r['id']
        payload = {'id': id_delete}
        CourierApi().delete(payload)

@pytest.fixture()
def create_order():
    data = {"firstName": "Люба",
            "lastName": "Пол",
            "address": "СПб 12",
            "metroStation": "2",
            "phone": "+79006367303",
            "rentTime": 2,
            "deliveryDate": "2024-07-22T21:00:00.000Z",
            "comment": "",
            "color": []
            }
    payload = json.dumps(data)
    response = OrderApi().post_create(payload)
    r = response.json()
    order_id = r['track']
    yield order_id
    payload = {'track': order_id}
    OrderApi().put_cancel(payload)
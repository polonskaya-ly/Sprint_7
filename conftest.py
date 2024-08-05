import pytest
import json

from .data.data_for_test import TestData
from .helpers import generate_random_string
from .client.order_api import OrderApi
from .client.courier_api import CourierApi


@pytest.fixture()
def generate_data_login_pass():
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
def register_new_courier(generate_data_login_pass):
    payload = {
        "login": generate_data_login_pass[0],
        "password": generate_data_login_pass[1],
        "firstName": generate_data_login_pass[2]
    }
    CourierApi().post_create(payload)


@pytest.fixture(scope='function')
def delete_order():
    payload = {}
    yield payload
    OrderApi().put_cancel(payload)


@pytest.fixture()
def create_order(delete_order):
    data = TestData.DATA_ORDER
    payload = json.dumps(data)
    response = OrderApi().post_create(payload)
    r = response.json()
    order_id = r['track']
    payload = {'track': order_id}
    delete_order.update(payload)

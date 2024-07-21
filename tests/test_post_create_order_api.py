import pytest
from ..client.order_api import OrderApi
import json
import allure


class TestCreateOrder:
    @allure.title('Создание заказа с разными параметрами цвета')
    @pytest.mark.parametrize('color', [["BLACK"], ["GREY"], [], ["BLACK", "GREY"]])
    def test_create_order_with_color_params(self, color):
        data = {"firstName":"Люба",
                "lastName":"Пол",
                "address":"СПб 12",
                "metroStation":"2",
                "phone":"+79006367303",
                "rentTime":2,
                "deliveryDate":"2024-07-22T21:00:00.000Z",
                "comment":"",
                "color": color
                }
        payload = json.dumps(data)
        response = OrderApi().post_create(payload)
        r = response.json()
        assert response.status_code == 201
        assert r['track'] > 0
        order_id = r['track']
        payload = {'track': order_id}
        OrderApi().put_cancel(payload)

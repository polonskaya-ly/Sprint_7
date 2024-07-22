import pytest

from ..data.data_for_test import TestData
from ..client.order_api import OrderApi
import json
import allure


class TestCreateOrder:
    @allure.title('Создание заказа с разными параметрами цвета')
    @pytest.mark.parametrize('color', [["BLACK"], ["GREY"], [], ["BLACK", "GREY"]])
    def test_create_order_with_color_params(self, color, delete_order):
        data = TestData.DATA_ORDER
        data['color'] = color
        payload = json.dumps(data)
        response = OrderApi().post_create(payload)
        r = response.json()
        assert response.status_code == 201
        assert r['track'] > 0
        order_id = r['track']
        payload = {'track': order_id}
        delete_order.update(payload)

import allure

from ..client.order_api import OrderApi

class TestOrderList:
    @allure.title('Получение списка заказов')
    def test_get_order_list(self, create_order):
        response = OrderApi().get_orders()
        r = response.json()
        assert response.status_code == 200
        assert len(r['orders']) > 0

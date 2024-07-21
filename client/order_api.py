import requests
import allure


from ..url_config import  UrlConfig

url = UrlConfig.domain


class OrderApi:
    @allure.step('Отправить запрос на создание заказа')
    def post_create(self, payload):
        response = requests.post(url + UrlConfig.api_create_order, data=payload)
        return response

    @allure.step('Отправить запрос на удаление заказа')
    def put_cancel(self, payload):
        response = requests.put(url + UrlConfig.api_cancel_order, data=payload)
        return response

    @allure.step('Отправить запрос на получение списка заказов')
    def get_orders(self):
        response = requests.get(url + UrlConfig.api_order_list)
        return response
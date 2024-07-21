import requests
import allure

from ..url_config import  UrlConfig

url = UrlConfig.domain


class CourierApi:
    @allure.step('Отправить запрос на авторизацию курьера')
    def post_login(self, payload):
        response = requests.post(url + UrlConfig.api_login, data=payload)
        return response

    @allure.step('Отправить запрос на создание курьера')
    def post_create(self, payload):
        response = requests.post(url + UrlConfig.api_create_courier, data=payload)
        return response

    @allure.step('Отправить запрос на удаление курьера')
    def delete(self, payload):
        response = requests.delete(url + UrlConfig.api_delete_courirer, data=payload)
        return response









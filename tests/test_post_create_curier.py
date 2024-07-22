import allure

from ..data.data_for_assert import AssertData
from ..client.courier_api import CourierApi


class TestCreateCourier:
    @allure.title('Создание курьера со всемми полями')
    def test_create_courier(self, generate_data_login_pass):
        payload = {'login': generate_data_login_pass[0],
                   'password': generate_data_login_pass[1],
                   'firstName': generate_data_login_pass[2]}
        response = CourierApi().post_create(payload)
        assert response.status_code == 201
        assert response.text == AssertData.RESPONSE_TRUE

    @allure.title('Создание курьера без логина')
    def test_create_courier_without_login(self, generate_data_login_pass):
        payload = {'login': '',
                   'password': generate_data_login_pass[1],
                   'firstName': generate_data_login_pass[2]}

        response = CourierApi().post_create(payload)
        r = response.json()
        assert response.status_code == 400
        assert r['message'] == AssertData.REGISTER_NO_REQUIRED_FIELDS

    @allure.title('Создание курьера без пароля')
    def test_create_courier_without_password(self, generate_data_login_pass):
        payload = {'login': generate_data_login_pass[0],
                   'password': '',
                   'firstName': generate_data_login_pass[2]}
        response = CourierApi().post_create(payload)
        r = response.json()
        assert response.status_code == 400
        assert r['message'] == AssertData.REGISTER_NO_REQUIRED_FIELDS

    @allure.title('Создание курьера без имени')
    def test_create_courier_without_firstName(self, generate_data_login_pass):
        payload = {'login': generate_data_login_pass[0],
                   'password': generate_data_login_pass[1],
                   'firstName': ''}
        response = CourierApi().post_create(payload)
        assert response.status_code == 201
        assert response.text == AssertData.RESPONSE_TRUE

    @allure.title('Создание двух одинаковых курьеров')
    def test_create_courier_same_courier(self, generate_data_login_pass, register_new_courier):
        payload = {'login': generate_data_login_pass[0],
                   'password': generate_data_login_pass[1]
                   }
        response = CourierApi().post_create(payload)
        r = response.json()
        assert response.status_code == 409
        assert r['message'] == AssertData.REGISTER_DOUBLE_LOGIN

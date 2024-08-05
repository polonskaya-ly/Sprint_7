import allure
import pytest

from ..data.data_for_assert import AssertData
from ..data.data_for_test import TestData
from ..client.courier_api import CourierApi


@pytest.mark.usefixtures('register_new_courier')
class TestLogin:
    @allure.title('Успешная авторизация курьера')
    def test_login(self, generate_data_login_pass):
        payload = {'login': generate_data_login_pass[0],
                   'password': generate_data_login_pass[1]}
        response = CourierApi().post_login(payload)
        assert response.status_code == 200
        r = response.json()
        assert r['id'] > 0

    @allure.title('Авторизация без логина')
    def test_login_without_login(self, generate_data_login_pass):
        payload = {'login': '', 'password': generate_data_login_pass[1]}
        response = CourierApi().post_login(payload)
        assert response.status_code == 400
        r = response.json()
        assert r['message'] == AssertData.LOGIN_NO_REQUIRED_FIELDS

    @allure.title('Авторизация без пароля')
    def test_login_without_password(self, generate_data_login_pass):
        payload = {'login': generate_data_login_pass[0], 'password': '' }
        response = CourierApi().post_login(payload)
        assert response.status_code == 400
        r = response.json()
        assert r['message'] == AssertData.LOGIN_NO_REQUIRED_FIELDS

    @allure.title('Авторизация с несуществующим логином')
    def test_login_with_fake_login(self, generate_data_login_pass):
        payload = {'login': TestData.FAKE_LOGIN,
                   'password': generate_data_login_pass[1]}
        response = CourierApi().post_login(payload)
        assert response.status_code == 404
        r = response.json()
        assert r['message'] == AssertData.LOGIN_NOT_EXISTED

    @allure.title('Авторизация с некорректным логином')
    def test_login_with_incorrect_login(self, generate_data_login_pass):
        payload = {'login': generate_data_login_pass[0] + 's',
                   'password': generate_data_login_pass[1]}
        response = CourierApi().post_login(payload)
        assert response.status_code == 404
        r = response.json()
        assert r['message'] == AssertData.LOGIN_NOT_EXISTED

    @allure.title('Авторизация с некорректным паролем')
    def test_login_with_incorrect_password(self, generate_data_login_pass):
        payload = {'login': generate_data_login_pass[0],
                   'password': generate_data_login_pass[1] + 's'}
        response = CourierApi().post_login(payload)
        assert response.status_code == 404
        r = response.json()
        assert r['message'] == AssertData.LOGIN_NOT_EXISTED

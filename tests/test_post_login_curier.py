import allure

from ..client.courier_api import CourierApi


class TestLogin:
    @allure.title('Успешная авторизация курьера')
    def test_login(self, register_new_courier):
        payload = {'login': register_new_courier[0],
                   'password': register_new_courier[1]}
        response = CourierApi().post_login(payload)
        assert response.status_code == 200
        r = response.json()
        assert r['id'] > 0

    @allure.title('Авторизация без логина')
    def test_login_without_login(self, register_new_courier):
        payload = {'login': '', 'password': register_new_courier[1]}
        response = CourierApi().post_login(payload)
        assert response.status_code == 400
        r = response.json()
        assert r['message'] == 'Недостаточно данных для входа'

    @allure.title('Авторизация без пароля')
    def test_login_without_password(self, register_new_courier):
        payload = {'login': register_new_courier[0], 'password': '' }
        response = CourierApi().post_login(payload)
        assert response.status_code == 400
        r = response.json()
        assert r['message'] == 'Недостаточно данных для входа'

    @allure.title('Авторизация с несуществующим логином')
    def test_login_with_fake_login(self, register_new_courier):
        payload = {'login': 'Mary3310',
                   'password': register_new_courier[1]}
        response = CourierApi().post_login(payload)
        assert response.status_code == 404
        r = response.json()
        assert r['message'] == 'Учетная запись не найдена'

    @allure.title('Авторизация с некорректным логином')
    def test_login_with_incorrect_login(self, register_new_courier):
        payload = {'login': register_new_courier[0] + 's',
                   'password': register_new_courier[1]}
        response = CourierApi().post_login(payload)
        assert response.status_code == 404
        r = response.json()
        assert r['message'] == 'Учетная запись не найдена'

    @allure.title('Авторизация с некорректным паролем')
    def test_login_with_incorrect_password(self, register_new_courier):
        payload = {'login': register_new_courier[0],
                   'password': register_new_courier[1] + 's'}
        response = CourierApi().post_login(payload)
        assert response.status_code == 404
        r = response.json()
        assert r['message'] == 'Учетная запись не найдена'

import allure
from ..client.courier_api import CourierApi


class TestCreateCourier:
    @allure.title('Создание курьера со всемми полями')
    def test_create_courier(self, generate_login_pass):
        payload = {'login': generate_login_pass[0],
                   'password': generate_login_pass[1],
                   'firstName': generate_login_pass[2]}
        response = CourierApi().post_create(payload)
        assert response.status_code == 201
        assert response.text == '{"ok":true}'

    @allure.title('Создание курьера без логина')
    def test_create_courier_without_login(self, generate_login_pass):
        payload = {'login': '',
                   'password': generate_login_pass[1],
                   'firstName': generate_login_pass[2]}

        response = CourierApi().post_create(payload)
        r = response.json()
        assert response.status_code == 400
        assert r['message'] == "Недостаточно данных для создания учетной записи"

    @allure.title('Создание курьера без пароля')
    def test_create_courier_without_password(self, generate_login_pass):
        payload = {'login': generate_login_pass[0],
                   'password': '',
                   'firstName': generate_login_pass[2]}
        response = CourierApi().post_create(payload)
        r = response.json()
        assert response.status_code == 400
        assert r['message'] == "Недостаточно данных для создания учетной записи"

    @allure.title('Создание курьера без имени')
    def test_create_courier_without_firstName(self, generate_login_pass):
        payload = {'login': generate_login_pass[0],
                   'password': generate_login_pass[1],
                   'firstName': ''}
        response = CourierApi().post_create(payload)
        assert response.status_code == 201
        assert response.text == '{"ok":true}'

    @allure.title('Создание двух одинаковых курьеров')
    def test_create_courier_same_courier(self, register_new_courier):
        payload = {'login': register_new_courier[0],
                   'password': register_new_courier[1]
                   }
        response = CourierApi().post_create(payload)
        r = response.json()
        assert response.status_code == 409
        assert r['message'] == "Этот логин уже используется."

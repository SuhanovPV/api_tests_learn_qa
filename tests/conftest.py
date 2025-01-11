import allure
import pytest
from api_tests_learn_qa.data.data_generator import email_generator
from api_tests_learn_qa.data.user import User
from api_tests_learn_qa.utils import custom_requests


@pytest.fixture(scope='function')
def create_user():
    user = User(
        username='punpkineater',
        firstName='Piter',
        lastName='Griffin',
        email=email_generator(),
        password='2324sdfdfqSD')
    with allure.step(f'Create user {user}'):
        response = custom_requests.post('/user', data=user.get_reg_data())
        assert response.status_code == 200
        user.id = response.json()['id']

    yield user


@pytest.fixture(scope='session')
def create_another_user():
    user = User(
        username='gigity',
        firstName='Glenn',
        lastName='Quagmire',
        email=email_generator(),
        password='23564ysodfqSD')

    with allure.step(f'Create user {user}'):
        response = custom_requests.post('/user', data=user.get_reg_data())
        assert response.status_code == 200
        user.id = response.json()['id']

    yield user


@pytest.fixture(scope='function')
def user_authorization(create_user):
    with allure.step(f'Auth as {create_user}'):
        response_login = custom_requests.post('/user/login', data=create_user.get_credentials())
        assert response_login.status_code == 200

    yield {
        'user': create_user,
        'auth_sid': response_login.cookies.get('auth_sid'),
        'x-csrf-token': response_login.headers.get('x-csrf-token')
    }


@pytest.fixture(scope='session', autouse=True)
def another_user_authorization(create_another_user):
    with allure.step(f'Auth as {create_another_user}'):
        response_login = custom_requests.post('/user/login', data=create_another_user.get_credentials())
        assert response_login.status_code == 200

    yield {
        'user': create_another_user,
        'auth_sid': response_login.cookies.get('auth_sid'),
        'x-csrf-token': response_login.headers.get('x-csrf-token')
    }

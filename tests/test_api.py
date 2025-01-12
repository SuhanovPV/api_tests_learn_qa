import allure
from jsonschema import validate
from api_tests_learn_qa.utils import get_json_schema, custom_requests
from api_tests_learn_qa.data.user import User
from api_tests_learn_qa.data.data_generator import email_generator

@allure.parent_suite('API Tests')
@allure.suite('API methods for User')
@allure.epic('api')
@allure.story('Test api methods for work with user ')
@allure.tag('api', 'user', 'create')
@allure.title('Create user with unique email')
@allure.severity(allure.severity_level.CRITICAL)
def test_create_user():
    user = User('ssuxxarr', 'Pavel', 'Svirin', email_generator(), '1234')
    with allure.step(f'Create new user {user}'):
        response = custom_requests.post('/user', data=user.get_reg_data())

    with allure.step('Verify user created'):
        assert response.status_code == 200
        validate(response.json(), get_json_schema.get_user_register_schema())

@allure.epic('api')
@allure.story('Test api methods for work with user ')
@allure.tag('api', 'user', 'create')
@allure.title('Create user with already used email')
@allure.severity(allure.severity_level.NORMAL)
def test_create_user_with_already_used_email(create_user):
    second_user = User('login_1', 'Johnybek', 'Aliev', create_user.email, '8534')
    with allure.step(f'Create new user {create_user}'):
        response_second_user = custom_requests.post('/user', data=second_user.get_reg_data())
    with allure.step('Verify user didn\'t created'):
        assert response_second_user.status_code == 400
        assert response_second_user.text == f"Users with email '{create_user.email}' already exists"

@allure.epic('api')
@allure.story('Test api methods for work with user ')
@allure.tag('api', 'user', 'auth')
@allure.title('Authorization')
@allure.severity(allure.severity_level.BLOCKER)
def test_user_authorization(create_user):
    with allure.step(f'Login as {create_user}'):
        response_login = custom_requests.post('/user/login', data=create_user.get_credentials())
    with allure.step('Verify user success logged in'):
        assert response_login.status_code == 200
        validate(response_login.json(), get_json_schema.get_user_auth_schema())
        assert 'auth_sid' in response_login.cookies
        assert 'x-csrf-token' in response_login.headers
        assert response_login.json()['user_id'] == int(create_user.id)

@allure.epic('api')
@allure.story('Test api methods for work with user ')
@allure.tag('api', 'user', 'get_info')
@allure.title('Get user info with authorization by same user')
@allure.severity(allure.severity_level.CRITICAL)
def test_get_user_info_with_authorization_by_same_user(user_authorization):
    user = user_authorization['user']
    auth_sid = user_authorization['auth_sid']
    token = user_authorization['x-csrf-token']
    with allure.step('Get user info'):
        response = custom_requests.get(f'/user/{user.id}', headers={'x-csrf-token': token},
                                       cookies={'auth_sid': auth_sid})

    with allure.step('Verify success response with full user info'):
        assert response.status_code
        validate(response.json(), get_json_schema.get_auth_user_info_schema())
        for key in user.get_info():
            assert response.json()[key] == user.get_info()[key]

@allure.epic('api')
@allure.story('Test api methods for work with user ')
@allure.tag('api', 'user', 'get_info')
@allure.title('Get user info with authorization by another user')
@allure.severity(allure.severity_level.MINOR)
def test_get_user_info_with_authorization_by_another_user(create_user, another_user_authorization):
    auth_sid = another_user_authorization['auth_sid']
    token = another_user_authorization['x-csrf-token']

    user = create_user

    with allure.step(f'Get user {user} info logged as {another_user_authorization['user']}'):
        user_info_response = custom_requests.get(f'/user/{user.id}', headers={'x-csrf-token': token},
                                                 cookies={'auth_sid': auth_sid})

    with allure.step('Verify response data'):
        assert user_info_response.status_code == 200
        validate(user_info_response.json(), get_json_schema.get_not_auth_user_info_schema())
        assert user_info_response.json()['username'] == user.username

@allure.epic('api')
@allure.story('Test api methods for work with user ')
@allure.tag('api', 'user', 'modify')
@allure.title('Modify user data with authorization by same user')
@allure.severity(allure.severity_level.CRITICAL)
def test_modify_user_data_with_authorization_by_same_user(user_authorization):
    user = user_authorization['user']
    auth_sid = user_authorization['auth_sid']
    token = user_authorization['x-csrf-token']

    user.username = 'biba'
    user.email = 'new_' + user.email
    with allure.step('Requeset to modify username and email'):
        user_update_response = custom_requests.put(f'/user/{user.id}',
                                                   data={'username': user.username, 'email': user.email},
                                                   headers={'x-csrf-token': token}, cookies={'auth_sid': auth_sid})

    with allure.step('Verify request completed successfully'):
        assert user_update_response.status_code == 200
        validate(user_update_response.json(), get_json_schema.get_success_schema())

    with allure.step('Get updated user information'):
        user_info_response = custom_requests.get(f'/user/{user.id}', headers={'x-csrf-token': token},
                                                 cookies={'auth_sid': auth_sid})
        assert user_info_response.status_code == 200
        validate(user_info_response.json(), get_json_schema.get_auth_user_info_schema())

    with allure.step('Check username and email was changed'):
        assert user_info_response.json()['email'] == user.get_info()['email']
        assert user_info_response.json()['username'] == user.get_info()['username']

@allure.epic('api')
@allure.story('Test api methods for work with user ')
@allure.tag('api', 'user', 'modify')
@allure.title('Modify user data with authorization by another user')
@allure.severity(allure.severity_level.MINOR)
def test_modify_user_data_with_authorization_by_another_user(user_authorization, another_user_authorization):
    another_user_auth_sid = another_user_authorization['auth_sid']
    another_user_token = another_user_authorization['x-csrf-token']

    user = user_authorization['user']
    user_auth_sid = user_authorization['auth_sid']
    user_token = user_authorization['x-csrf-token']

    with allure.step(f'Modify user {user} logged as {another_user_authorization["user"].id}'):
        user_update_response = custom_requests.put(f'/user/{user.id}', data={'username': 'new_name'},
                                                   headers={'x-csrf-token': another_user_token},
                                                   cookies={'auth_sid': another_user_auth_sid})

    with allure.step('Verify request failed with error'):
        assert user_update_response.status_code == 400
        validate(user_update_response.json(), get_json_schema.get_failed_schema())
        assert user_update_response.json()['error'] == 'This user can only edit their own data.'

    with allure.step(f'Confirm user {user} didn\'t changed'):
        user_info_response = custom_requests.get(f'/user/{user.id}', headers={'x-csrf-token': user_token},
                                                 cookies={'auth_sid': user_auth_sid})

        assert user_info_response.status_code == 200
        user.id = user_info_response.json()['id']
        for key in user.get_info():
            assert user_info_response.json()[key] == user.get_info()[key]

@allure.epic('api')
@allure.story('Test api methods for work with user ')
@allure.tag('api', 'user', 'delete')
@allure.title('Delete user with authorization by same user')
@allure.severity(allure.severity_level.NORMAL)
def test_delete_user_with_authorization_by_same_user(user_authorization):
    user = user_authorization['user']
    auth_sid = user_authorization['auth_sid']
    token = user_authorization['x-csrf-token']

    with allure.step(f'Delete user {user}'):
        user_delete_response = custom_requests.delete(f'/user/{user.id}', headers={'x-csrf-token': token},
                                                      cookies={'auth_sid': auth_sid})
    with allure.step('Verify request completed successfully'):
        assert user_delete_response.status_code == 200
        validate(user_delete_response.json(), get_json_schema.get_success_schema())
    with allure.step(f'Check there is no user was deleted'):
        get_user_response = custom_requests.get(f'/user/{user.id}')
        assert get_user_response.status_code == 404

@allure.epic('api')
@allure.story('Test api methods for work with user ')
@allure.tag('api', 'user', 'delete')
@allure.title('Delete user with authorization by another user')
@allure.severity(allure.severity_level.NORMAL)
def test_delete_user_with_authorization_by_another_user(create_user, another_user_authorization):
    another_user_auth_sid = another_user_authorization['auth_sid']
    another_user_token = another_user_authorization['x-csrf-token']

    user = create_user
    with allure.step(f'Delete user {user} logged in as {another_user_authorization['user']}'):
        user_delete_response = custom_requests.delete(f'/user/{user.id}',
                                                      headers={'x-csrf-token': another_user_token},
                                                      cookies={'auth_sid': another_user_auth_sid})

    with allure.step('Verify request failed with error'):
        assert user_delete_response.status_code == 400
        validate(user_delete_response.json(), get_json_schema.get_failed_schema())
        assert user_delete_response.json()['error'] == 'This user can only delete their own account.'

    with allure.step(f'Check user {user.id} exists'):
        get_user_response = custom_requests.get(f'/user/{user.id}')
        assert get_user_response.status_code == 200

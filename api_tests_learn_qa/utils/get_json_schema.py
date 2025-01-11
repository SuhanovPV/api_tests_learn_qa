import json
import os

import api_tests_learn_qa

SCHEMA_DIR = os.path.abspath(os.path.join(os.path.dirname(api_tests_learn_qa.__file__), 'schemas'))


def get_schema(file_name):
    with open(os.path.join(SCHEMA_DIR, file_name)) as file:
        return json.loads(file.read())


def get_user_register_schema():
    return get_schema('user_register_schema.json')

def get_user_auth_schema():
    return get_schema('user_auth_schema.json')

def get_auth_user_info_schema():
    return get_schema('auth_user_info_schema.json')

def get_not_auth_user_info_schema():
    return get_schema('not_auth_user_info_schema.json')

def get_success_schema():
    return  get_schema('success_schema.json')

def get_failed_schema():
    return  get_schema('failed_schema.json')

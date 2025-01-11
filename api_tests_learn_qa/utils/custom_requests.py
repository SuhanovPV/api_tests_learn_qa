import requests

from config import base_url
from api_tests_learn_qa.utils.custom_logger import request_logging


def url_join(endpoint):
    return f'{base_url}/api{endpoint}'


def get(endpoint, **kwargs):
    response = requests.get(url_join(endpoint), **kwargs)
    request_logging(response, kwargs.get('cookies'))
    return response


def post(endpoint, **kwargs):
    response = requests.post(url_join(endpoint), **kwargs)
    request_logging(response, kwargs.get('cookies'))
    return response


def put(endpoint, **kwargs):
    response = requests.put(url_join(endpoint), **kwargs)
    request_logging(response, kwargs.get('cookies'))
    return response


def delete(endpoint, **kwargs):
    response = requests.delete(url_join(endpoint), **kwargs)
    request_logging(response, kwargs.get('cookies'))
    return response

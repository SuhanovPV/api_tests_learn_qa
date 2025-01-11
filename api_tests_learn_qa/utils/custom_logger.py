import logging


def request_logging(response, cookies):
    logging.info(f'{response.request.method}: {response.request.url}')
    logging.info(f'Request headers: {response.request.headers}')
    logging.info(f'Request cookies: {cookies}')
    logging.info(f'Request payload: {response.request.body}')
    logging.info(f'Response status code: {response.status_code}')
    logging.info(f'Response headers: {response.headers}')
    logging.info(f'Response cookies: {dict(response.cookies)}')

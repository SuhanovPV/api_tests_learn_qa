from datetime import datetime


def email_generator() -> str:
    login_part = f'test{datetime.now().strftime("%Y%m%d%H%M%S")}'
    domain = 'test.su'
    return f'{login_part}@{domain}'

# создать тип Email, и проверку, что адрес содержит @.
# написать функцию send_email, которая принимает валидный Email
from typing import NewType
from email_validator import validate_email as validate_email_
from email_validator import EmailNotValidError

Email = NewType('Email', str)


def validate_email(email: str) -> Email:
    try:
        validate_email_(email, check_deliverability=False)
        return Email(email)
    except EmailNotValidError:
        raise ValueError(f"{email=} is not valid")

def send_email(email: Email) -> None:
    print(f'Sending email to {email}')


if __name__ == "__main__":
    send_email(validate_email("user@example.com"))  # ОК
    send_email("user@example.com")  # mypy должен ругаться на строку, но в runtime все ОК
    send_email("user-example.com")  # mypy должен ругаться на строку, но в runtime все ОК
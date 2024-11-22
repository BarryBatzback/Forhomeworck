
import re
from email.policy import default


def send_email(message, rec, sender="university.help@gmail.com" ):

    from email.utils import parseaddr

    email_regex = re.compile((r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"))

    rec1 = rec
    is_valid = email_regex.fullmatch(rec1)
    parsed_email = parseaddr(rec1)[1]

    if rec == sender:
        print('Невозможно отправить письмо самому себе')
    elif is_valid is None:
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {rec}")
    elif is_valid is not None and parsed_email == rec1 and sender != "university.help@gmail.com":
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {rec}.")
    elif is_valid is not None and parsed_email == rec1:
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {rec}.")



send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')

send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')

send_email('Пожалуйста, исправьте задание', 'urban.student@mailru', sender='urban.teacher@mail.uk')

send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
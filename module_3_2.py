def send_email(message, recipient, sender="university.help@gmail.com"):
    a = [recipient[-4:], recipient[-3:], recipient[-4:], sender[-4:], sender[-3:], sender[-4:]]
    b = ['.com', '.ru', '.net', '.com', '.ru', '.net']
    q = 0
    for i in range(6):
        if a[i] == b[i]:
            q = q + 1
    if '@' not in recipient or '@' not in sender:
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient} ")
    elif q != 2:
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient} ")
    elif sender == recipient:
        print('Нельзя отправить письмо самому себе!')
    elif sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")


send_email('Здравствуйте какая у меня оценка за задание', "sasha.sapegin.99@gmail.ru")
send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')






# recipient='sasha.sapegin.99@gmail.ru'
# sender="university.help@gmail.com"
# a = [recipient[-4:], recipient[-3:], recipient[-4:], sender[-4:], sender[-3:], sender[-4:]]
# b = ['.com', '.ru', '.net', '.com', '.ru', '.net']
# q = 0
# for i in range(6):
#     if a[i] == b[i]:
#         q = q + 1
# if q!=2:
#     print(f"2 Невозможно отправить письмо с адреса {sender} на адрес {recipient} ")
# else:
#     print("Yes")

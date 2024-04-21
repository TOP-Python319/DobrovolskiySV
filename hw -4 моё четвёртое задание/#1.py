
email = input('Введите адрес алектронной почты: ')
if '@' in email and '.' in email:
    print('Да')
else:
    print('Нет')

# Введите адрес алектронной почты: spartakmv@mailru
# Нет
# Введите адрес алектронной почты: spartakkmvgmailcom
# Нет
# Введите адрес алектронной почты: spartakmv@yandex.ru
# Да

# Решение с урока

email = input()

if email.count('@') != 1:
    result ='Нет'
else:
    # Разбиваем строку на части по символу '@'
    name_email, domain = email.split('@')
    if domain.count('.') != 1:
        result = 'Нет'
    else:
        if domain[-1] == '.' or domain[0] == '.':
            result = 'Нет'
        else:
            result = 'Да'
print(result)           

# kivi@mail.ru
# Да
# spartakmvmail.ru
# Нет


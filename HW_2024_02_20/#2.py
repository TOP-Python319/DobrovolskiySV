
num = int(input('Введите желаемое колличество цифр:'))
sum = 0
for _ in range(num):
    n = int(input('Введите Ваши числа:'))
    if n > 0:
        sum += n
        print(f'Сумма введёных только положительных чисел : {sum}')
    else :
        sum <= 0
        print('Нет положительных чисел.')

# Введите желаемое колличество цифр:4
# Введите Ваши числа:0
# Введите Ваши числа:-6
# Введите Ваши числа:-2
# Введите Ваши числа:8
# Сумма введёных только положительных чисел 8   


# Комментарий преподавателя:
# Всё верно! =)

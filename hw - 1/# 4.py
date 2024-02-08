num = int(input('Введите трёхзначное число: '))
digit1 = num // 100
digit2 = num % 100 // 10
digit3 = num % 10

print('Сумма цыфр =',digit1 + digit2 + digit3,',', 'Произведение цифр =', digit1 * digit2 * digit3)



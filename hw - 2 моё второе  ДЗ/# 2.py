
divisible = int(input('Введите число - делимое: '))
divider = int(input('Введите число - делитель: '))
if divisible % divider == 0:
    result = divisible / divider
    print(f'{divisible} делится начело на {divider}')
    print(f'частное - {result}')
else:
    divisible % divider != 0
    result = divisible // divider
    print(f'{divisible} не делится начело на {divider}')
    print(f'частное - {result}')
    print(f'остаток - {divisible % divider}')

#  Введите число - делимое: 16
#  Введите число - делитель: 4
#  16 делится начело на 4
#  частное - 4.0

#  Введите число - делимое: 3
#  Введите число - делитель: 5
#  3 не делится начело на 5
#  частное - 0
#  остаток - 3







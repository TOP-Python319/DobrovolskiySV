num = int(input('\nВведите число кратное семи:'))
d = []
while num % 7 == 0:
    d += [str(num)]
    num = int(input('\nВведите число кратное семи:'))
else:
   # print(*d.reverse,sep=' ')
    print(*d[::-1],sep=' ')

# Введите число кратное семи:7
# Введите число кратное семи:14
# Введите число кратное семи:14
# Введите число кратное семи:21
# Введите число кратное семи:9
# 21 14 14 7
    

# Комментарий прпеподавателя:
# можно заменить строку: d += [str(num)] на d.append(str(num)) - это более python'овский способ добавления элемента в список

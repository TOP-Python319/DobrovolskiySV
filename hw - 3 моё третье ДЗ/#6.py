
number_ticket = input('Введите номер билета:')  

if sum(int(i) for i in number_ticket[0:3]) == sum(int(i) for i in number_ticket[3:6]):

#half_1 = sum(int(i) for i in number_ticket[:3])  # а можно так, по сути тоже самое
#half_2 = sum(int(i) for i in number_ticket[3:])
#if half_1 == half_2:
    print('Вам достался счастливый билетик')
else:
    print('Нет, не в этот раз')

# Введите номер билета:567765
# Вам достался счастливый билетик
# Введите номер билета:456890
# Нет, не в этот раз



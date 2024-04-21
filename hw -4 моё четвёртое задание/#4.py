dict = {}
while True:
    user_input = input("введите данные: ")
    if not user_input :
        break
    else :
        key, value = user_input.split()
        dict[key] = value
 
error_descr = input('введите проверочные данные: ')
 
try :
    key = next(key for key, value in dict.items() if value == error_descr)
 
except StopIteration :
    key = '! value error !'
print(key)

# введите данные: 1970 Спартак
# введите данные: 1982 Стас
# введите данные: 1993 Андрей
# введите данные: 2000 Семён
# введите данные: 2004 Матвей
# введите данные: 
# введите проверочные данные: Андрей
# 1993

# введите данные: 1970 Спартак
# введите данные: 1982 Стас
# введите данные: 1993 Андрей
# введите данные: 2000 Семён
# введите данные: 
# введите проверочные данные: Матвей
# ! value error !



#fruit = input('Введите название фрукта: ')
#mix = []
#while fruit != '':
#    
#    fruit == input('Введите название ещё одного фрукта: ')
#    if len(mix) == 1:
#        mix += [fruit]
#        print(''.join(mix))
#    else:
#        print(', '.join(mix[0:-1]) + ' и ' + mix[-1])
   


fruits =[]
while True:
    new_fruit = input('Введите назввание фрукта:')
    if new_fruit:
        fruits.append(new_fruit)
    else:
        break

    if len(fruits) == 1:
        print(fruits[0])
    else:
        result = ','.join(fruits[:-1]) +  ' и ' + fruits[-1]
        print(result)


# Введите назввание фрукта:киви
# киви
# Введите назввание фрукта:манго
# киви и манго
# Введите назввание фрукта:слива
# киви,манго и слива
# Введите назввание фрукта:ананас
# киви,манго,слива и ананас










king_move1 = input('Введите название клетки:')
king_move2 = input('Введите название другой клетки:')
x = ord(king_move1[0])
y = ord(king_move2[0])
x1 = int(king_move1[1])
y1 = int(king_move2[1])
if abs(x -y) <= 1 and abs(x1 - y1) <= 1:
    print('Да')
else:
    print('Нет')

# Введите название клетки:d4
# Введите название другой клетки:c3
# Да   

# Введите название клетки:b4
# ведите название другой клетки:h7
# Нет    
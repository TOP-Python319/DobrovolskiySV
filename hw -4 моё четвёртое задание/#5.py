scores_letters = {
    1: 'АВЕИНОРСТ',
    2: 'ДКЛМПУ',
    3: 'БГЬЯ',
    4: 'ЙЫ',
    5: 'ЖЗХЦЧ',
    8: 'ФШЭЮ',
    10: 'Щ',
    15: 'Ъ'
}

def callculation_score(word):
    count = 0
    for letter in word.upper():
        for key, value in scores_letters.items():
            if letter in value:
                count += key
    return count
 
word = input().replace('Ё', 'Е')
print(callculation_score(word))

# синхрофазотрон
# 29

# жзхцч
# 25

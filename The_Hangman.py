import random

dic = ['год', 'человек','время','дело',    'жизнь',    'день',    'рука',    'раз','работа',    'слово',    'место',    'лицо',    'друг',    'глаз',    'вопрос',    'дом','сторона',    'страна',    'мир','случай',    'голова',    'ребенок',    'сила']

word = list(random.choice(dic))
word2 = list('-' * len(word))
c, s = 0, 'Эти буквы ты уже пробовал: '

print('Какое слово я загадал?')
print(*word2)
print('Гадай по буквам=)')

while word != list('-' * len(word)):
    letter = input()
    s += letter.upper()
    print(s)
    if letter in word:
        while letter in word:
            word2[word.index(letter)] = letter.upper()
            word[word.index(letter)] = '-'
        print(*word2)
    else:
        c += 1
        if c == 1: print('''
 O ''') 
        
        if c == 2: print('''
 O 
 |''')
        if c == 3: print('''
 O 
/|''')
        if c == 4: print('''
 O 
/|\ ''')
        if c == 5: print('''
 O 
/|\ 
/''')
        if c == 6: 
            print('''
 O 
/|\ 
/ \ 
Ты проиграл=)''')
            break
else:
    print('Ты победил, поздравляю!')

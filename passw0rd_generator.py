from random import *

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = lowercase_letters.upper()
punctuation = '!#$%&*+-=?@^_'
p = 'il1Lo0O'
x = []
m = ['да', 'нет', 'lf', 'ytn', 'yes', 'no', 'y', 'n']
def answers(z):
    while z.lower() not in m:
        z = input('я не понял ответ, давай попробуем еще раз, да или нет? ')
    if z.lower() == 'lf' or z.lower() == 'да' or z.lower() == 'yes' or z.lower() == 'y':
        x.append(1)
    elif z.lower() == 'ytn' or z.lower() == 'нет' or z.lower() == 'no' or z.lower() == 'n':
        x.append(0)


def questions():
    global a, b, c, d, e, f, g, z
    a = input('Сколько паролей необходимо сгенерировать? ')
    while a.isdigit() == False:
        a = input('Сколько паролей необходимо сгенерировать? ')
    b = input('Сколько символов должна быть длина паролей? ')
    while b.isdigit() == False:
        b = input('Сколько символов должна быть длина паролей? ')
    c = input('Включать ли цифры 0123456789 ? ')
    z = c
    answers(c)
    d = input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ ? ')
    z = d
    answers(z)
    e = input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz ? ')
    z = e
    answers(e)
    f = input('Включать ли символы !#$%&*+-=?@^_ ? ')
    z = f
    answers(f)
    g = input('Исключить ли символы il1Lo0O ? ')
    z = g
    answers(g)


print('Привет, Хочешь сгенерировать пароль? только не забудь его потом!')
questions()
y = []
if x[0] == 1:
    y.extend(digits)
if x[1] == 1:
    y.extend(uppercase_letters)
if x[2] == 1:
    y.extend(lowercase_letters)
if x[3] == 1:
    y.extend(punctuation)
if x[4] == 1:
    for i in range(len(p)):
        y.remove(p[i])
for i in range(int(a)):
    for j in range(int(b)):
        print(choice(y), end = '')
    print()

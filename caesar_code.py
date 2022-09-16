eng_lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
eng_upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
rus_lower_alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
rus_upper_alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
symbol = [" ", ",", ".", "!", "?"]

lan = input("Выберите язык: aнгл=e, рус=r:")
chif = input("Выберите шифрование: шифрование - ch, дешифрование - def:")
n = int(input("Введите ключ шифрования, цифру:"))
f = input("Введите фразу:")

def chru(chifr, n, l, fraza):
    if l == 'r':
        moch = 32
    if l == 'e':
        moch = 26
    if chifr== 'def':
        n = -n
    for i in range(len(fraza)):
        if fraza[i].isalpha():
            if fraza[i] == fraza[i].upper():
                for j in range (moch):
                    if moch == 32:
                        if fraza[i] == rus_upper_alphabet[j]:
                            print(rus_upper_alphabet[(j+n)%moch], end = '')
                            break
                    if moch == 26:
                        if fraza[i] == eng_upper_alphabet[j]:
                            print(eng_upper_alphabet[(j+n)%moch], end = '')
                            break
            elif fraza[i] ==fraza[i].lower():
                for j in range (moch):
                    if moch == 32:
                        if fraza[i] == rus_lower_alphabet[j]:
                           print(rus_lower_alphabet[(j+n)%moch], end='')
                           break
                    if moch == 26:
                        if fraza[i] == eng_lower_alphabet[j]:
                           print(eng_lower_alphabet[(j+n)%moch], end = '')
                           break
        else:
            print(fraza[i], end='')

chru(chif, n, lan, f)

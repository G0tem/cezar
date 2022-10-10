print('Программа шифровки / дешифровки текста по методу Цезаря')
k = int(input('Введите шаг сдвига для шифровки ( >0 ) или дешифровки ( <0 )\n'))
en_alphabet = [chr(i) for i in range(65, 91)] + [chr(j) for j in range(97, 123)]
ru_alphabet = [chr(i) for i in range(1040, 1104)]
def cezar(text):
    resul = list()
    if text[0] in en_alphabet:
        alphabet = en_alphabet
        moch = 26
    else:
        alphabet = ru_alphabet
        moch = 32
    for i in range(len(text)):
        if text[i].isalpha():
            if text[i].isupper():
                resul.append(alphabet[(alphabet.index(text[i]) + k) % moch])
            else:
                resul.append(alphabet[(alphabet.index(text[i]) + k) % moch + moch])
        else:
            resul.append(text[i])
    return resul
text = input('Введите текст ')
print(*cezar(text), sep = '')
import string

print('Выберете язык шифруемой фразы [en/ru]')
language = input()
print('Выберете смещение[+int/-int]')
shift = int(input())
print('Напишите фразу')
text = input()

def shifr_programm(language, text, shift):
    punctuation = string.punctuation + ' '
    shifr_text = ''
    alphabet = ''
    if language == 'ru':
        alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    elif language == 'en':
        alphabet = string.ascii_lowercase

    for let in text:
        index = alphabet.find(let.lower())
        if (index + shift) < len(alphabet):
            index = index + shift
        else:
            index = index + shift - len(alphabet)
        print(index, shift)
        if let.isupper():
            shifr_text += alphabet[index].upper()
        elif let in punctuation:
            shifr_text += let
        else:
            shifr_text += alphabet[index]

    return shifr_text


print(shifr_programm(language, text, shift))
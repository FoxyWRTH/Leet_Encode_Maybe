"""
Основной файл.
"""
import random
import string

from Resources.letters_database import all_letters


def combine_letters(some_text, switch=True, upper=False):
    result = ''
    if switch:
        for i in some_text.lower():
            result += random.choice(all_letters.get(i)[0])
    else:
        for i in some_text:
            if i in string.punctuation or i == ' ':
                result += all_letters.get(i)
            elif i == i.upper():
                result += str(all_letters.get(i.lower())[1][1])
            elif i != i.upper():
                result += str(all_letters.get(i.lower())[1][0])
            else:
                print('Чего бля?')
    if upper:
        return result.upper()
    return result


def user_interaction():
    while True:
        input_text = input('Что ж, пиши что нужно перекомбинировать.\n')
        if input_text == 'end':
            return 'Пока что хватит'
        if input_text:
            result = combine_letters(input_text)
            print(f'Вот тебе результат: {result}\n'
                  f'Доволен?')


if __name__ == '__main__':
    print(user_interaction())

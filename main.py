"""
Основной файл.
"""
import random
import string

from Resources.letters_database import all_letters


def combine_letters(some_text, flag=True, upper=False):
    result = ''
    if flag:
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


if __name__ == '__main__':
    print()
    print(combine_letters('Ваше мнение говно ебаное, админы - пидорасы, '
                          'ваш фильтр против мата - хуита'))
    print()
    print(combine_letters('Съешь ещё этих мягких французских булок да выпей чаю, '
                          'можешь добавить себе сахара по вкусу.'))
    print()
    print(combine_letters('Eat some more of these soft French rolls and drink some tea,'
                          ' you can add sugar to your taste.'))
    print()
    print(combine_letters('Александр Владимирович!', False, True))

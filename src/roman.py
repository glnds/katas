import collections


def convert(number):
    roman_letters = {9: 'IX', 40: 'XL', 10: 'X',
                     90: 'XC', 5: 'V', 4: 'IV', 1: 'I'}

    sorted_dict = collections.OrderedDict(
        sorted(roman_letters.items(), reverse=True))

    for key, value in sorted_dict.items():
        if number >= key:
            return value + convert(number - key)

    return ''

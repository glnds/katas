import pytest
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


@pytest.mark.parametrize(
    'arabic, roman', [
        (1, 'I'),
        (2, 'II'),
        (3, 'III'),
        (4, 'IV'),
        (5, 'V'),
        (6, 'VI'),
        (7, 'VII'),
        (8, 'VIII'),
        (9, 'IX'),
        (10, 'X'),
        (11, 'XI'),
        (14, 'XIV'),
        (19, 'XIX'),
        (20, 'XX'),
        (39, 'XXXIX'),
        (40, 'XL'),
        (41, 'XLI'),
        (42, 'XLII'),
        (90, 'XC'),
        (99, 'XCIX'),
    ]
)
def test_roman(arabic, roman):
    assert convert(arabic) == roman

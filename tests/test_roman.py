import pytest
from roman import convert


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
    ]
)
def test_roman_1_to_10(arabic, roman):
    assert convert(arabic) == roman


@pytest.mark.parametrize(
    'arabic, roman', [
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
def test_roman_11_to_99(arabic, roman):
    assert convert(arabic) == roman

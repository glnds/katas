import pytest
from fizzbuzz import fizzbuzz


@pytest.mark.parametrize(
    'some_number, output', [
        (1, 1),
        (2, 2),
        (3, 'fizz'),
        (4, 4),
        (5, 'buzz'),
        (6, 'fizz'),
        (7, 'bar'),
        (8, 8),
        (9, 'fizz'),
        (10, 'buzz'),
    ]
)
def test_fizzbuzz_1_to_10(some_number, output):
    assert fizzbuzz(some_number) == output


@pytest.mark.parametrize(
    'some_number, output', [
        (3*5, 'fizzbuzz'),
        (3*7, 'fizzbar'),
        (5*7, 'buzzbar'),
        (3*5*7, 'fizzbuzzbar'),
    ]
)
def test_fizzbuzz_contenated_words(some_number, output):
    assert fizzbuzz(some_number) == output

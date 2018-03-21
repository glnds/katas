def fizzbuzz(some_value):
    result = ''
    if some_value % 3 == 0:
        result = 'fizz'
    if some_value % 5 == 0:
        result += 'buzz'
    if some_value % 7 == 0:
        result += 'bar'

    if not result:
        return some_value

    return result


def test_fizzbuzz_1():
    assert fizzbuzz(1) == 1


def test_fizzbuzz_2():
    assert fizzbuzz(2) == 2


def test_fizzbuzz_3():
    assert fizzbuzz(3) == 'fizz'


def test_fizzbuzz_4():
    assert fizzbuzz(4) == 4


def test_fizzbuzz_5():
    assert fizzbuzz(5) == 'buzz'


def test_fizzbuzz_6():
    assert fizzbuzz(6) == 'fizz'


def test_fizzbuzz_7():
    assert fizzbuzz(7) == 'bar'


def test_fizzbuzz_8_to_9():
    assert fizzbuzz(8) == 8
    assert fizzbuzz(9) == 'fizz'


def test_fizzbuzz_10():
    assert fizzbuzz(10) == 'buzz'


def test_fizzbuzz_15():
    assert fizzbuzz(15) == 'fizzbuzz'


def test_fizzbuzz_21():
    assert fizzbuzz(21) == 'fizzbar'


def test_fizzbuzz_35():
    assert fizzbuzz(35) == 'buzzbar'


def test_fizzbuzz_3_x_5_x_7():
    assert fizzbuzz(3*5*7) == 'fizzbuzzbar'

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

def soma(x, y):
    '''
    Soma x e y

    >>> soma(10, 20)
    30

    >>> soma('10', 20)
    Traceback (most recent call last):
    ...
    AssertionError: X precisa ser int ou float

    >>> soma(10, '20')
    Traceback (most recent call last):
    ...
    AssertionError: Y precisa ser int ou float
    '''
    assert isinstance(x, (int | float)), 'X precisa ser int ou float'
    assert isinstance(y, (int | float)), 'Y precisa ser int ou float'
    return x + y


def subtrai(x, y):
    '''
    >>> subtrai(-10, -20)
    -30
    '''
    assert isinstance(x, (int | float)), 'X precisa ser int ou float'
    assert isinstance(y, (int | float)), 'Y precisa ser int ou float'
    return x - y


if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True)

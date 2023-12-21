"""
1- Receber um numero inteiro
2- Saber se o numero é multiplo de 3 e 5:
   baconeggs
3- Saber se o numero e multiplo somente de 3:
   bacon
4- Saber se o numero e multiplo somente de 5:
   eggs
5- Saber se o numero NAO e multiplo nem de 3 nem de 5:
   passa fome
"""


def bacon_eggs(num):
    assert isinstance(num, (int)), f'{num} precisa ser inteiro'
    if num % 3 == 0 and num % 5 == 0:
        return 'baconeggs'

    elif num % 3 == 0 or num % 5 == 0:
        if num % 3 == 0:
            return 'bacon'
        return 'eggs'

    return 'passa fome'

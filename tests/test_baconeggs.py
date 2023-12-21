try:
    import sys
    import os

    sys.path.append(
        os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),
                '../src'
            )
        )
    )
except ImportError:
    raise ImportError


import unittest
from baconeggs import bacon_eggs


class TestBaconEggs(unittest.TestCase):
    def test_bacon_eggs_deve_levantar_assertion_se_nao_for_int(self):
        with self.assertRaises(AssertionError):
            bacon_eggs('1.5')

    def test_bacon_eggs_deve_retornar_baconeggs_se_entrada_for_mult_3_e_5(self):
        entradas = (15, 30, 45, 60)
        saida = 'baconeggs'

        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(
                    bacon_eggs(entrada),
                    saida
                    )

    def test_bacon_eggs_deve_retornar_bacon_se_entrada_for_mult_3(self):
        entradas = (3, 6, 9, 12)
        saida = 'bacon'

        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(
                    bacon_eggs(entrada),
                    saida
                )

    def test_bacon_eggs_deve_retornar_eggs_se_entrada_for_mult_5(self):
        entradas = (5, 10, 20, 25)
        saida = 'eggs'

        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(
                    bacon_eggs(entrada),
                    saida
                )

    def test_bacon_eggs_deve_retornar_passa_fome_se_entrada_nao_for_mult_3_nem_5(self):
        entradas = (2, 4, 8, 7)
        saida = 'passa fome'

        for entrada in entradas:
            with self.subTest(entrada=entrada):
                self.assertEqual(bacon_eggs(entrada), saida)


if __name__ == '__main__':
    unittest.main()

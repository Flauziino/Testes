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
from calculadora import soma, subtrai


class TesteCalculadora(unittest.TestCase):
    # Testes para funcao soma
    def test_soma_5_e_5_deve_retornar_10(self):
        self.assertEqual(soma(5, 5), 10)

    def test_soma_5_negativo_e_5_deve_retornar_0(self):
        self.assertEqual(soma(-5, 5), 0)

    def test_soma_varias_entradas_soma(self):
        x_y_saidas = (
            (10, 10, 20),
            (5, -5, 0),
            (1.5, 1.5, 3.0),
            (-10, 10, 0),
            (100, 100, 200),
        )

        for x_y_saida in x_y_saidas:
            with self.subTest(x_y_saida=x_y_saida):
                x, y, saida = x_y_saida
                self.assertEqual(soma(x, y), saida)

    def test_soma_retorna_assertionerror_para_x(self):
        with self.assertRaises(AssertionError):
            soma('11', 10)

    def test_soma_retorna_assertionerror_para_y(self):
        with self.assertRaises(AssertionError):
            soma(10, '10')

    # Testes para funcao subtrai
    def test_varias_entradas_subtrai(self):
        x_y_saidas = (
            (10, 5, 5),
            (-5, 5, -10),
            (10, 10, 0),
            (4.5, 1.5, 3.0),
        )

        for x_y_saida in x_y_saidas:
            with self.subTest(x_y_saida=x_y_saida):
                x, y, saida = x_y_saida
                self.assertEqual(subtrai(x, y), saida)

    def test_subtrai_retorna_assertionerror_para_x(self):
        with self.assertRaises(AssertionError):
            subtrai('11', 10)

    def test_subtrai_retorna_assertionerror_para_y(self):
        with self.assertRaises(AssertionError):
            subtrai(10, '10')


if __name__ == '__main__':
    unittest.main()

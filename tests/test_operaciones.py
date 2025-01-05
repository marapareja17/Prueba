import unittest
from src.operaciones import suma

class TestOperaciones(unittest.TestCase):
    def test_suma_positivos(self):
        self.assertEqual(suma(1, 2), 3)

    def test_suma_negativos(self):
        self.assertEqual(suma(-1, -1), -2)

    def test_suma_cero(self):
        self.assertEqual(suma(0, 0), 0)

if __name__ == '__main__':
    unittest.main()

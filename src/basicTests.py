import unittest
import mathLib  # Importuje mathLib, aby byly dostupné funkce jako add, subtract, etc.

class TestMatLib(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)

    def test_add(self):
        self.assertEqual(mathLib.add(2, 3), 5)  # Test základního sčítání kladných čísel
        self.assertEqual(mathLib.add(1000000, 1), 1000001)  # Test sčítání velkých čísel
        self.assertEqual(mathLib.add(-3, 3), 0)  # Test sčítání čísla se záporným protějškem (výsledek 0)
        self.assertEqual(mathLib.add(-10, 7), -3)  # Test sčítání záporného a kladného čísla
        self.assertEqual(mathLib.add(-10, -20), -30)  # Test sčítání dvou záporných čísel
        self.assertEqual(mathLib.add(0, 7), 7)  # Test sčítání s nulou

    def test_subtract(self):
        self.assertEqual(mathLib.subtract(5, 3), 2)  # Test základního odčítání kladných čísel
        self.assertEqual(mathLib.subtract(-5, -3), -2)  # Test odčítání dvou záporných čísel
        self.assertEqual(mathLib.subtract(5, -3), 8)  # Test odčítání záporného čísla (ekvivalent sčítání)
        self.assertEqual(mathLib.subtract(7, 0), 7)  # Test odčítání nuly
        self.assertEqual(mathLib.subtract(0, 7), -7)  # Test odčítání od nuly
        self.assertEqual(mathLib.subtract(1000000, 500000), 500000)  # Test odčítání velkých čísel
        self.assertEqual(mathLib.subtract(42, 42), 0)  # Test odčítání stejných čísel (výsledek 0)

    def test_multiply(self):
        self.assertEqual(mathLib.multiply(2, 3), 6)
        self.assertEqual(mathLib.multiply(4, 3), 12)  # Kladná čísla
        self.assertEqual(mathLib.multiply(-4, -3), 12)  # Záporná čísla
        self.assertEqual(mathLib.multiply(4, -3), -12)  # Kladné × záporné
        self.assertEqual(mathLib.multiply(7, 0), 0)  # Násobení nulou
        self.assertEqual(mathLib.multiply(0, 7), 0)  # Násobení nulou (obráceně)
        self.assertEqual(mathLib.multiply(1000, 1000), 1000000)  # Velká čísla

    def test_divide(self):
        self.assertEqual(mathLib.divide(10, 2), 5)  # Kladná čísla
        self.assertEqual(mathLib.divide(-10, 2), -5)  # Záporné číslo děleno kladným
        self.assertEqual(mathLib.divide(10, -2), -5)  # Kladné číslo děleno záporným
        self.assertEqual(mathLib.divide(0, 5), 0)  # Nula dělená číslem

        # Dělení se zbytkem
        self.assertEqual(mathLib.divide_with_remainder(10, 3), (3, 1))  # 10 / 3 = 3 zbytek 1
        self.assertEqual(mathLib.divide_with_remainder(25, 7), (3, 4))  # 25 / 7 = 3 zbytek 4

        # Test dělení nulou (očekává výjimku)
        with self.assertRaises(ZeroDivisionError):
            mathLib.divide(10, 0)
        with self.assertRaises(ZeroDivisionError):
            mathLib.divide_with_remainder(10, 0)

    def test_factorial(self):
        self.assertEqual(mathLib.factorial(0), 1)  # Faktoriál nuly
        self.assertEqual(mathLib.factorial(5), 120)  # Faktoriál kladného čísla
        self.assertEqual(mathLib.factorial(10), 3628800)  # Faktoriál většího čísla

        # Test pro záporné číslo (očekává výjimku)
        with self.assertRaises(ValueError):
            mathLib.factorial(-5)

    def test_power(self):
        self.assertEqual(mathLib.power(2, 3), 8)  # Umocnění kladného čísla
        self.assertEqual(mathLib.power(5, 0), 1)  # Umocnění na nulu
        self.assertEqual(mathLib.power(7, -2), 0.02040816326530612)  # Umocnění s negativním exponentem

        # Test pro záporný exponent v umocnění (očekává výjimku)
        with self.assertRaises(ValueError):
            mathLib.power(0, -1)  # Nula nemůže mít záporný exponent


if __name__ == '__main__':
    unittest.main()

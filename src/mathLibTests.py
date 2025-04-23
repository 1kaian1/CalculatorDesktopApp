# This file is part of Calculator_app.
#
# Calculator_app is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Calculator_app is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.
#
# Copyright (c) 2025 Jan Kai Marek, xmarekj00

import unittest
from mathLib import MathLib  # Importuje mathLib, aby byly dostupné funkce jako add, subtract, etc.

class TestMatLib(unittest.TestCase):
    def test_add(self):
        self.assertEqual(MathLib.add(2, 3), 5)  # Test základního sčítání kladných čísel
        self.assertEqual(MathLib.add(1000000, 1), 1000001)  # Test sčítání velkých čísel
        self.assertEqual(MathLib.add(-3, 3), 0)  # Test sčítání čísla se záporným protějškem (výsledek 0)
        self.assertEqual(MathLib.add(-10, 7), -3)  # Test sčítání záporného a kladného čísla
        self.assertEqual(MathLib.add(-10, -20), -30)  # Test sčítání dvou záporných čísel
        self.assertEqual(MathLib.add(0, 7), 7)  # Test sčítání s nulou

        # Float testy
        self.assertAlmostEqual(MathLib.add(2.5, 3.2), 5.7)
        self.assertAlmostEqual(MathLib.add(-1.1, 1.1), 0.0)
        self.assertAlmostEqual(MathLib.add(1000.5, 0.5), 1001.0)
        self.assertAlmostEqual(MathLib.add(-3.7, -2.3), -6.0)

    def test_subtract(self):
        self.assertEqual(MathLib.subtract(5, 3), 2)  # Test základního odčítání kladných čísel
        self.assertEqual(MathLib.subtract(-5, -3), -2)  # Test odčítání dvou záporných čísel
        self.assertEqual(MathLib.subtract(5, -3), 8)  # Test odčítání záporného čísla (ekvivalent sčítání)
        self.assertEqual(MathLib.subtract(7, 0), 7)  # Test odčítání nuly
        self.assertEqual(MathLib.subtract(0, 7), -7)  # Test odčítání od nuly
        self.assertEqual(MathLib.subtract(1000000, 500000), 500000)  # Test odčítání velkých čísel
        self.assertEqual(MathLib.subtract(42, 42), 0)  # Test odčítání stejných čísel (výsledek 0)

        # Float testy
        self.assertAlmostEqual(MathLib.subtract(5.5, 3.2), 2.3)
        self.assertAlmostEqual(MathLib.subtract(-1.1, -2.2), 1.1)
        self.assertAlmostEqual(MathLib.subtract(10.75, 0.75), 10.0)
        self.assertAlmostEqual(MathLib.subtract(-4.5, 2.5), -7.0)

    def test_multiply(self):
        self.assertEqual(MathLib.multiply(2, 3), 6)
        self.assertEqual(MathLib.multiply(4, 3), 12)  # Kladná čísla
        self.assertEqual(MathLib.multiply(-4, -3), 12)  # Záporná čísla
        self.assertEqual(MathLib.multiply(4, -3), -12)  # Kladné × záporné
        self.assertEqual(MathLib.multiply(7, 0), 0)  # Násobení nulou
        self.assertEqual(MathLib.multiply(0, 7), 0)  # Násobení nulou (obráceně)
        self.assertEqual(MathLib.multiply(1000, 1000), 1000000)  # Velká čísla

        # Float testy
        self.assertAlmostEqual(MathLib.multiply(2.5, 4.0), 10.0)
        self.assertAlmostEqual(MathLib.multiply(-3.5, 2.0), -7.0)
        self.assertAlmostEqual(MathLib.multiply(0.1, 0.2), 0.02)
        self.assertAlmostEqual(MathLib.multiply(-1.1, -2.2), 2.42)

    def test_divide(self):
        self.assertEqual(MathLib.divide(10, 2), 5)  # Kladná čísla
        self.assertEqual(MathLib.divide(-10, 2), -5)  # Záporné číslo děleno kladným
        self.assertEqual(MathLib.divide(10, -2), -5)  # Kladné číslo děleno záporným
        self.assertEqual(MathLib.divide(0, 5), 0)  # Nula dělená číslem

        # Float testy
        self.assertAlmostEqual(MathLib.divide(5.5, 2.0), 2.75)
        self.assertAlmostEqual(MathLib.divide(-9.0, 3.0), -3.0)
        self.assertAlmostEqual(MathLib.divide(7.5, 2.5), 3.0)
        self.assertAlmostEqual(MathLib.divide(0.5, 0.1), 5.0)

        # Test dělení nulou (očekává výjimku)
        with self.assertRaises(ZeroDivisionError):
            MathLib.divide(10, 0)

    def test_divide_with_remainder(self):
        self.assertEqual(MathLib.divide_with_remainder(10, 3), (3, 1))  # 10 / 3 = 3 zbytek 1
        self.assertEqual(MathLib.divide_with_remainder(25, 7), (3, 4))  # 25 / 7 = 3 zbytek 4

        # Dělení se zbytkem floaty
        self.assertEqual(MathLib.divide_with_remainder(10.5, 3.2), (3.0, 1.1))  # 10.5 / 3.2 = 3.0 zbytek 1.1
        self.assertEqual(MathLib.divide_with_remainder(25.7, 7.5), (3.0, 3.2))  # 25.7 / 7.5 = 3.0 zbytek 3.2
        self.assertEqual(MathLib.divide_with_remainder(-15.6, 4.1), (-3.0, -3.3))  # -15.6 / 4.1 = -3.0 zbytek -3.3
        self.assertEqual(MathLib.divide_with_remainder(8.4, -2.5), (-3.0, 0.9))  # 8.4 / -2.5 = -3.0 zbytek 0.9

        # Test dělení nulou (očekává výjimku)
        with self.assertRaises(ZeroDivisionError):
            MathLib.divide_with_remainder(10, 0)

    def test_factorial(self):
        self.assertEqual(MathLib.factorial(0), 1)  # Faktoriál nuly
        self.assertEqual(MathLib.factorial(5), 120)  # Faktoriál kladného čísla
        self.assertEqual(MathLib.factorial(10), 3628800)  # Faktoriál většího čísla

        # Test pro záporné číslo (očekává výjimku)
        with self.assertRaises(ValueError):
            MathLib.factorial(-5)

        # Test pro float číslo (očekává výjimku)
        with self.assertRaises(ValueError):
            MathLib.factorial(5.5)

    def test_power(self):
        self.assertEqual(MathLib.power(2, 3), 8)  # Umocnění kladného čísla
        self.assertEqual(MathLib.power(5, 0), 1)  # Umocnění na nulu
        self.assertAlmostEqual(MathLib.power(7, -2), 0.02040816326530612)  # Umocnění s negativním exponentem

        # Test pro záporný exponent v umocnění (očekává výjimku)
        with self.assertRaises(ValueError):
            MathLib.power(0, -1)  # Nula nemůže mít záporný exponent

        # Test pro exponent typu float (očekává výjimku)
        with self.assertRaises(ValueError):
            MathLib.power(2, 3.5)  # Exponent je typu float

    def test_sqrt(self):
        # Odmocnina z kladného čísla
        self.assertEqual(MathLib.sqrt(4, 1), 2)  # Odmocnina z 4 (exponent 1)
        self.assertEqual(MathLib.sqrt(9, 1), 3)  # Odmocnina z 9 (exponent 1)
        self.assertEqual(MathLib.sqrt(0, 1), 0)  # Odmocnina z 0 (exponent 1)

        # Odmocnina z necelého čísla
        self.assertAlmostEqual(MathLib.sqrt(2, 1), 1.414213562, places=9)  # Odmocnina z 2 (exponent 1)

        # Test pro záporný exponent
        self.assertAlmostEqual(MathLib.sqrt(4, -1), 0.5, places=9)  # Záporný exponent pro 4 (exponent -1)
        self.assertAlmostEqual(MathLib.sqrt(2, -2), 0.25, places=9)  # Záporný exponent pro 2 (exponent -2)

        # Float testy
        self.assertAlmostEqual(MathLib.sqrt(2.25, 1), 1.5, places=9)  # Odmocnina z 2.25 (exponent 1)
        self.assertAlmostEqual(MathLib.sqrt(7.84, 1), 2.8, places=9)  # Odmocnina z 7.84 (exponent 1)
        self.assertAlmostEqual(MathLib.sqrt(0.01, 1), 0.1, places=9)  # Odmocnina z 0.01 (exponent 1)
        self.assertAlmostEqual(MathLib.sqrt(100.0, 1), 10.0, places=9)  # Odmocnina z 100.0 (exponent 1)

        # Záporné exponenty pro floaty
        self.assertAlmostEqual(MathLib.sqrt(2.0, -1), 0.5, places=9)  # Záporný exponent pro 2.0 (exponent -1)
        self.assertAlmostEqual(MathLib.sqrt(0.25, -2), 16.0, places=9)  # Záporný exponent pro 0.25 (exponent -2)
        self.assertAlmostEqual(MathLib.sqrt(5.0, -3), 0.008, places=9)  # Záporný exponent pro 5.0 (exponent -3)

        # Test záporného čísla (očekává výjimku)
        with self.assertRaises(ValueError):
            MathLib.sqrt(-4)


if __name__ == '__main__':
    unittest.main()

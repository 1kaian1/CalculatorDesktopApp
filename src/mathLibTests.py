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
from mathLib import MathLib

class TestMatLib(unittest.TestCase):

    def test_evaluate_parentheses(self):

        self.assertEqual(MathLib("(2+3)*5").evaluate_parentheses().get_result(), "5*5")
        self.assertEqual(MathLib("(2+3)5").evaluate_parentheses().get_result(), "5*5")
        self.assertEqual(MathLib("5(2+3)").evaluate_parentheses().get_result(), "5*5")
        self.assertEqual(MathLib("-(-(2+3))").evaluate_parentheses().get_result(), "--5")
        self.assertEqual(MathLib("(2+3)(2*3)").evaluate_parentheses().get_result(), "5*6")
        self.assertEqual(MathLib("(2+3.2)(2.5*3)").evaluate_parentheses().get_result(), "5.2*7.5")
        self.assertEqual(MathLib("(2+3.2)(-2(2.5*3))").evaluate_parentheses().get_result(), "5.2*-15")

        with self.assertRaises(ValueError): MathLib("((2+3)(2*3)").evaluate_parentheses().get_result()
        with self.assertRaises(ValueError): MathLib("(2+3)(2*3))").evaluate_parentheses().get_result()

    # def test_add(self):
    #
    #     # Integer tests
    #     self.assertEqual(MathLib("2+3").evaluate_expression(), "5")
    #     self.assertEqual(MathLib("-3+3").evaluate_expression(), "0")
    #     self.assertEqual(MathLib("0+7").evaluate_expression(), "7")
    #     self.assertEqual(MathLib("-3+2").evaluate_expression(), "-1")
    #     self.assertEqual(MathLib("-3+(-2)").evaluate_expression(), "-5")
    #
    #     # Float tests
    #     self.assertAlmostEqual(MathLib("2.5+3.2").evaluate_expression(), "5.7")
    #     self.assertAlmostEqual(MathLib("-1.1+1.1").evaluate_expression(), "0")
    #     self.assertAlmostEqual(MathLib("0+3.2").evaluate_expression(), "3.2")
    #     self.assertAlmostEqual(MathLib("-2.5+1.2").evaluate_expression(), "-1.3")
    #     self.assertAlmostEqual(MathLib("-2.5+(-1.2)").evaluate_expression(), "-3.7")
    #
    #     # Conflicts tests
    #     self.assertEqual(MathLib("2++3").evaluate_expression(), "5")
    #     self.assertEqual(MathLib("--2++3").evaluate_expression(), "5")
    #     self.assertEqual(MathLib("2-+3").evaluate_expression(), "-1")
    #     self.assertEqual(MathLib("2--3").evaluate_expression(), "5")
    #     self.assertEqual(MathLib("2++3-").evaluate_expression(), "Error")
    #
    #
    # def test_subtract(self):
    #
    #     # Integer tests
    #     self.assertEqual(MathLib("2-3").evaluate_expression(), "-1")
    #     self.assertEqual(MathLib("-3-3").evaluate_expression(), "-6")
    #     self.assertEqual(MathLib("0-7").evaluate_expression(), "-7")
    #     self.assertEqual(MathLib("-3-2").evaluate_expression(), "-5")
    #     self.assertEqual(MathLib("-3-(-2)").evaluate_expression(), "-1")
    #
    #     # Float tests
    #     self.assertAlmostEqual(MathLib("2.5-3.2").evaluate_expression(), "-0.7")
    #     self.assertAlmostEqual(MathLib("-1.1-1.1").evaluate_expression(), "-2.2")
    #     self.assertAlmostEqual(MathLib("0-3.2").evaluate_expression(), "-3.2")
    #     self.assertAlmostEqual(MathLib("-2.5-1.2").evaluate_expression(), "-3.7")
    #     self.assertAlmostEqual(MathLib("-2.5-(-1.2)").evaluate_expression(), "-1.3")
    #
    #     # Conflicts tests
    #     self.assertEqual(MathLib("2++3").evaluate_expression(), "5")
    #     self.assertEqual(MathLib("--2++3").evaluate_expression(), "5")
    #     self.assertEqual(MathLib("2-+3").evaluate_expression(), "-1")
    #     self.assertEqual(MathLib("2--3").evaluate_expression(), "5")
    #     self.assertEqual(MathLib("2++3-").evaluate_expression(), "Error")

    # def test_multiply(self):
    #
    #     # Integer tests
    #     self.assertEqual(MathLib("2*3").evaluate_expression(), "6")
    #     self.assertEqual(MathLib("-2*(-3)").evaluate_expression(), "6")
    #     self.assertEqual(MathLib("2*3").evaluate_expression(), "6")
    #     self.assertEqual(MathLib("2*3").evaluate_expression(), "6")
    #     self.assertEqual(MathLib("2*3").evaluate_expression(), "6")
    #
    #     # Float tests
    #
    #     self.assertEqual(mathLib.multiply(4, 3), 12)  # Kladná čísla
    #     self.assertEqual(mathLib.multiply(-4, -3), 12)  # Záporná čísla
    #     self.assertEqual(mathLib.multiply(4, -3), -12)  # Kladné × záporné
    #     self.assertEqual(mathLib.multiply(7, 0), 0)  # Násobení nulou
    #     self.assertEqual(mathLib.multiply(0, 7), 0)  # Násobení nulou (obráceně)
    #     self.assertEqual(mathLib.multiply(1000, 1000), 1000000)  # Velká čísla
    #
    #     # Float testy
    #     self.assertAlmostEqual(mathLib.multiply(2.5, 4.0), 10.0)
    #     self.assertAlmostEqual(mathLib.multiply(-3.5, 2.0), -7.0)
    #     self.assertAlmostEqual(mathLib.multiply(0.1, 0.2), 0.02)
    #     self.assertAlmostEqual(mathLib.multiply(-1.1, -2.2), 2.42)
    #
    # def test_divide(self):
    #     self.assertEqual(mathLib.divide(10, 2), 5)  # Kladná čísla
    #     self.assertEqual(mathLib.divide(-10, 2), -5)  # Záporné číslo děleno kladným
    #     self.assertEqual(mathLib.divide(10, -2), -5)  # Kladné číslo děleno záporným
    #     self.assertEqual(mathLib.divide(0, 5), 0)  # Nula dělená číslem
    #
    #     # Float testy
    #     self.assertAlmostEqual(mathLib.divide(5.5, 2.0), 2.75)
    #     self.assertAlmostEqual(mathLib.divide(-9.0, 3.0), -3.0)
    #     self.assertAlmostEqual(mathLib.divide(7.5, 2.5), 3.0)
    #     self.assertAlmostEqual(mathLib.divide(0.5, 0.1), 5.0)
    #
    #     # Test dělení nulou (očekává výjimku)
    #     with self.assertRaises(ZeroDivisionError):
    #         mathLib.divide(10, 0)
    #
    # def test_divide_with_remainder(self):
    #     self.assertEqual(mathLib.divide_with_remainder(10, 3), (3, 1))  # 10 / 3 = 3 zbytek 1
    #     self.assertEqual(mathLib.divide_with_remainder(25, 7), (3, 4))  # 25 / 7 = 3 zbytek 4
    #
    #     # Dělení se zbytkem floaty
    #     self.assertEqual(mathLib.divide_with_remainder(10.5, 3.2), (3.0, 1.1))  # 10.5 / 3.2 = 3.0 zbytek 1.1
    #     self.assertEqual(mathLib.divide_with_remainder(25.7, 7.5), (3.0, 3.2))  # 25.7 / 7.5 = 3.0 zbytek 3.2
    #     self.assertEqual(mathLib.divide_with_remainder(-15.6, 4.1), (-3.0, -3.3))  # -15.6 / 4.1 = -3.0 zbytek -3.3
    #     self.assertEqual(mathLib.divide_with_remainder(8.4, -2.5), (-3.0, 0.9))  # 8.4 / -2.5 = -3.0 zbytek 0.9
    #
    #     # Test dělení nulou (očekává výjimku)
    #     with self.assertRaises(ZeroDivisionError):
    #         mathLib.divide_with_remainder(10, 0)
    #
    # def test_factorial(self):
    #     self.assertEqual(mathLib.evaluate_factorial(0), 1)  # Faktoriál nuly
    #     self.assertEqual(mathLib.evaluate_factorial(5), 120)  # Faktoriál kladného čísla
    #     self.assertEqual(mathLib.evaluate_factorial(10), 3628800)  # Faktoriál většího čísla
    #
    #     # Test pro záporné číslo (očekává výjimku)
    #     with self.assertRaises(ValueError):
    #         mathLib.evaluate_factorial(-5)
    #
    #     # Test pro float číslo (očekává výjimku)
    #     with self.assertRaises(ValueError):
    #         mathLib.evaluate_factorial(5.5)
    #
    # def test_power(self):
    #     self.assertEqual(mathLib.evaluate_power(2, 3), 8)  # Umocnění kladného čísla
    #     self.assertEqual(mathLib.evaluate_power(5, 0), 1)  # Umocnění na nulu
    #     self.assertAlmostEqual(mathLib.evaluate_power(7, -2), 0.02040816326530612)  # Umocnění s negativním exponentem
    #
    #     # Test pro záporný exponent v umocnění (očekává výjimku)
    #     with self.assertRaises(ValueError):
    #         mathLib.evaluate_power(0, -1)  # Nula nemůže mít záporný exponent
    #
    #     # Test pro exponent typu float (očekává výjimku)
    #     with self.assertRaises(ValueError):
    #         mathLib.evaluate_power(2, 3.5)  # Exponent je typu float
    #
    # def test_sqrt(self):
    #     # Odmocnina z kladného čísla
    #     self.assertEqual(mathLib.evaluate_sqrt(4, 1), 2)  # Odmocnina z 4 (exponent 1)
    #     self.assertEqual(mathLib.evaluate_sqrt(9, 1), 3)  # Odmocnina z 9 (exponent 1)
    #     self.assertEqual(mathLib.evaluate_sqrt(0, 1), 0)  # Odmocnina z 0 (exponent 1)
    #
    #     # Odmocnina z necelého čísla
    #     self.assertAlmostEqual(mathLib.evaluate_sqrt(2, 1), 1.414213562, places=9)  # Odmocnina z 2 (exponent 1)
    #
    #     # Test pro záporný exponent
    #     self.assertAlmostEqual(mathLib.evaluate_sqrt(4, -1), 0.5, places=9)  # Záporný exponent pro 4 (exponent -1)
    #     self.assertAlmostEqual(mathLib.evaluate_sqrt(2, -2), 0.25, places=9)  # Záporný exponent pro 2 (exponent -2)
    #
    #     # Float testy
    #     self.assertAlmostEqual(mathLib.evaluate_sqrt(2.25, 1), 1.5, places=9)  # Odmocnina z 2.25 (exponent 1)
    #     self.assertAlmostEqual(mathLib.evaluate_sqrt(7.84, 1), 2.8, places=9)  # Odmocnina z 7.84 (exponent 1)
    #     self.assertAlmostEqual(mathLib.evaluate_sqrt(0.01, 1), 0.1, places=9)  # Odmocnina z 0.01 (exponent 1)
    #     self.assertAlmostEqual(mathLib.evaluate_sqrt(100.0, 1), 10.0, places=9)  # Odmocnina z 100.0 (exponent 1)
    #
    #     # Záporné exponenty pro floaty
    #     self.assertAlmostEqual(mathLib.evaluate_sqrt(2.0, -1), 0.5, places=9)  # Záporný exponent pro 2.0 (exponent -1)
    #     self.assertAlmostEqual(mathLib.evaluate_sqrt(0.25, -2), 16.0, places=9)  # Záporný exponent pro 0.25 (exponent -2)
    #     self.assertAlmostEqual(mathLib.evaluate_sqrt(5.0, -3), 0.008, places=9)  # Záporný exponent pro 5.0 (exponent -3)
    #
    #     # Test záporného čísla (očekává výjimku)
    #     with self.assertRaises(ValueError):
    #         mathLib.evaluate_sqrt(-4)


if __name__ == '__main__':
    unittest.main()

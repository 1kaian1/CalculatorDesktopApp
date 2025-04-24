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
    """Unit tests for the MathLib class."""

    def test_evaluate_parentheses(self):
        """Tests evaluation of expressions with parentheses, including nested and implicit multiplication cases."""
        self.assertEqual(MathLib("2+(3+4)").evaluate_parentheses().expression, "2+7")
        self.assertEqual(MathLib("2+(3*(1+2))").evaluate_parentheses().expression, "2+9")
        self.assertEqual(MathLib("2(3+4)").evaluate_parentheses().expression, "2*7")
        self.assertEqual(MathLib("(2+3)(4+1)").evaluate_parentheses().expression, "5*5")
        self.assertEqual(MathLib("10/(2+3)").evaluate_parentheses().expression, "10/5")
        self.assertEqual(MathLib("(1+2)+(3+4)").evaluate_parentheses().expression, "3+7")
        self.assertEqual(MathLib("(2+3)*(1+1)").evaluate_parentheses().expression, "5*2")
        self.assertEqual(MathLib("2+(3+(4+5))").evaluate_parentheses().expression, "2+12")
        self.assertEqual(MathLib("((2+3)+4)").evaluate_parentheses().expression, "9")
        self.assertEqual(MathLib("2+(3+((1+1)+1))").evaluate_parentheses().expression, "2+6")

    def test_evaluate_sqrt(self):
        """Tests correct evaluation of square roots and n-th roots, including handling of negative numbers and decimals."""
        self.assertAlmostEqual(float(MathLib("√9").evaluate_sqrt().expression), 3.0)
        self.assertAlmostEqual(float(MathLib("3√27").evaluate_sqrt().expression), 3.0)
        self.assertAlmostEqual(float(MathLib("4√16").evaluate_sqrt().expression), 2.0)
        self.assertAlmostEqual(float(MathLib("√2.25").evaluate_sqrt().expression), 1.5)
        self.assertAlmostEqual(float(MathLib("3√-27").evaluate_sqrt().expression), -3.0)
        self.assertAlmostEqual(float(MathLib("5√-32").evaluate_sqrt().expression), -2.0)
        self.assertAlmostEqual(float(MathLib("2√0").evaluate_sqrt().expression), 0.0)
        self.assertAlmostEqual(float(MathLib("3√0.008").evaluate_sqrt().expression), 0.2)
        self.assertAlmostEqual(float(MathLib("√10000").evaluate_sqrt().expression), 100.0)
        self.assertRaises(ValueError, lambda: MathLib("2√-16").evaluate_sqrt())

    def test_evaluate_factorial(self):
        """Tests evaluation of factorial expressions, including combinations with arithmetic and edge cases."""
        self.assertEqual(MathLib("0!").evaluate_factorial().expression, "1")
        self.assertEqual(MathLib("1!").evaluate_factorial().expression, "1")
        self.assertEqual(MathLib("3!").evaluate_factorial().expression, "6")
        self.assertEqual(MathLib("5!").evaluate_factorial().expression, "120")
        self.assertEqual(MathLib("6!+2").evaluate_factorial().expression, "720+2")
        self.assertEqual(MathLib("2+4!").evaluate_factorial().expression, "2+24")
        self.assertEqual(MathLib("2*3!").evaluate_factorial().expression, "2*6")
        self.assertEqual(MathLib("-3!").evaluate_factorial().expression, "-6")
        self.assertEqual(MathLib("2+1!").evaluate_factorial().expression, "2+1")
        self.assertRaises(ValueError, lambda: MathLib("4.5!").evaluate_factorial())

    def test_evaluate_power(self):
        """Tests evaluation of exponentiation operations, including negative and fractional exponents."""
        self.assertEqual(MathLib("2^3").evaluate_power().expression, "8.0")
        self.assertEqual(MathLib("5^0").evaluate_power().expression, "1.0")
        self.assertEqual(MathLib("9^0.5").evaluate_power().expression, "3.0")
        self.assertEqual(MathLib("2^3^2").evaluate_power().expression, "8.0^2")
        self.assertEqual(MathLib("10^1").evaluate_power().expression, "10.0")
        self.assertEqual(MathLib("3^2.0").evaluate_power().expression, "9.0")
        self.assertEqual(MathLib("2.5^2").evaluate_power().expression, "6.25")
        self.assertEqual(MathLib("4^-1").evaluate_power().expression, "0.25")
        self.assertEqual(MathLib("16^0.25").evaluate_power().expression, "2.0")
        self.assertEqual(MathLib("0^0").evaluate_power().expression, "1.0")

    def test_evaluate_percentage(self):
        """Tests conversion of percentages to decimal values and combination of percentages in expressions."""
        self.assertEqual(MathLib("100%").evaluate_percentage().expression, "1.0")
        self.assertEqual(MathLib("50%").evaluate_percentage().expression, "0.5")
        self.assertEqual(MathLib("25%").evaluate_percentage().expression, "0.25")
        self.assertEqual(MathLib("200%").evaluate_percentage().expression, "2.0")
        self.assertEqual(MathLib("0%").evaluate_percentage().expression, "0.0")
        self.assertEqual(MathLib("12.5%").evaluate_percentage().expression, "0.125")
        self.assertEqual(MathLib("1.5%").evaluate_percentage().expression, "0.015")
        self.assertEqual(MathLib("99.9%").evaluate_percentage().expression, "0.999")
        self.assertEqual(MathLib("0.1%").evaluate_percentage().expression, "0.001")
        self.assertEqual(MathLib("3% + 5%").evaluate_percentage().expression, "0.03 + 0.05")

    def test_evaluate_double_operators(self):
        """Tests simplification of expressions with multiple or conflicting operators (e.g. --, +-)."""
        self.assertEqual(MathLib("1+2--3").evaluate_double_operators().expression, "1+2+3")
        self.assertEqual(MathLib("5+-6").evaluate_double_operators().expression, "5-6")
        self.assertEqual(MathLib("3-+-4").evaluate_double_operators().evaluate_double_operators().expression, "3+4")
        self.assertEqual(MathLib("1--2").evaluate_double_operators().expression, "1+2")
        self.assertEqual(MathLib("1+-2+-3").evaluate_double_operators().expression, "1-2-3")
        self.assertEqual(MathLib("3++4").evaluate_double_operators().expression, "3+4")
        self.assertEqual(MathLib("1+-+2--3").evaluate_double_operators().expression, "1-2+3")
        self.assertEqual(MathLib("4--5+-6").evaluate_double_operators().expression, "4+5-6")
        self.assertEqual(MathLib("1+2--3++4+-+5-+-6").evaluate_double_operators().expression, "1+2+3+4-5+6")
        self.assertEqual(MathLib("++2-+-3").evaluate_double_operators().expression, "+2+3")

    def test_evaluate_multiplication_and_division(self):
        """Tests multiplication and division operations, including order of operations and fractional results."""
        self.assertEqual(MathLib("3*4").evaluate_multiplication_and_division().expression, "12")
        self.assertEqual(MathLib("10/2").evaluate_multiplication_and_division().expression, "5")
        self.assertEqual(MathLib("5/2").evaluate_multiplication_and_division().expression, "2.5")
        self.assertEqual(MathLib("7/3").evaluate_multiplication_and_division().expression, "2.333")
        self.assertEqual(MathLib("2*3/6").evaluate_multiplication_and_division().expression, "1")
        self.assertEqual(MathLib("8/+4*2").evaluate_multiplication_and_division().expression, "4")
        self.assertEqual(MathLib("6/3*5").evaluate_multiplication_and_division().expression, "10")
        self.assertEqual(MathLib("9*5/3").evaluate_multiplication_and_division().expression, "15")
        self.assertEqual(MathLib("3*5/2").evaluate_multiplication_and_division().expression, "7.5")
        self.assertEqual(MathLib("0*100").evaluate_multiplication_and_division().expression, "0")

    def test_evaluate_addition_and_substraction(self):
        """Tests basic addition and subtraction, including handling of leading signs and multiple operations."""
        self.assertEqual(MathLib("3+2").evaluate_addition_and_substraction().expression, "5")
        self.assertEqual(MathLib("5-3").evaluate_addition_and_substraction().expression, "2")
        self.assertEqual(MathLib("3+2-1").evaluate_addition_and_substraction().expression, "4")
        self.assertEqual(MathLib("1+2+3+4").evaluate_addition_and_substraction().expression, "10")
        self.assertEqual(MathLib("10-5-2").evaluate_addition_and_substraction().expression, "3")
        self.assertEqual(MathLib("1+2-3+4").evaluate_addition_and_substraction().expression, "4")
        self.assertEqual(MathLib("+5-3").evaluate_addition_and_substraction().expression, "2")
        self.assertEqual(MathLib("-5+3").evaluate_addition_and_substraction().expression, "-2")
        self.assertEqual(MathLib("0+5-3").evaluate_addition_and_substraction().expression, "2")
        self.assertEqual(MathLib("10-2+4-1+3").evaluate_addition_and_substraction().expression, "14")

if __name__ == '__main__':
    unittest.main()

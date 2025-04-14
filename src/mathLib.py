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
# Copyright (c) 2025 Jan Frantisek Levicek, xlevic02

import re

class MathLib:

    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b

    @staticmethod
    def multiply(a, b):
        return a * b

    @staticmethod
    def divide(a, b):
        if b == 0:
            raise ZeroDivisionError("Error: Division by zero")
        return a / b

    @staticmethod
    def factorial(n):
        if n < 0:
            raise ValueError("Error: Factorial is defined only for positive numbers")
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

    @staticmethod
    def power(base, exponent):
        return base ** exponent

    @staticmethod
    def sqrt(x, degree=2):
        if x < 0 and degree % 2 != 0:
            return -((-x) ** (1 / degree))
        elif x < 0 and degree % 2 == 0:
            raise ValueError("Error: A negative number does not have a real root with an even index")
        return x ** (1 / degree)

    @staticmethod
    def percentage(num1, operator, num2):
        if operator == "+":
            return num1 + num2 / 100 * num1
        elif operator == "-":
            return num1 - num2 / 100 * num1
        elif operator == "*":
            return num1 * (num2 / 100)
        elif operator == "/":
            return num1 / (num2 / 100)

    @staticmethod
    def evaluate_expression(expression):

        try:

            # Evaluating operator in front of parentheses
            #
            # re.sub - „search and replace“ given pattern in expression
            # lambda - anonymous function (could also be overwritten using def, but not necessary)
            #
            #   (?<=[^+\-*/%!√^]) \(
            #   group(1)^
            #
            # group(1) - checks for whatever char in front of "(" except for chars in square brackets
            #
            # This function says: If there is an opening bracket "(" and no operator is in front of it, but "*" there
            #
            expression = re.sub(
                r'(?<=[^+\-*/%!√^])\(',
                r'*(',
                expression
            )

            # Evaluating parentheses
            while '(' in expression:

                # Find the innermost parentheses
                inner_expr = re.search(r'\(([^()]+)\)', expression)

                if inner_expr:

                    # Recursively evaluating inner_expr
                    result = MathLib.evaluate_expression(inner_expr.group(1))

                    # Replacing inner_expr with result
                    expression = expression.replace(inner_expr.group(0), result)

                # Error if only "(" was found
                else:
                    raise ValueError("Error: Unable to find a properly closed pair of parentheses")

            # Evaluating square root
            #
            # re.sub - „search and replace“ given pattern in expression
            # lambda - anonymous function (could also be overwritten using def, but not necessary)
            # MathLib.sqrt() - calling MathLib func for square root
            #
            #         (\d*) √ (-?\d+\.?\d*)
            #   group(1)^   group(2)^
            #
            # group(1) - zero or more digits
            #
            # group(2):
            #   -?: optional minus
            #   d+: one or more digits
            #   .?: optional dot (for decimal number)
            #   d*: zero or more digits
            #
            # If group(1) is None, takes 2 as default (meaning square root from x at degree 2)
            #
            expression = re.sub(
                r'(\d*)√(-?\d+\.?\d*)',
                lambda m: str(MathLib.sqrt(float(m.group(2)), int(m.group(1)) if m.group(1) else 2)),
                expression
            )

            # Evaluating factorial
            #
            # re.sub - „search and replace“ given pattern in expression
            # lambda - anonymous function (could also be overwritten using def, but not necessary)
            # MathLib.factorial() - calling MathLib func for factorial
            #
            #         (\d+)!
            #   group(1)^
            #
            # group(1) - one or more digits
            #
            expression = re.sub(
                r'(\d+)!',
                lambda m: str(MathLib.factorial(int(m.group(1)))),
                expression
            )

            # Evaluating exponentation
            #
            # re.sub - „search and replace“ given pattern in expression
            # lambda - anonymous function (could also be overwritten using def, but not necessary)
            # MathLib.power() - calling MathLib func for exponentation
            #
            #     (\d+\.?\d*) \^ (-?\d+\.?\d*)
            #   group(1)^        group(2)^
            #
            # both group(1) and group(2):
            #   d+: one or more digits
            #   .?: optional dot (for decimal number)
            #   d*: zero or more digits
            #
            expression = re.sub(
                r'(\d+\.?\d*)\^(-?\d+\.?\d*)',
                lambda m: str(MathLib.power(float(m.group(1)), float(m.group(2)))),
                expression
            )

            # Evaluating percentage
            #
            # re.sub - „search and replace“ given pattern in expression
            # lambda - anonymous function (could also be overwritten using def, but not necessary)
            # MathLib.percentage() - calling MathLib func for exponentation
            #
            #      (\d+\.?\d*) ([+\-*/]) (-?\d+\.?\d*) %
            #   group(1)^  group(2)^   group(3)^
            #
            # both group(1) and group(3):
            #   d+: one or more digits
            #   .?: optional dot (for decimal number)
            #   d*: zero or more digits
            #
            # group(2) - one operator (+,-,*,/)
            #
            # In this function it is important, whether the operator is (1) "+" / "-" or (2) "*" / "/"
            #   (1) The added or subtracted percentage value is evaluated from group(1) number
            #       - example: 30-50% = 15
            #       - Fifty percent of 15 is subtracted from 30, giving the result of 15.
            #   (2) The multiplied or divided percentage value is evaluated from 1/group(3) number
            #       - example: 100/50% = 200
            #       - Fifty percent of 1 (1/2) is the divisor for 100, giving the result of 200.
            #
            # Examples:
            #   30-50% = 15
            #   30+50% = 45
            #   100/50% = 200
            #   100*50% = 50
            #
            expression = re.sub(
                r'(\d+\.?\d*)([+\-*/])(-?\d+\.?\d*)%',
                lambda m: str(MathLib.percentage(float(m.group(1)), m.group(2), float(m.group(3)))),
                expression
            )

            # Evaluating double operators
            #
            # re.sub - „search and replace“ given pattern in expression
            # lambda - anonymous function (could also be overwritten using def, but not necessary)
            #
            #       [+\-]{2,}
            #   group(0)^
            #
            # group(0) - plus or minus two or more times
            #
            # This function replaces every two-or-more operators with the correct equal one
            #
            # Examples:
            #   -- = +
            #   +-+ = -
            #   -+- = +
            #   1+2--3++4+-+5-+-6 = 1+2+3+4-5+6
            #
            expression = re.sub(
                r'[+\-]{2,}',
                lambda m: '-' if m.group(0).count('-') % 2 else '+',
                expression
            )

            # If expression begins with minus, we add "0" at start
            if expression.startswith('-'):
                expression = '0' + expression

            # Evaluating the rest of the expression (tokenization)
            #
            # re.findall - „find all matches“ of pattern in expression
            #
            #   \d+\.\d+|\d+|[-+*/]
            #
            # This pattern is set to look for a value that is either float, integer or operator. Nothing else can be in
            # our expression at this time.
            #
            tokens = re.findall(
                r'\d+\.\d+|\d+|[-+*/]',
                expression
            )

            # This loops goes through every token and if it finds "*" or "/", it multiplies or divides the values on
            # the left and on the right
            i = 0
            while i < len(tokens):
                if tokens[i] in ('*', '/'):
                    left = float(tokens[i - 1])
                    operator = tokens[i]
                    right = float(tokens[i + 1])

            # This loops goes through every token and if it finds "*" or "/", it multiplies or divides the values on
            # the left and on the right
            i = 0
            while i < len(tokens):
                if tokens[i] in ('*', '/'):
                    left = float(tokens[i - 1])
                    operator = tokens[i]
                    right = float(tokens[i + 1])

                    if operator == '*':
                        result = MathLib.multiply(left, right)
                    elif operator == '/':
                        result = MathLib.divide(left, right)

                    tokens[i - 1] = result
                    del tokens[i:i + 2]
                    i -= 1
                else:
                    i += 1

            # This loops goes through every token and if it finds "+" or "-", it adds or subtracts the values on
            # the left and on the right
            i = 1
            result = float(tokens[0])
            while i < len(tokens):
                operator = tokens[i]
                next_number = float(tokens[i + 1])

                if operator == '+':
                    result = MathLib.add(result, next_number)
                elif operator == '-':
                    result = MathLib.subtract(result, next_number)

                i += 2

            # Returns results either as an integer or float as rounded value.
            if result.is_integer():
                return str(int(result))
            return str(round(result, 3))

        # If an error occured during the evaluation, error message is printed on the calculator's screen. More info in
        # console
        except (ZeroDivisionError, IndexError, ValueError) as e:
            print(e)
            return "Error"

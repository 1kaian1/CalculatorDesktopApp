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

    def __init__(self, expression):

        self.original_expression = expression
        self.expression = expression
        self.recursion = False

    def evaluate_expression(self):
        r"""
        Evaluate given expression
        """

        print("Calling evaluate_expression")
        print("Eval:", self.expression)
        print("vvvvvvvvvv")

        try:

            # Evaluating parentheses
            self.evaluate_parentheses()
            self.print_step()

            # Evaluating square root
            self.evaluate_sqrt()
            self.print_step()

            # Evaluating factorial
            self.evaluate_factorial()
            self.print_step()

            # Evaluating exponentation
            self.evaluate_power()
            self.print_step()

            # Evaluating percentage
            self.evaluate_percentage()
            self.print_step()

            # Evaluating double operators
            self.evaluate_double_operators()
            self.print_step()

            # Evaluating multiplication and division
            self.evaluate_multiplication_and_division()
            self.print_step()

            # Evaluating addition and subtraction
            self.evaluate_addition_and_substraction()

            print("Result:", self.expression)
            print("----------")

        # If an error occured during the evaluation, error message is printed on the calculator's screen. More info in
        # console
        except (ZeroDivisionError, IndexError, ValueError) as e:
            print(e)
            self.expression = "Error"

        return self.expression

    def print_step(self):
        r"""
        Print evaluation step in console.
        :return:
        """

        if not self.recursion and self.expression != self.original_expression:
            print("Eval:", self.expression)
        self.original_expression = self.expression

    def get_result(self):
        r"""
        Return self.expression when requested.
        """

        return self.expression

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
    def sqrt(a):
        if a < 0:
            raise ValueError("Error: A negative number does not have a real root with an even index")
        return a ** 0.5

    def evaluate_parentheses(self):
        r"""
        Evaluating parentheses and adding '*' operator before parentheses if necessary.

        re.sub - „search and replace“ given pattern in expression
        MathLib.evaluate_expression - calling MathLib func to evaluate the inner expression in parentheses

             (\d|\)|!|%|√|\^) \(
            group(1)^

        group(1) - checks for any character in front of "(" except for those inside square brackets.

        This function performs two tasks:
        1. If there is an opening bracket "(" and no operator is in front of it, the function adds a "*" before it.
        2. It recursively evaluates the innermost expressions within parentheses, replacing them with the result.
        """

        # Add '*' where implicit multiplication is likely intended
        self.expression = re.sub(
            r'(\d|\))\(',
            r'\1*(',
            self.expression
        )
        self.expression = re.sub(
            r'\)(\d|\()',
            r')*\1',
            self.expression
        )

        # Parentheses checking with a counter
        count = 0
        for c in self.expression:
            if c == '(':
                count += 1
            elif c == ')':
                count -= 1
                if count < 0:
                    raise ValueError("Error: Too many closing parentheses")
        if count != 0:
            raise ValueError("Error: Too many opening parentheses")

        # Evaluate the parentheses recursively
        while '(' in self.expression:

            # Find the innermost parentheses
            inner_expr = re.search(r'\(([^()]+)\)', self.expression)

            if inner_expr:

                # Recursively evaluating inner expression
                self.recursion = True
                result = MathLib(inner_expr.group(1)).evaluate_expression()
                self.recursion = False

                # Replace the evaluated result back into the expression
                self.expression = self.expression.replace(inner_expr.group(0), result)

            else:
                raise ValueError("Error: Unable to find a properly closed pair of parentheses")

        return self

    def evaluate_sqrt(self):
        r"""
        Evaluating square root

        re.findall - „find all matches“ of the given pattern in expression
        MathLib.sqrt - calling MathLib func for square root

                  (\d*) √ (-?\d+\.?\d*)
            group(1)^   group(2)^

        group(1) - zero or more digits
        group(2):
            -?: optional minus
            d+: one or more digits
            .?: optional dot (for decimal number)
            d*: zero or more digits

        If group(1) is None, takes 2 as default (meaning square root from x at degree 2)
        """

        matches = re.findall(r'(\d*)√(-?\d+\.?\d*)', self.expression)
        for match in matches:
            degree_str, number_str = match  # Získáme čísla přímo z n-tice

            number = float(number_str)
            degree = int(degree_str) if degree_str else 2

            if number < 0:
                if degree % 2 == 0:
                    raise ValueError("Error: A negative number does not have a real root with an even index")
                result = -((-number) ** (1 / degree))
            else:
                result = number ** (1 / degree)

            self.expression = self.expression.replace(f"{degree_str}√{number_str}", str(result))

        return self


    def evaluate_factorial(self):
        r"""
        Evaluating factorial

        re.findall - „find all matches“ of the given pattern in expression
        MathLib.factorial - calling MathLib func for factorial

                  (\d+) !
            group(1)^

        group(1) - one or more digits
        """

        matches = re.findall(r'(\d+)!', self.expression)
        for match in matches:
            n_str = match

            n = int(n_str)

            if n < 0:
                raise ValueError("Error: Factorial is defined only for positive numbers")

            result = 1
            for i in range(1, n + 1):
                result *= i

            self.expression = self.expression.replace(f"{n_str}!", str(result))

        return self

    def evaluate_power(self):
        r"""
        Evaluating exponentiation

        re.findall - „find all matches“ of the given pattern in expression
        MathLib.power - calling MathLib func for exponentiation

                (\d+\.?\d*) \^ (-?\d+\.?\d*)
            group(1)^       group(2)^

        group(1) - one or more digits, optional decimal part
        group(2) - one or more digits, optional decimal part, possibly negative
        """

        matches = re.findall(r'(\d+\.?\d*)\^(-?\d+\.?\d*)', self.expression)
        for match in matches:
            base_str, exponent_str = match  # Získáme čísla přímo z n-tice

            base = float(base_str)
            exponent = float(exponent_str)

            result = base ** exponent

            self.expression = self.expression.replace(f"{base_str}^{exponent_str}", str(result))

        return self

    def evaluate_percentage(self):
        r"""
        Evaluating percentage

        re.findall - „find all matches“ of the given pattern in expression
        MathLib.percentage - calling MathLib func for percentage calculation

                (\d+\.?\d*) ([+\-*/]) (-?\d+\.?\d*) %
            group(1)^   group(2)^   group(3)^

        group(1) - one or more digits, optional decimal part
        group(3) - one or more digits, optional decimal part, possibly negative
        group(2) - one operator (+, -, *, /)

        In this function it is important, whether the operator is (1) "+" / "-" or (2) "*" / "/"
        (1) The added or subtracted percentage value is evaluated from group(1) number
            - example: 30-50% = 15
            - Fifty percent of 15 is subtracted from 30, giving the result of 15.
        (2) The multiplied or divided percentage value is evaluated from 1/group(3) number
            - example: 100/50% = 200
            - Fifty percent of 1 (1/2) is the divisor for 100, giving the result of 200.

        Examples:
        30-50% = 15
        30+50% = 45
        100/50% = 200
        100*50% = 50
        """

        matches = re.findall(r'(\d+\.?\d*)([+\-*/])(-?\d+\.?\d*)%', self.expression)
        for match in matches:
            num1_str, operator, num2_str = match

            num1 = float(num1_str)
            num2 = float(num2_str)

            if operator == "+":
                result = num1 + num2 / 100 * num1
            elif operator == "-":
                result = num1 - num2 / 100 * num1
            elif operator == "*":
                result = num1 * (num2 / 100)
            elif operator == "/":
                result = num1 / (num2 / 100)
            else:
                raise ValueError("Unsupported operator in percentage expression.")

            self.expression = self.expression.replace(f"{num1_str}{operator}{num2_str}%", str(result))

        return self

    def evaluate_double_operators(self):
        r"""
        Evaluating double operators

        re.sub - „search and replace“ given pattern in expression
        lambda - anonymous function (could also be overwritten using def, but not necessary)

                [+\-]{2,}
            group(0)^

        group(0) - plus or minus two or more times

        This function replaces every two-or-more operators with the correct equal one

        Examples:
            -- = +
            +-+ = -
            -+- = +
            1+2--3++4+-+5-+-6 = 1+2+3+4-5+6
        """

        self.expression = re.sub(
            r'[+\-]{2,}',
            lambda m: '-' if m.group(0).count('-') % 2 else '+',
            self.expression
        )

        return self

    def evaluate_multiplication_and_division(self):
        r"""
        This function processes the expression for multiplication '*' and division '/' operations.

        It loops through the expression and if it finds '*' or '/', it performs the operation between
        the number on the left and the number on the right, then replaces the operation with the result.

        Returns:
           The modified expression with * and / operations resolved.
        """

        if self.expression.startswith('-') or self.expression.startswith('+'):
            self.expression = '0' + self.expression

        # Tokenize the expression
        tokens = re.findall(r'\d+\.\d+|\d+|[-+*/]', self.expression)

        i = 0
        while i < len(tokens):
            if tokens[i] in ('*', '/'):
                left = float(tokens[i - 1])
                operator = tokens[i]

                if tokens[i + 1] in ('-', '+') and (i + 2 < len(tokens)):
                    right = float(tokens[i + 1] + tokens[i + 2])
                    del tokens[i + 1:i + 3]
                else:
                    right = float(tokens[i + 1])
                    del tokens[i + 1]

                if operator == '*':
                    result = MathLib.multiply(left, right)
                elif operator == '/':
                    result = MathLib.divide(left, right)

                result = round(result, 3) if not result.is_integer() else int(result)
                tokens[i - 1] = result
                del tokens[i:i + 2]
                i -= 1
            else:
                i += 1

        # Rebuild the expression with the evaluated tokens
        self.expression = ''.join(map(str, tokens))

        return self

    def evaluate_addition_and_substraction(self):
        r"""
        This function processes the expression for addition '+' and subtraction '-' operations.

        It loops through the expression and if it finds '+' or '-', it performs the operation between
        the number on the left and the number on the right, then updates the result.

        Returns:
           The final result after performing the + and - operations.
        """

        if self.expression.startswith('-') or self.expression.startswith('+'):
            self.expression = '0' + self.expression

        # Tokenize the expression
        tokens = re.findall(r'\d+\.\d+|\d+|[-+*/]', self.expression)

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

        self.expression = str(round(result, 3)) if not result.is_integer() else str(int(result))

        return self
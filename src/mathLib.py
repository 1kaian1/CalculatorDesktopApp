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
        """
        Initializes the MathLib object with a mathematical expression.

        Parameters:
        - expression (str): The input mathematical expression to be processed.

        Attributes:
        - original_expression (str): Stores the original, unmodified expression.
        - expression (str): A working copy of the expression used for evaluation and transformation.
        - recursion (bool): A flag indicating whether recursive evaluation is active.
        """

        self.original_expression = expression
        self.expression = expression

    def evaluate_expression(self):
        """
        Evaluates the stored mathematical expression step-by-step.

        The evaluation proceeds in the following order of operations:
        1. Parentheses
        2. Square roots (√)
        3. Factorials (!)
        4. Exponentiation (^)
        5. Percentages (%)
        6. Double operator cleanup (e.g., "--" -> "+")
        7. Multiplication and division (*, /)
        8. Addition and subtraction (+, -)

        In case of any evaluation error (e.g., division by zero, malformed expression),
        the method catches the exception and returns "Error".

        Returns:
            str: The final evaluated result or "Error" if evaluation failed.
        """

        try:

            # Evaluating parentheses
            self.evaluate_parentheses()

            # Evaluating square root
            self.evaluate_sqrt()

            # Evaluating factorial
            self.evaluate_factorial()

            # Evaluating exponentation
            self.evaluate_power()

            # Evaluating percentage
            self.evaluate_percentage()

            # Evaluating double operators
            self.evaluate_double_operators()

            # Evaluating multiplication and division
            self.evaluate_multiplication_and_division()

            # Evaluating addition and subtraction
            self.evaluate_addition_and_substraction()

        # If an error occured during the evaluation, error message is printed on the calculator's screen. More info in
        # console
        except (ZeroDivisionError, IndexError, ValueError) as e:
            print(e)
            self.expression = "Error"

        return self.expression

    @staticmethod
    def add(a, b):
        """
        Returns the sum of a and b.
        """
        return a + b

    @staticmethod
    def subtract(a, b):
        """
        Returns the difference between a and b (a - b).
        """
        return a - b

    @staticmethod
    def multiply(a, b):
        """
        Returns the product of a and b.
        """
        return a * b

    @staticmethod
    def divide(a, b):
        """
        Returns the result of division a / b.

        Raises:
            ZeroDivisionError: If b is zero.
        """
        if b == 0:
            raise ZeroDivisionError("Error: Division by zero")
        return a / b

    def evaluate_parentheses(self):
        """
        Evaluates parentheses in the expression and ensures correct handling of implicit multiplication.

        This function performs two main tasks:
        1. If an opening parenthesis '(' is preceded by a number or a closing parenthesis ')', it inserts a '*'
           operator to account for implicit multiplication (e.g., "2(3+4)" becomes "2*(3+4)").
        2. It recursively evaluates expressions inside parentheses, replacing them with their evaluated results.

        Steps:
        - Adds '*' before parentheses if necessary (e.g., "2(3)" becomes "2*(3)").
        - Ensures balanced parentheses by counting opening and closing parentheses.
        - Recursively evaluates the innermost expressions inside parentheses and replaces them in the main expression.

        Raises:
            ValueError: If there is a mismatch in parentheses or an invalid expression inside parentheses.
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
        """
        Evaluates square roots in the expression, allowing for custom roots (e.g., √x or n√x).

        This function searches for square root expressions in the form of "n√x", where "n" is the degree of the root
        (defaulting to 2 for square roots) and "x" is the number under the root. It then evaluates the square root,
        replacing the original expression with the result.

        Steps:
        1. The function searches for all occurrences of square roots in the expression using a regular expression.
        2. For each match, it calculates the root of the number using the specified degree.
        3. If the degree is not specified, it defaults to 2 (square root).
        4. The function handles both positive and negative numbers, checking if the degree is even when the number is negative
           (as even roots of negative numbers are not defined in the real number system).
        5. The original expression is updated by replacing each square root expression with its result.

        Raises:
            ValueError: If a negative number has an even degree root, as this would result in a complex number.
        """

        matches = re.findall(r'(\d*\.?\d*)√(-?\d+\.?\d*)', self.expression)
        for match in matches:
            degree_str, number_str = match  # Získáme čísla přímo z n-tice

            if degree_str and '.' in degree_str:
                raise ValueError("Error: A float number cannot precede a square root")

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
        """
        Evaluates factorial expressions in the form of "n!", where "n" is a positive integer.

        This function searches for all occurrences of factorial expressions in the form of "n!" in the given mathematical
        expression. It then calculates the factorial of the number "n", replacing the original factorial expression with the result.

        Steps:
        1. The function uses a regular expression to find all occurrences of numbers followed by an exclamation mark (factorial).
        2. For each match, it calculates the factorial of the number by multiplying all integers from 1 to "n".
        3. The function checks if the number is negative and raises an error, since factorials are only defined for non-negative integers.
        4. The original expression is updated by replacing each factorial expression with its computed result.

        Raises:
            ValueError: If the number "n" is negative, as factorials are undefined for negative numbers.
        """

        matches = re.findall(r'(\d+(?:\.\d+)?)!', self.expression)
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

        """
        Evaluates exponentiation expressions in the form of "base^exponent", where both base and exponent can be integers or decimals.

        This function searches for all occurrences of exponentiation expressions in the form of "base^exponent" in the given mathematical
        expression. It then calculates the result of raising the base to the power of the exponent, replacing the original exponentiation
        expression with the result.

        Steps:
        1. The function uses a regular expression to find all occurrences of numbers in the form of "base^exponent".
        2. For each match, it calculates the exponentiation by raising the base to the power of the exponent.
        3. The original expression is updated by replacing each exponentiation expression with its computed result.

        Details:
            - The base is the number being raised to a power.
            - The exponent is the power to which the base is raised.
            - Both the base and the exponent may be integers or floating-point numbers.
            - The exponent may be negative, representing a reciprocal.

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
        """
        Evaluates percentage expressions in the form of "number%", where the number can be an integer or a decimal.

        This function searches for all occurrences of percentage expressions in the form of "number%" in the given mathematical expression.
        It then calculates the equivalent decimal value by dividing the number by 100 and replaces the original percentage expression
        with the computed result.

        Steps:
        1. The function uses a regular expression to find all occurrences of numbers in the form of "number%".
        2. For each match, it divides the number by 100 to convert the percentage into a decimal.
        3. The original expression is updated by replacing each percentage expression with the computed decimal value, rounded to three decimal places.

        Details:
            - The number before the percentage sign can be an integer or a floating-point number.
            - The result is rounded to three decimal places.

        """

        matches = re.findall(r'(\d+\.?\d*)%', self.expression)
        for match in matches:
            num_str = match
            num1 = float(num_str)
            self.expression = self.expression.replace(f"{num_str}%", str(num1/100))

        return self

    def evaluate_double_operators(self):
        """
        Validates and simplifies consecutive operators in the expression.

        This function performs two main tasks:
        1. It checks for invalid consecutive occurrences (two or more) of certain operators,
           and raises a ValueError if any are found:
               - Multiple square roots (e.g., √√)
               - Multiple factorials (e.g., !!)
               - Multiple multiplication signs (e.g., ** or more)
               - Multiple division signs (e.g., // or more)
               - Multiple percentage signs (e.g., %% or more)

        2. It simplifies sequences of consecutive '+' and '-' signs into a single '+' or '-'
           depending on the count of negative signs. For example:
               -- becomes +
               -+- becomes +
               +-+ becomes -

        Example:
            Expression "3--2++4" becomes "3+2+4"
        """

        patterns = {
            r'√{1,}': 'double or more square root',
            r'\^{2,}': 'double or more power',
            r'!{1,}': 'double or more factorial',
            r'\*{2,}': 'double or more multiplication',
            r'/{2,}': 'double or more division',
            r'%{1,}': 'double or more division',
        }
        for pattern, description in patterns.items():
            if re.search(pattern, self.expression):
                raise ValueError(f"Error: {description} is not allowed")

        self.expression = re.sub(
            r'[+\-]+',
            lambda m: '+' if m.group(0).count('-') % 2 == 0 else '-',
            self.expression
        )

        return self

    def evaluate_multiplication_and_division(self):
        """
        Evaluates multiplication '*' and division '/' operations in the expression.

        It tokenizes the expression, processes each '*' and '/' operation by performing
        the corresponding mathematical operation, and updates the expression with the results.

        Returns:
            The modified expression with resolved multiplication and division.
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
                    del tokens[i + 1:i + 2]
                else:
                    right = float(tokens[i + 1])

                if operator == '*':
                    result = MathLib.multiply(left, right)
                elif operator == '/':
                    if right == 0:
                        raise ZeroDivisionError("Error: Division by zero")
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
        """
        Evaluates addition '+' and subtraction '-' operations in the expression.

        It tokenizes the expression, processes each '+' and '-' operation by performing
        the corresponding mathematical operation, and updates the result.

        Returns:
            The final result after performing the addition and subtraction operations.
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
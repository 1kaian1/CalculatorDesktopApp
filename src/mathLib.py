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

# mathlib.py - knihovna pro základní matematické operace

import re


# Základní matematické operace

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Nelze dělit nulou.")
    return a / b


def divide_with_remainder(a, b):
    if b == 0:
        raise ZeroDivisionError("Nelze dělit nulou.")
    return divmod(a, b)


def factorial(n):
    if n < 0:
        raise ValueError("Faktoriál je definován pouze pro nezáporná čísla.")
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def power(base, exponent):
    return base ** exponent


def sqrt(x, degree=2):
    # Pro výpočet odmocniny
    if x < 0 and degree % 2 == 0:
        raise ValueError("Záporné číslo nemá reálnou odmocninu při sudém odmocniteli.")
    return x ** (1 / degree)


def evaluate_expression(expression):
    # Nejprve musíme nahradit všechny výskyty odmocniny
    expression = re.sub(r'(\d*)√(\d+)', lambda m: str(sqrt(float(m.group(2)), int(m.group(1)) if m.group(1) else 2)),
                        expression)

    # Nahradíme faktoriály (např. 5! -> 120)
    expression = re.sub(r'(\d+)!', lambda m: str(factorial(int(m.group(1)))), expression)

    # První krok je zjistit, jestli je zde záporné číslo před odmocninou
    # Zpracujeme to jako "n√x" před tím, než použijeme jakékoli operátory
    if expression.startswith('-'):
        expression = '0' + expression  # Pokud začíná "-" přidáme nulu před záporné číslo, aby bylo možné vyhodnotit jako nulu + číslo

    # Tokenizace výrazu pro operátory a čísla
    tokens = re.findall(r'\d+\.\d+|\d+|[-+*/]', expression)

    # Nejprve vyřešíme násobení a dělení
    i = 0
    while i < len(tokens):
        if tokens[i] == '*' or tokens[i] == '/':
            left = float(tokens[i - 1])  # Předchozí číslo
            operator = tokens[i]
            right = float(tokens[i + 1])  # Následující číslo

            if operator == '*':
                result = multiply(left, right)
            elif operator == '/':
                result = divide(left, right)

            tokens[i - 1] = result
            del tokens[i:i + 2]  # Odstranění operátoru a pravého čísla
            i -= 1  # Vrátili jsme se zpět, abychom zkontrolovali, jestli zůstaly nějaké operátory na tomto místě
        else:
            i += 1

    # Poté vyřešíme sčítání a odčítání
    i = 1
    result = float(tokens[0])
    while i < len(tokens):
        operator = tokens[i]
        next_number = float(tokens[i + 1])

        if operator == '+':
            result = add(result, next_number)
        elif operator == '-':
            result = subtract(result, next_number)

        i += 2

    # Pokud je výsledek celé číslo (např. 5.0), převedeme na int
    if result.is_integer():
        return str(int(result))

    # Pokud není celé číslo, vrátíme výsledek zaokrouhlený na 2 desetinná místa
    return str(round(result, 2))

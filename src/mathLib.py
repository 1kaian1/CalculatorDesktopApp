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
#import gui

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class ExpressionTree:
    def __init__(self):
        self.root = None
        self.values = []
        self.operators = []

    def reset_tree(self):
        self.root = None
        self.values = []
        self.operators = []

    def is_operator(self, value):
        return value in ['+', '-', '*', '/']

    def precedence(self, operator):
        if operator in ['+', '-']:
            return 1

        if operator in ['*', '/']:
            return 2

        return 0

    def add_value(self, value):
        if isinstance(value, int):
            self.values.append(Node(value))

        elif self.is_operator(value):
            while self.operators and self.precedence(self.operators[-1]) >= self.precedence(value):
                self.apply_operator()

            self.operators.append(value)

    def apply_operator(self):
        operator = self.operators.pop()
        right = self.values.pop()
        left = self.values.pop()
        node = Node(operator)
        node.left = left
        node.right = right
        self.values.append(node)

    def finalize_tree(self):
        while self.operators:
            self.apply_operator()

        self.root = self.values[-1] if self.values else None

    def evaluate(self, node):
        if node.left is None and node.right is None:
            return node.value

        left_val = self.evaluate(node.left)
        right_val = self.evaluate(node.right)

        if node.value == '+':
            return left_val + right_val
        elif node.value == '-':
            return left_val - right_val
        elif node.value == '*':
            return left_val * right_val
        elif node.value == '/':
            if right_val == 0:
                return str("Deleni nulou")
            return left_val / right_val

    def evaluate_expression(self):
        if not self.root:
            return 0\

        return self.evaluate(self.root)
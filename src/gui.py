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

# Copyright (c) 2025 Jan Frantisek Levicek, xlevic02
# Copyright (c) 2025 Jakub Sebela, xsebelj00

import sys

from PySide6 import QtCore
from PySide6.QtCore import QEvent, Qt, QCoreApplication, QTimer
from PySide6.QtGui import QFont, Qt, QKeyEvent
from PySide6.QtWidgets import QWidget, QLineEdit, QVBoxLayout, QHBoxLayout, QPushButton, QApplication
from mathLib import evaluate_expression




class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        print("Inicializace proběhla správně!")

        self.setWindowTitle("Kalkulačka")
        self.setGeometry(100, 100, 300, 400)

        self.expression_field = QLineEdit(self)
        self.expression_field.setReadOnly(True)
        self.expression_field.setAlignment(Qt.AlignmentFlag.AlignRight)

        self.result_field = QLineEdit(self)
        self.result_field.setReadOnly(True)
        self.result_field.setAlignment(Qt.AlignmentFlag.AlignRight)

        font = QFont()
        font.setPointSize(14)
        self.expression_field.setFont(font)
        font.setPointSize(24)
        self.result_field.setFont(font)

        self.expression_field.setFocusPolicy(Qt.NoFocus)
        self.expression_field.setStyleSheet("border: none; background: transparent;")
        self.expression_field.setFixedHeight(30)

        self.main_layout = QVBoxLayout(self)
        self.button_layout = QVBoxLayout()
        self.main_layout.addWidget(self.expression_field)
        self.main_layout.addWidget(self.result_field)
        self.main_layout.addLayout(self.button_layout)

        self.buttons = [
            ['7', '8', '9', '/', 'C'],
            ['4', '5', '6', '*', 'CE'],
            ['1', '2', '3', '-', '√'],
            ['0', '.', '=', '+', '!']
        ]

        for row in self.buttons:
            row_layout = QHBoxLayout()
            for btn_text in row:

                button = QPushButton(btn_text)
                button.click()

                button_font = QFont()
                button_font.setPointSize(18)
                button.setFont(button_font)

                button.setFixedSize(60, 60)

                button.clicked.connect(self.on_button_click)
                row_layout.addWidget(button)

            self.button_layout.addLayout(row_layout)

        self.result_text = '0'
        self.result_field.setText(self.result_text)
        self.expression_text = ''
        self.override_result_text = False
        self.last_sender_expression = ''
        self.last_sender_text = ''
        self.key_pressed = ''
        self.enter_clicked = False

        self.key = None




    def on_button_click(self):
        button = self.sender()
        if button is not None:
            self.handle_input(button.text())

    def handle_input(self, key_pressed):

        button_operators = ['+', '-', '*', '/', '^']
        button_numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

        if key_pressed in button_numbers:
            print("KEY IN NUMBERS")

            if self.enter_clicked:
                self.result_text += key_pressed
                self.expression_text = ''
            if self.override_result_text:
                self.result_text = key_pressed
                self.override_result_text = False
            else:
                self.result_text += key_pressed
                print("RESULT CHANGED:", self.result_text)

            self.enter_clicked = False

        elif key_pressed in button_operators:  # co se stříškou?
            print("KEY IN BUTTONS")
            self.enter_clicked = False

            if self.expression_text == '':
                self.expression_text = '0'
                self.expression_text += key_pressed
            elif self.expression_text == '' and self.result_text != '':
                self.expression_text = self.result_text
                self.expression_text += key_pressed
            elif self.expression_text[-1] not in ['+', '-', '*', '/']:
                if self.expression_text[-1] == '=':
                    self.expression_text = self.expression_text[:-1]
                self.expression_text += self.result_text
                self.expression_text = evaluate_expression(self.expression_text)
                self.result_text = self.expression_text
                self.expression_text += key_pressed
                self.override_result_text = True
            else:
                self.expression_text[-1] = key_pressed

        elif key_pressed == '=':

            self.enter_clicked = True

            if self.last_sender_text in button_operators:
                self.expression_text += self.result_text
                self.result_text = evaluate_expression(self.expression_text)
                self.expression_text += '='
            elif self.enter_clicked:
                self.expression_text = self.result_text + self.last_sender_expression
                self.result_text = evaluate_expression(self.expression_text)
                self.expression_text += '='
            else:
                self.expression_text += self.result_text
                self.result_text = self.expression_text
                self.result_text = evaluate_expression(self.result_text)
                self.expression_text += '='

        elif key_pressed == 'backspace':
            print("BACKSPACE")
            self.result_text = self.result_text[:-1]

        # elif button == 'C':
        #    pass
        # elif button == 'CE':
        #    pass

        self.result_field.setText(self.result_text)
        self.expression_field.setText(self.expression_text)

        if self.last_sender_expression in button_operators and self.key_pressed not in button_operators:
            self.last_sender_expression += self.key_pressed
        elif self.last_sender_expression in button_operators and self.key_pressed in button_operators:
            self.last_sender_expression = self.key_pressed

        self.last_sender_text = self.key_pressed

    def keyPressEvent(self, event: QKeyEvent):
        key = event.text()
        print("KEY EVENT:", key)
        if key.isdigit() or key in "+-*/.=C":
            self.handle_input(key)
        elif event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return:
            self.handle_input('=')
        elif event.key() == Qt.Key_Backspace:
            event.accept()
            print("backspace")
            if self.result_text != '':
                self.result_text = self.result_text[:-1]
                self.result_field.setText(self.result_text)
        else:
            super().keyPressEvent(event)
        event.accept()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    sys.exit(app.exec())

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
# Copyright (c) 2025 Jan Kai Marek, xmarekj00;

import sys

from PySide6.QtCore import QRegularExpression, Qt
from PySide6.QtGui import QFont, QRegularExpressionValidator, QIcon
from PySide6.QtWidgets import QWidget, QLineEdit, QVBoxLayout, QPushButton, QApplication, QGridLayout, QSizePolicy

from mathLib import MathLib


class GUI(QWidget):

    def __init__(self):

        # Calling QWidget constructor
        super().__init__()

        # Setting window title
        self.setWindowTitle("Kalkulačka")

        # Creating value_field (where the expression is written)
        self.value_field = QLineEdit(self)

        # Setting limitations on value_field inputs using regex
        regex = QRegularExpression("[0-9+*/\\-!%().^√]+")
        validator = QRegularExpressionValidator(regex, self.value_field)
        self.value_field.setValidator(validator)

        # Connecting value field to on_text_changed listener
        self.value_field.textChanged.connect(lambda: self.on_text_changed())

        # Connecting value field to on_cursor_position_changed listener
        self.value_field.cursorPositionChanged.connect(self.on_cursor_position_changed)

        # Creating backup for expression, used after evaluation
        self.value_field_equation_preserved = ""

        # Stores recent expression for caret-aware editing
        self.value_field_instant_history = ""

        # Creating main layout
        self.main_layout = QVBoxLayout(self)

        # Adding value_field to layout
        self.main_layout.addWidget(self.value_field)

        # Creating layout for buttons
        self.button_layout = QGridLayout()

        # Adding buttons layout into main layout
        self.main_layout.addLayout(self.button_layout)

        # Defining calculator buttons
        self.buttons = [
            ['^', '!', 'C', '⌫'],
            ['(', ')', '√', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['%', '0', '.', '=']
        ]

        # Creating and adding buttons into layout
        for row_index, row in enumerate(self.buttons):
            for col_index, btn_text in enumerate(row):
                button = QPushButton(btn_text, self)

                # Expands to available space
                button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
                button.setMinimumSize(70, 70)

                # Setting font and size
                button_font = QFont()
                button_font.setPointSize(20)
                button.setFont(button_font)

                # Adding button into layout
                self.button_layout.addWidget(button, row_index, col_index)
                button.clicked.connect(self.on_button_click)

        # True if result was recently evaluated, used for result post-processing
        self.result_flag = False

        # Setting dark UI theme
        self.setStyleSheet("""
            QWidget {
            background-color: #1e1e1e;
            }

            QLineEdit {
            background-color: #121212;
            color: #ffffff;
            border: 1px solid #444444;
            border-radius: 6px;
            padding: 10px;
            }

            QPushButton {
            background-color: #333333;
            color: #ffffff;
            border-radius: 10px;
            font-size: 20px;
            padding: 15px;
            }

            QPushButton:hover {
            background-color: #4d4d4d;
            }

            QPushButton:pressed {
            background-color: #666666;
            }

            QPushButton:disabled {
            background-color: #2c2c2c;
            color: #555555;
            }
        """)

    def on_button_click(self):
        r"""
        Called when any button is clicked.

        Performs various actions depending on button label:
        - "=" evaluates expression.
        - "C" clears input.
        - "⌫" deletes character at cursor.
        - Otherwise, inserts clicked character at cursor.
        """

        button = self.sender()

        if button.text() == "=":

            # Evaluate expression only if not empty
            if self.value_field.text() != "":
                self.value_field_equation_preserved = self.value_field.text()
                result = MathLib(self.value_field.text()).evaluate_expression()
                self.value_field.setText(result)
                self.result_flag = True

        elif button.text() == "C":

            # Clear input and reset flag
            self.result_flag = False
            self.value_field.setText("")

        elif button.text() == "⌫":

            # Delete character before cursor or clear field if result was just shown
            if self.result_flag:
                self.value_field.setText("")
                self.result_flag = False
            else:
                current_text = self.value_field.text()
                cursor_position = self.value_field.cursorPosition()

                text_before_cursor = current_text[:cursor_position]
                text_after_cursor = current_text[cursor_position:]

                new_text = text_before_cursor[:-1] + text_after_cursor
                self.value_field.setText(new_text)
                self.value_field.setCursorPosition(cursor_position - 1)

        else:

            # Insert character at current cursor position
            current_text = self.value_field.text()
            cursor_position = self.value_field.cursorPosition()

            text_before_cursor = current_text[:cursor_position]
            text_after_cursor = current_text[cursor_position:]

            new_text = text_before_cursor + button.text() + text_after_cursor
            self.value_field.setText(new_text)
            self.value_field.setCursorPosition(cursor_position + 1)

        # Ensure cursor stays in value_field
        self.value_field.setFocus()

    def on_text_changed(self):
        r"""
        Called when value_field text changes.

        Manages:
        - After-evaluation state,
        - Basic input restrictions.
        """

        text = self.value_field.text()
        if text == "":
            self.result_flag = False

        # Managing user input after a result was evaluated
        if self.result_flag:

            if text == self.value_field_instant_history[:-1]:
                self.value_field.setText("")

            elif text[-1].isdigit():

                # Start new equation with digit
                self.value_field.blockSignals(True)
                self.value_field.setText(text[-1])
                self.value_field.blockSignals(False)

            elif text[:5] == "Error":

                # Clear error message
                self.value_field.blockSignals(True)
                self.value_field.setText("")
                self.value_field.blockSignals(False)

            # Result flag reset once user starts editing
            self.result_flag = False

        self.value_field_instant_history = self.value_field.text()

    def on_cursor_position_changed(self, old_pos, new_pos):

        # Managing the after-evaluation care

        # This function is needed to restrict user's interfering with printed "Error" message. With any cursor
        # position change the value_field_equation_preserved is printed on the screen, enabling the user to correct the equation

        # Result is printed and we are choosing what do to next
        if self.result_flag:

            # Safely giving value_field the value_field_equation_preserved with blockSignals() to avoid infinite recursion and
            # interfering between on_text_changed and on_cursor_position_changed
            self.value_field.blockSignals(True)
            self.value_field.setText(self.value_field_equation_preserved)
            self.value_field.blockSignals(False)

            # result_flag set to false, because we are no more in the state of printing results
            self.result_flag = False

    def keyPressEvent(self, event):

        # This function is only needed to handle the enter-pressed event

        # If enter (16777220) is pressed, evaluate, print result
        if event.key() == 16777220 and self.value_field.text() != "":

            self.value_field_equation_preserved = self.value_field.text()
            new_text = MathLib(self.value_field.text()).evaluate_expression()
            self.value_field.setText(new_text)
            self.result_flag = True

        # ChatGPT said this should be here
        super().keyPressEvent(event)

    def resizeEvent(self, event):

        # ChatGPT said this should be here
        super().resizeEvent(event)

        # Change font size based on window height
        window_height = self.height()

        # If the window height is greater than 600, set font size to 48
        if window_height > 600:

            font = QFont()
            font.setPointSize(48)
            self.value_field.setFont(font)

        # Else set font size to 36
        else:

            font = QFont()
            font.setPointSize(36)
            self.value_field.setFont(font)

if __name__ == '__main__':

    app = QApplication(sys.argv)
    calculator = GUI()
    calculator.show()
    sys.exit(app.exec())


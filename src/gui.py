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

import tkinter as tk
from mathLib import ExpressionTree

class GUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Kalkulacka")
        self.root.geometry("600x900+100+200")
        self.root.resizable(False, False)
        self.root.configure(bg = "#DDDDDD")

        self.buttonWidth = 4
        self.buttonHeight = 2
        self.buttonColor = "#000000"
        self.textColor = "#FFFFFF"
        self.font = ("arial", 30)
        self.buttonX = (15, 165, 315, 465)
        self.buttonY = (220, 340, 460, 580, 700)

        self.equation_text = ""
        self.equation_memory_text = ""
        self.equation_label = tk.StringVar()
        self.equation_memory_label = tk.StringVar()

        self.tree = ExpressionTree()

        self.setup_ui()

    def setup_ui(self):
        # Pametovy label
        self.memory_label = tk.Label(self.root, textvariable = self.equation_memory_label, width = 20, height = 2, font = ("arial", 20), bg = "#CCCCCC")
        self.memory_label.place(x = 245, y = 50)

        # Vypisovy label
        self.label = tk.Label(self.root, textvariable = self.equation_label, width = 23, height = 2, font = self.font, bg = "#7cc7a9")
        self.label.place(x = 10, y = 100)

        # Vsechna hlavni tlacitka
        buttons = [
            ("!", 0, 0), ("xⁿ", 1, 0), ("ˣ√n", 2, 0), ("%", 3, 0),
            ("7", 0, 1), ("8", 1, 1), ("9", 2, 1), ("/", 3, 1),
            ("4", 0, 2), ("5", 1, 2), ("6", 2, 2), ("*", 3, 2),
            ("1", 0, 3), ("2", 1, 3), ("3", 2, 3), ("-", 3, 3),
            ("0", 0, 4), (".", 1, 4), ("=", 2, 4), ("+", 3, 4)
        ]

        for (text, col, row) in buttons:
            if text == "=":
                command = self.calculate
            else:
                command = lambda val = text: self.button_press(val)

            tk.Button(self.root, text = text, command = command,
                      width = self.buttonWidth, height = self.buttonHeight,
                      fg = self.textColor, bg = self.buttonColor,
                      font = self.font).place(x = self.buttonX[col], y = self.buttonY[row])

        # Tlacitka C a CE
        tk.Button(self.root, text = "C", width = 2, height = 1, fg = "red", bg = "#FFFFFF",
                  font = self.font, command = self.clear).place(x = 165, y = 825)
        tk.Button(self.root, text = "CE", width = 2, height = 1, fg = "red", bg = "#FFFFFF",
                  font = self.font, command = self.clear_entry).place(x = 315, y = 825)


    def button_press(self, value):
        if value in ["+", "-", "*", "/"] and self.equation_text != "":
            self.equation_memory_text += self.equation_text + value

            number = float(self.equation_text) if '.' in self.equation_text else int(self.equation_text)
            self.tree.add_value(number)
            self.tree.add_value(value)
            self.equation_memory_label.set(self.equation_memory_text)
            self.equation_text = ""
            self.equation_label.set("")

        elif value == "-" and self.equation_text == "" or value not in ["+", "*", "/"]:
            self.equation_text += str(value)
            self.equation_label.set(self.equation_text)

        else:
            self.equation_label.set("Chybejici cislo")
            self.equation_text = ""


    def clear_entry(self):
        self.equation_text = ""
        self.equation_label.set("")

    def clear(self):
        self.equation_text = ""
        self.equation_label.set("")
        self.equation_memory_text = ""
        self.equation_memory_label.set("")
        print("Clearing")

    def calculate(self):
        if self.equation_text:
            number = float(self.equation_text) if '.' in self.equation_text else int(self.equation_text)
            self.tree.add_value(number)

        try:
            self.tree.finalize_tree()
            root_node = self.tree.root
            result = str(self.tree.evaluate(root_node))

            if result == "Deleni nulou":
                self.equation_label.set("Deleni nulou")
                self.equation_text = ""
            else:
                self.equation_label.set(result)
                self.equation_text = result
                self.equation_memory_text = ""
                self.equation_text = ""
                self.equation_memory_label.set("")

        except:
            self.equation_label.set("Error")
            self.equation_text = ""



if __name__ == "__main__":
    root = tk.Tk()
    app = GUI(root)
    root.mainloop()

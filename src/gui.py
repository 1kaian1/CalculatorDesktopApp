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

class GUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Kalkulacka")
        self.root.geometry("600x800+100+200")
        self.root.resizable(False, False)
        self.root.configure(bg = "#DDDDDD")

        self.buttonWidth = 4
        self.buttonHeight = 2
        self.buttonColor = "#000000"
        self.textColor = "#FFFFFF"
        self.font = ("arial", 30)
        self.buttonX = (15, 165, 315, 465)
        self.buttonY = (135, 255, 375, 495, 615)

        self.equation_text = ""
        self.equation_label = tk.StringVar()

        self.setup_ui()

    def setup_ui(self):
        # Vypisovy label
        self.label = tk.Label(self.root, textvariable = self.equation_label, width = 23, height = 2, font = self.font, bg = "#7cc7a9")
        self.label.place(x = 12, y = 12)

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
                  font = self.font, command = self.clear).place(x = 165, y = 735)
        tk.Button(self.root, text = "CE", width = 2, height = 1, fg = "red", bg = "#FFFFFF",
                  font = self.font, command = self.clear).place(x = 315, y = 735)


    def button_press(self, value):
        self.equation_text += str(value)
        self.equation_label.set(self.equation_text)

    def clear(self):
        self.equation_text = ""
        self.equation_label.set("")

    def calculate(self):
        try:
            result = str(eval(self.equation_text))
            self.equation_label.set(result)
            self.equation_text = result
        except:
            self.equation_label.set("Error")
            self.equation_text = ""



if __name__ == "__main__":
    root = tk.Tk()
    app = GUI(root)
    root.mainloop()

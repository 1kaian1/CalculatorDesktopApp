import unittest
import tkinter as tk
import gui

class TestGUI(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()
        self.root.withdraw()
        self.app = gui.GUI(self.root)

    def tearDown(self):
        self.root.destroy()

    def updateGui(self):
        self.root.update_idletasks()
        self.root.update()

    def input_expression(self, expr):
        for char in expr:
            self.app.button_press(char)

    def test_initial_state(self):
        self.assertEqual(self.app.equation_text, "")
        self.assertEqual(self.app.equation_label.get(), "")

    # TODO: jak otestovat C a CE button?
    def test_clear(self):
        # Clear pomoci C buttonu
        for char in "123":
            self.app.button_press(char)
        self.app.clear()
        self.updateGui()
        self.assertEqual(self.app.equation_text, "")
        self.assertEqual(self.app.equation_label.get(), "")

        # Clear pomoci CE
        for char in "123":
            self.app.button_press(char)
        self.app.clear()
        self.updateGui()
        self.assertEqual(self.app.equation_text, "")
        self.assertEqual(self.app.equation_label.get(), "")

    def test_button_press_adds_number(self):
        test_cases = {
            "7": "7",
            "123": "123",
            "1+3": "1+3",
            "1.2": "1.2",
        }

        for expr, expected in test_cases.items():
            with self.subTest(expr = expr):
                self.input_expression(expr)
                self.assertEqual(self.app.equation_text, expected)
                self.assertEqual(self.app.equation_label.get(), expected)
                self.app.clear()

    # TODO: vypocet 1.3-1.2 se zobrazi jako 0.10000000000000009
    def test_calculate_simple_expression(self):
        test_cases = {
            "2+3": "5",
            "3-2": "1",
            "2*3": "6",
            "6/2": "3",
            "3/2": "1.5",
            "1.2+1.3": "2.5",
            "1.3-1.2": "0.1",
            "1.5*1.5": "2.25",
            "2.5/1.25": "2.0",
            "2.5/2": "1.25",
        }

        for expr, expected in test_cases.items():
            with self.subTest(expr = expr):
                self.input_expression(expr)
                self.app.calculate()
                self.updateGui()
                result = self.app.equation_label.get()
                try:
                    self.assertAlmostEqual(float(result), float(expected), places=6)
                except ValueError:
                    self.assertEqual(result, expected)
                self.app.clear()

    def test_calculate_divide_by_zero(self):
        expressions = ["1/0", "2.5/0"]
        for expr in expressions:
            with self.subTest(expr=expr):
                self.input_expression(expr)
                self.app.calculate()
                self.updateGui()
                self.assertEqual(self.app.equation_label.get(), "Error")
                self.app.clear()

    def test_invalid_input(self):
        invalid_expressions = [
            "2+", "3-", "2*", "3/", "*2", "/3",
            "2+++2", "2+-+2", "2-+-2", "2---2",
            "2**2", "2*/2", "2//2",
            "1..1", "1.2.3", "..1"
        ]

        for expr in invalid_expressions:
            with self.subTest(expr=expr):
                self.input_expression(expr)
                self.app.calculate()
                self.updateGui()
                self.assertEqual(self.app.equation_label.get(), "Error")
                self.app.clear()

    # TODO: vypocet .1*.1 se zobrazi jako 0.010000000000000002
    def test_valid_input(self):
        test_cases = {
            ".1": "0.1",
            "1.": "1.0",
            "-.1": "-0.1",
            "-1.": "-1.0",
            "+.1": "0.1",
            "+1.": "1.0",
            ".1+.1": "0.2",
            ".1-.1": "0.0",
            ".1*.1": "0.01",
            ".1/.1": "1.0",
            "1.+1.": "2.0",
            "1.-1.": "0.0",
            "1.*1.": "1.0",
            "1./1.": "1.0",
        }

        for expr, expected in test_cases.items():
            with self.subTest(expr = expr):
                self.input_expression(expr)
                self.app.calculate()
                self.updateGui()
                result = self.app.equation_label.get()
                try:
                    self.assertAlmostEqual(float(result), float(expected), places=6)
                except ValueError:
                    self.assertEqual(result, expected)
                self.app.clear()

    def test_repeated_equation(self):
        test_cases = {
            "2+2": "4",
            "2-2": "0",
            "2*2": "4",
            "2/2": "1",
        }

        for expr, expected in test_cases.items():
            with self.subTest(expr = expr):
                self.input_expression(expr)
                self.app.calculate()
                self.updateGui()
                result = self.app.equation_label.get()
                try:
                    self.assertAlmostEqual(float(result), float(expected), places=6)
                except ValueError:
                    self.assertEqual(result, expected)
                self.app.calculate()
                self.updateGui()
                result = self.app.equation_label.get()
                try:
                    self.assertAlmostEqual(float(result), float(expected), places=6)
                except ValueError:
                    self.assertEqual(result, expected)
                self.app.clear()

if __name__ == '__main__':
    unittest.main()

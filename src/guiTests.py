import unittest
import tkinter as tk
import gui

class TestGUI(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()
        self.app = gui.GUI(self.root)

    def tearDown(self):
        self.root.destroy()

    def test_initial_state(self):
        self.assertEqual(self.app.equation_text, "")
        self.assertEqual(self.app.equation_label.get(), "")

    def test_button_press_adds_number(self):
        self.app.button_press("7")
        self.assertEqual(self.app.equation_text, "7")
        self.assertEqual(self.app.equation_label.get(), "7")

    def test_clear(self):
        self.app.button_press("123")
        self.app.clear()
        self.assertEqual(self.app.equation_text, "")
        self.assertEqual(self.app.equation_label.get(), "")

    def test_calculate_simple_expression(self):
        self.app.button_press("2")
        self.app.button_press("+")
        self.app.button_press("3")
        self.app.calculate()
        self.assertEqual(self.app.equation_label.get(), "5")

    def test_calculate_divide_by_zero(self):
        self.app.button_press("1/0")
        self.app.calculate()
        self.assertEqual(self.app.equation_label.get(), "Error")


if __name__ == '__main__':
    unittest.main()

import unittest
import tkinter as tk
import gui_remade

class TestGUI(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()
        self.app = gui_remade.GUI(self.root)

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
        for char in "123":
            self.app.button_press(char)
        self.app.clear()
        self.assertEqual(self.app.equation_text, "")
        self.assertEqual(self.app.equation_label.get(), "")

    def test_calculate_simple_expression(self):
        for char in "2+3":
            self.app.button_press(char)
        self.app.calculate()
        self.assertEqual(self.app.equation_label.get(), "5")

    def test_calculate_divide_by_zero(self):
        for char in "1/0":
            self.app.button_press(char)
        self.app.calculate()
        self.assertEqual(self.app.equation_label.get(), "Error")


if __name__ == '__main__':
    unittest.main()

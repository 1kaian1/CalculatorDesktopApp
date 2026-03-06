Calculator App & Statistical Tool
A professional-grade Python desktop application providing a full graphical calculator interface and a specialized command-line utility for statistical calculations.

🚀 Features
Graphical User Interface: Modern, responsive dark-themed UI built with PySide6 (Qt).

Smart Expression Engine: A custom-implemented math library in mathLib.py that parses complex expressions (including parentheses and operator precedence) without using eval().

Standard Deviation Utility: A dedicated CLI tool (stddev.py) for computing sample standard deviation using the numerically stable Welford's algorithm.

Robust Testing: Extensive unit tests for the arithmetic engine and statistical accuracy.

🛠️ Requirements
Python 3.8+

PySide6 (Qt for Python)

To install the necessary library, run:
pip install PySide6

📖 Usage
1. Graphical Calculator
To launch the main desktop application:
python main.py

2. Standard Deviation Tool (CLI)
The tool calculates sample standard deviation from numbers provided via standard input (stdin):
echo "10 20 30 40 50" | python stddev.py

OR
python stddev.py < data_input.txt

3. Running Unit Tests
To verify all mathematical components and edge cases:
python -m unittest mathLibTests.py
python -m unittest std_devTests.py

📁 Project Structure
main.py - Entry point for the application.

gui.py - UI design, button mapping, and responsive scaling logic.

mathLib.py - Mathematical engine and expression parser.

stddev.py - CLI statistical module.

mathLibTests.py - Test suite for the calculator engine.

std_devTests.py - Test suite for the statistical utility.

⚖️ License
This project is licensed under the GNU General Public License v3.0.

Copyright (c) 2025
Jan Kai Marek, Jan František Levíček, Tomáš Kudrna, Jakub Šebela.

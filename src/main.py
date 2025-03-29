# main.py
import sys
from PySide6.QtWidgets import QApplication
from gui import TextInputApp  # Importování třídy TextInputApp z gui.py


def main():
    app = QApplication(sys.argv)

    # Vytvoření instance GUI
    window = TextInputApp()

    # Příklad odeslání vstupu z main.py do gui.py



    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()

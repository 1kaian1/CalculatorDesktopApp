from PySide6.QtWidgets import QGridLayout, QLabel, QPushButton, QWidget, QLineEdit, QVBoxLayout
from PySide6.QtCore import QRegularExpression
from PySide6.QtGui import QRegularExpressionValidator

class TextInputApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Text Input with Buttons 1-9 and Operators")
        self.setGeometry(100, 100, 400, 400)

        self.layout = QVBoxLayout()

        # Vytvoření labelu
        self.label = QLabel("Enter up to 50 characters:", self)
        self.layout.addWidget(self.label)

        # Vytvoření textového pole
        self.text_input = QLineEdit(self)
        self.text_input.setMaxLength(50)  # Nastavení maximální délky textu na 50 znaků

        # Regulární výraz pro povolení čísel, desetinné čárky a operátorů +,-,*,/
        regex = QRegularExpression(r"^[0-9+\-*/.]*$")  # Tento regex povolí čísla a operátory
        validator = QRegularExpressionValidator(regex)

        # Nastavení validátoru pro QLineEdit
        self.text_input.setValidator(validator)

        # Nastavení placeholderu pro QLineEdit
        self.text_input.setPlaceholderText("Zadejte čísla, operátory +,-,*,/ nebo desetinnou čárku.")
        self.layout.addWidget(self.text_input)

        # Připojení signálu textChanged k metodě pro tisk textu do konzole
        self.text_input.textChanged.connect(self.print_text_input)

        # Vytvoření mřížky pro tlačítka
        grid_layout = QGridLayout()

        # Vytvoření tlačítek 1-9 a operátorů
        buttons = [QPushButton(str(i)) for i in range(1, 10)] + [QPushButton(op) for op in ["+", "-", "*", "/"]]

        # Umístění tlačítek do mřížky
        for i, button in enumerate(buttons):
            row = i // 3
            col = i % 3
            grid_layout.addWidget(button, row, col)
            button.clicked.connect(self.button_clicked)

        self.layout.addLayout(grid_layout)
        self.setLayout(self.layout)

    def button_clicked(self):
        button = self.sender()  # Získání tlačítka, které bylo stisknuto
        current_text = self.text_input.text()  # Aktuální text v poli
        new_text = current_text + button.text()  # Přidání textu tlačítka
        if len(new_text) <= 50:  # Pokud není text delší než 50 znaků
            self.text_input.setText(new_text)

    # Metoda pro přijímání vstupů z main.py
    def update_text_input(self, text):
        current_text = self.text_input.text()
        new_text = current_text + text
        if len(new_text) <= 50:
            self.text_input.setText(new_text)

    # Funkce pro tisk aktuálního textu v text_input do konzole
    def print_text_input(self):
        print(self.text_input.text())  # Tiskne obsah textového pole do konzole

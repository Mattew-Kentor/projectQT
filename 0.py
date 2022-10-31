import sys

from PyQt5.QtWidgets import QApplication, QHBoxLayout, QPushButton, QMainWindow, QWidget, QSizePolicy


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.buttons = []
        self.lay = QHBoxLayout()
        alphabet = "АБВГДЕЁЖЗИЙКЛМНОПРСТУЙХЦЧШЩЪЫЬЭЮЯ"
        for letter in range(len(alphabet)):
            self.buttons.append(QPushButton(alphabet[letter], self))
            self.buttons[letter].setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
            self.buttons[letter].setMaximumSize(20, 20)
            self.lay.addWidget(self.buttons[letter])
        self.setLayout(self.lay)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
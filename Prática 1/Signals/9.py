# Use o sinal textChanged de um QLineEdit e emita-o com uma string vazia.

import sys
from PySide6.QtCore import Signal
from PySide6.QtWidgets import QApplication, QLineEdit, QMainWindow

class MainWindow(QMainWindow):

    def __init__ (self):
        super().__init__()
        self.campo = QLineEdit()

app = QApplication(sys.argv)
window = MainWindow()
window.campo.textChanged.emit("")
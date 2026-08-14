import sys
from PySide6.QtCore import Signal
from PySide6.QtWidgets import QApplication, QMainWindow

class MainWindow(QMainWindow):
    meu_sinal = Signal()

    def __init__(self):
        super().__init__()
        self.meu_sinal.emit()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QRadioButton
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Slot com QRadioButton")

        self.radio = QRadioButton("Fundo vermelho")

        self.radio.toggled.connect(self.alternar_cor)

        layout = QVBoxLayout()
        layout.addWidget(self.radio)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.alternar_cor(False)  # define cor inicial

    def alternar_cor(self, marcado: bool):
        if marcado:
            self.setStyleSheet("background-color: red;")
        else:
            self.setStyleSheet("background-color: black;")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
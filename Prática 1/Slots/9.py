import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Slot com contador")

        self.contador = 0

        self.label = QLabel(f"Contador: {self.contador}")
        self.botao = QPushButton("Incrementar")

        self.botao.clicked.connect(self.incrementar_contador)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.botao)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def incrementar_contador(self):
        self.contador += 1
        self.label.setText(f"Contador: {self.contador}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
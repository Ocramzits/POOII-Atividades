import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QTextEdit, QPushButton
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Slot para limpar QTextEdit")

        self.texto = QTextEdit()
        self.botao_limpar = QPushButton("Limpar")

        self.botao_limpar.clicked.connect(self.limpar_texto)

        layout = QVBoxLayout()
        layout.addWidget(self.texto)
        layout.addWidget(self.botao_limpar)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def limpar_texto(self):
        self.texto.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
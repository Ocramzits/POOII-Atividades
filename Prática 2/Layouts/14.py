import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QTextEdit, QPushButton
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QVBoxLayout com stretch=2")
        self.setFixedSize(400, 300)

        layout = QVBoxLayout()

        botao = QPushButton("Botão (stretch padrão)")
        texto = QTextEdit()
        texto.setPlaceholderText("Área de texto (stretch=2, ocupa mais espaço)")

        layout.addWidget(botao)
        layout.addWidget(texto, 2)  # segundo argumento é o stretch factor

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
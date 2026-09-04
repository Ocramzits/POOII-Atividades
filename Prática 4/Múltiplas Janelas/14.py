import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QLineEdit, QVBoxLayout, QWidget, QLabel
)


class JanelaComTexto(QMainWindow):
    def __init__(self, texto_recebido: str):
        super().__init__()
        self.setWindowTitle("Janela com texto recebido")
        self.setFixedSize(300, 200)
        self.setCentralWidget(QLabel(f"Texto recebido: {texto_recebido}"))


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Janela Principal")
        self.setFixedSize(400, 300)

        self.janela_texto = None

        self.campo = QLineEdit()
        self.campo.setPlaceholderText("Digite um texto para enviar...")

        botao = QPushButton("Enviar para outra janela")
        botao.clicked.connect(self.abrir_com_texto)

        layout = QVBoxLayout()
        layout.addWidget(self.campo)
        layout.addWidget(botao)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def abrir_com_texto(self):
        # O texto digitado é passado direto pelo construtor da nova janela
        self.janela_texto = JanelaComTexto(self.campo.text())
        self.janela_texto.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

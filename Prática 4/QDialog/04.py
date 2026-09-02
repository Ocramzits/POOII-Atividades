import sys
from PySide6.QtWidgets import (
    QApplication, QDialog, QVBoxLayout, QLineEdit, QPushButton
)


class MeuDialogo(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Diálogo com entrada de texto")
        self.setFixedSize(300, 150)

        self.campo = QLineEdit()
        self.campo.setPlaceholderText("Digite algo...")

        botao_confirmar = QPushButton("Confirmar")
        botao_confirmar.clicked.connect(self.confirmar)

        layout = QVBoxLayout()
        layout.addWidget(self.campo)
        layout.addWidget(botao_confirmar)
        self.setLayout(layout)

    def confirmar(self):
        print(f"Texto confirmado: {self.campo.text()}")
        self.accept()  # fecha o diálogo com resultado "aceito"


if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialogo = MeuDialogo()
    dialogo.show()
    sys.exit(app.exec())

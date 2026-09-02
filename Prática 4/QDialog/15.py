import sys
from PySide6.QtWidgets import QApplication, QDialog, QVBoxLayout, QTextEdit


class MeuDialogo(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Diálogo com QTextEdit de uma linha")
        self.setFixedSize(300, 150)

        texto = QTextEdit()
        texto.setPlaceholderText("Digite algo...")
        # QTextEdit é multilinha por natureza; para simular uma única linha,
        # limitamos a altura ao espaço equivalente a uma linha de texto.
        texto.setFixedHeight(30)

        layout = QVBoxLayout()
        layout.addWidget(texto)
        self.setLayout(layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialogo = MeuDialogo()
    dialogo.show()
    sys.exit(app.exec())

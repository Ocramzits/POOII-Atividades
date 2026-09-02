import sys
from PySide6.QtWidgets import QApplication, QDialog, QVBoxLayout, QPushButton


class MeuDialogo(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Diálogo com botão OK")
        self.setFixedSize(300, 200)

        botao_ok = QPushButton("OK")
        botao_ok.clicked.connect(self.close)  # close() fecha a janela do diálogo

        layout = QVBoxLayout()
        layout.addWidget(botao_ok)
        self.setLayout(layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialogo = MeuDialogo()
    dialogo.show()
    sys.exit(app.exec())

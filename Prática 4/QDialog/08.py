import sys
from PySide6.QtWidgets import QApplication, QDialog, QVBoxLayout, QLabel


class MeuDialogo(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Diálogo com tamanho fixo")
        self.setFixedSize(300, 200)  # usuário não consegue redimensionar

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Este diálogo tem tamanho fixo: 300x200"))
        self.setLayout(layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialogo = MeuDialogo()
    dialogo.show()
    sys.exit(app.exec())

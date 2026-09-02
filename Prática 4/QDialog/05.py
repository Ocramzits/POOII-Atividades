import sys
from PySide6.QtWidgets import QApplication, QDialog, QVBoxLayout, QLabel, QLineEdit


class MeuDialogo(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Diálogo com QLabel")
        self.setFixedSize(300, 150)

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Digite seu nome"))
        layout.addWidget(QLineEdit())
        self.setLayout(layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialogo = MeuDialogo()
    dialogo.show()
    sys.exit(app.exec())

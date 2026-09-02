import sys
from PySide6.QtWidgets import QApplication, QDialog, QVBoxLayout, QLabel


class MeuDialogo(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Configurações")
        self.setFixedSize(300, 150)

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Tela de configurações"))
        self.setLayout(layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialogo = MeuDialogo()
    dialogo.show()
    sys.exit(app.exec())

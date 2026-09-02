import sys
from PySide6.QtWidgets import QApplication, QDialog


class MeuDialogo(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Meu Diálogo")
        self.setFixedSize(300, 200)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialogo = MeuDialogo()
    dialogo.show()
    sys.exit(app.exec())

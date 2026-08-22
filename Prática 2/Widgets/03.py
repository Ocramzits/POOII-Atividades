import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLineEdit


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QLineEdit")
        self.setFixedSize(400, 300)

        self.campo = QLineEdit(self)
        self.campo.setPlaceholderText("Digite algo aqui...")
        self.setCentralWidget(self.campo)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
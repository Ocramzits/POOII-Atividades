import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QTextEdit


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QTextEdit")
        self.setFixedSize(400, 300)

        self.texto = QTextEdit(self)
        self.texto.setPlaceholderText("Digite um texto com várias linhas...")
        self.setCentralWidget(self.texto)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
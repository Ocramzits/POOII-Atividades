import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QPushButton")
        self.setFixedSize(400, 300)

        self.botao = QPushButton("Botão", self)
        self.botao.setText("Clique-me")
        self.setCentralWidget(self.botao)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
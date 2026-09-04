import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel


class Janela2(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Janela 2")
        self.setFixedSize(300, 200)
        self.setCentralWidget(QLabel("Sou a Janela 2"))


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Janela Principal")
        self.setFixedSize(400, 300)

        self.janela_2 = None

        botao = QPushButton("Abrir Janela 2", self)
        botao.clicked.connect(self.abrir_janela_2)
        self.setCentralWidget(botao)

    def abrir_janela_2(self):
        self.janela_2 = Janela2()
        self.janela_2.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

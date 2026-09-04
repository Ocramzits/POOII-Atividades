import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel


class JanelaA(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Janela A")
        self.setFixedSize(300, 200)
        self.setCentralWidget(QLabel("Sou a Janela A"))


class JanelaB(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Janela B")
        self.setFixedSize(300, 200)
        self.setCentralWidget(QLabel("Sou a Janela B"))


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Ambas são independentes: nenhuma é "pai" da outra, e fechar uma não
    # fecha a outra.
    janela_a = JanelaA()
    janela_b = JanelaB()

    janela_a.show()
    janela_b.show()

    sys.exit(app.exec())

import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel


class JanelaFilha(QMainWindow):
    def __init__(self, pai):
        super().__init__()
        self.setWindowTitle("Janela Filha")
        self.setFixedSize(300, 200)
        self.setCentralWidget(QLabel("Tenho um pai definido via setParent"))

        # setParent vincula esta janela à janela principal: ela passa a ficar
        # sempre acima do pai e é fechada automaticamente se o pai fechar.
        self.setParent(pai)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Janela Principal")
        self.setFixedSize(400, 300)

        self.janela_filha = None

        botao = QPushButton("Abrir janela filha", self)
        botao.clicked.connect(self.abrir_filha)
        self.setCentralWidget(botao)

    def abrir_filha(self):
        self.janela_filha = JanelaFilha(self)
        self.janela_filha.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

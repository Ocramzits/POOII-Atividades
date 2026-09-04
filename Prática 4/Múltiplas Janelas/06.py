import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton


class JanelaFilha(QMainWindow):
    def __init__(self, pai):
        # A flag Qt.Window força esta janela a se comportar como uma janela
        # de nível superior de verdade (com botões de minimizar/fechar
        # próprios), mesmo tendo um "pai" definido.
        super().__init__(pai, Qt.Window)
        self.setWindowTitle("Janela Filha (Qt.Window)")
        self.setFixedSize(300, 200)

        botao_fechar = QPushButton("Fechar esta janela", self)
        botao_fechar.clicked.connect(self.close)
        self.setCentralWidget(botao_fechar)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Janela Principal")
        self.setFixedSize(400, 300)

        self.filha = None

        botao = QPushButton("Abrir janela filha", self)
        botao.clicked.connect(self.abrir_filha)
        self.setCentralWidget(botao)

    def abrir_filha(self):
        self.filha = JanelaFilha(self)
        self.filha.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

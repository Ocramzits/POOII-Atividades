import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel


class JanelaSecundaria(QMainWindow):
    def __init__(self, principal):
        super().__init__()
        self.principal = principal
        self.setWindowTitle("Janela Secundária")
        self.setFixedSize(300, 200)

        botao = QPushButton("Voltar para a principal", self)
        botao.clicked.connect(self.voltar)
        self.setCentralWidget(botao)

    def voltar(self):
        self.hide()             # esconde a secundária
        self.principal.show()   # reexibe a principal


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Janela Principal")
        self.setFixedSize(400, 300)

        self.secundaria = JanelaSecundaria(self)

        botao = QPushButton("Ir para a secundária", self)
        botao.clicked.connect(self.ir_para_secundaria)
        self.setCentralWidget(botao)

    def ir_para_secundaria(self):
        self.hide()               # esconde a principal
        self.secundaria.show()    # mostra a secundária


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

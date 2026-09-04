import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel


class JanelaSecundaria(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Janela Secundária")
        self.setFixedSize(300, 200)
        self.setCentralWidget(QLabel("Estou em foco agora"))


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Janela Principal")
        self.setFixedSize(400, 300)

        self.secundaria = JanelaSecundaria()
        self.secundaria.show()

        botao = QPushButton("Trazer secundária para frente", self)
        botao.clicked.connect(self.focar_secundaria)
        self.setCentralWidget(botao)

    def focar_secundaria(self):
        # activateWindow() traz a janela para frente e lhe dá o foco do
        # teclado, mesmo que ela já esteja visível atrás de outras janelas.
        self.secundaria.raise_()
        self.secundaria.activateWindow()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton


class JanelaSecundaria(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Janela Secundária")
        self.setFixedSize(300, 200)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Janela Principal")
        self.setFixedSize(400, 300)

        # Guarda referência para o Python não destruir o objeto após o clique
        self.janela_secundaria = None

        botao = QPushButton("Abrir segunda janela", self)
        botao.clicked.connect(self.abrir_segunda_janela)
        self.setCentralWidget(botao)

    def abrir_segunda_janela(self):
        self.janela_secundaria = JanelaSecundaria()
        self.janela_secundaria.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

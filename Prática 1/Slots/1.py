import sys
from PySide6.QtWidgets import QApplication, QPushButton

class Botao(QPushButton):
    def __init__(self):
        super().__init__("Clique aqui")
        self.clicked.connect(self.botao_clicado)

    def botao_clicado(self):
        print("Botão clicado!")

if __name__ == "__main__":
    app = QApplication(sys.argv)

    botao = Botao()
    botao.show()

    sys.exit(app.exec())
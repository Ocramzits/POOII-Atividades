import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel


class JanelaSecundaria(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Janela Secundária (400x300)")
        self.setFixedSize(400, 300)  # não pode ser redimensionada
        self.setCentralWidget(QLabel("Tamanho fixo: 400x300"))


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Janela Principal")
        self.setFixedSize(300, 200)

        self.secundaria = None

        botao = QPushButton("Abrir secundária", self)
        botao.clicked.connect(self.abrir_secundaria)
        self.setCentralWidget(botao)

    def abrir_secundaria(self):
        self.secundaria = JanelaSecundaria()
        self.secundaria.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel


class JanelaFerramenta(QMainWindow):
    def __init__(self):
        # Qt.Tool cria uma janela "de utilidade": barra de título reduzida
        # (geralmente sem botão de minimizar/maximizar) e não aparece na
        # barra de tarefas do sistema operacional.
        super().__init__(flags=Qt.Tool)
        self.setWindowTitle("Ferramenta")
        self.setFixedSize(250, 150)
        self.setCentralWidget(QLabel("Janela do tipo Qt.Tool"))


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Janela Principal")
        self.setFixedSize(400, 300)

        self.ferramenta = None

        botao = QPushButton("Abrir janela de ferramenta", self)
        botao.clicked.connect(self.abrir_ferramenta)
        self.setCentralWidget(botao)

    def abrir_ferramenta(self):
        self.ferramenta = JanelaFerramenta()
        self.ferramenta.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

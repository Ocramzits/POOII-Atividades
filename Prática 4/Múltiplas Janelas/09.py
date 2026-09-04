import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QLabel, QWidget, QVBoxLayout
)


class JanelaExtra(QMainWindow):
    def __init__(self, titulo: str):
        super().__init__()
        self.setWindowTitle(titulo)
        self.setFixedSize(250, 150)
        self.setCentralWidget(QLabel(f"Sou a {titulo}"))


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Janela Principal")
        self.setFixedSize(400, 300)

        self.janela_1 = JanelaExtra("Janela 1")
        self.janela_2 = JanelaExtra("Janela 2")
        self.janela_3 = JanelaExtra("Janela 3")

        botao_abrir = QPushButton("Abrir as 3 janelas", self)
        botao_abrir.clicked.connect(self.abrir_todas)

        botao_fechar = QPushButton("Fechar todas", self)
        botao_fechar.clicked.connect(self.fechar_todas)

        layout = QVBoxLayout()
        layout.addWidget(botao_abrir)
        layout.addWidget(botao_fechar)
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def abrir_todas(self):
        self.janela_1.show()
        self.janela_2.show()
        self.janela_3.show()

    def fechar_todas(self):
        self.janela_1.close()
        self.janela_2.close()
        self.janela_3.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

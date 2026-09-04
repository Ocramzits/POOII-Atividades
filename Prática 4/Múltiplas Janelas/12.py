import sys
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel


class JanelaSecundaria(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Janela Secundária com Toolbar")
        self.setFixedSize(300, 200)
        self.setCentralWidget(QLabel("Use a toolbar para fechar"))

        barra = self.addToolBar("Principal")
        acao_fechar = QAction("Fechar", self)
        acao_fechar.triggered.connect(self.close)
        barra.addAction(acao_fechar)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Janela Principal")
        self.setFixedSize(400, 300)

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

import sys
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel


class JanelaNova(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Janela Nova")
        self.setFixedSize(300, 200)
        self.setCentralWidget(QLabel("Aberta pelo menu da janela principal"))


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Janela Principal")
        self.setFixedSize(400, 300)

        self.janela_nova = None

        menu_arquivo = self.menuBar().addMenu("Arquivo")
        acao_abrir_janela = QAction("Abrir Janela Nova", self)
        acao_abrir_janela.triggered.connect(self.abrir_janela_nova)
        menu_arquivo.addAction(acao_abrir_janela)

    def abrir_janela_nova(self):
        self.janela_nova = JanelaNova()
        self.janela_nova.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

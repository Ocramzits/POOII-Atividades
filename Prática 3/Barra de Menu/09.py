import sys
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QApplication, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Menu Ver com Modo Escuro")
        self.setFixedSize(400, 300)

        menu_ver = self.menuBar().addMenu("Ver")

        acao_modo_escuro = QAction("Modo Escuro", self)
        acao_modo_escuro.setCheckable(True)
        acao_modo_escuro.toggled.connect(self.alternar_modo_escuro)

        menu_ver.addAction(acao_modo_escuro)

    def alternar_modo_escuro(self, ativado: bool):
        if ativado:
            self.setStyleSheet("background-color: #2b2b2b; color: white;")
        else:
            self.setStyleSheet("")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

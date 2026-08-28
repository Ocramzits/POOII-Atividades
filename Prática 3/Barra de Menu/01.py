import sys
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QApplication, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QMenuBar com menu Arquivo")
        self.setFixedSize(400, 300)

        barra_menu = self.menuBar()
        menu_arquivo = barra_menu.addMenu("Arquivo")

        acao_novo = QAction("Novo", self)
        menu_arquivo.addAction(acao_novo)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

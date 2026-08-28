import sys
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QApplication, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QAction Imprimir")
        self.setFixedSize(400, 300)

        menu_arquivo = self.menuBar().addMenu("Arquivo")
        menu_arquivo.addAction(QAction("Novo", self))
        menu_arquivo.addAction(QAction("Abrir", self))

        acao_imprimir = QAction("Imprimir", self)
        acao_imprimir.triggered.connect(self.imprimir)
        menu_arquivo.addAction(acao_imprimir)

    def imprimir(self):
        print("Imprimindo...")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

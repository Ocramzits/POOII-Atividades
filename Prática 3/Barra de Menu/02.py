import sys
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QApplication, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QAction Abrir via menuBar()")
        self.setFixedSize(400, 300)

        # self.menuBar() retorna o QMenuBar da janela (cria um automaticamente
        # se ainda não existir).
        menu_arquivo = self.menuBar().addMenu("Arquivo")

        acao_abrir = QAction("Abrir", self)
        menu_arquivo.addAction(acao_abrir)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

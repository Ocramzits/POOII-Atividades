import sys
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QApplication, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QAction Sair")
        self.setFixedSize(400, 300)

        menu_arquivo = self.menuBar().addMenu("Arquivo")

        acao_sair = QAction("Sair", self)
        acao_sair.triggered.connect(self.close)  # close() é slot nativo de QWidget

        menu_arquivo.addAction(acao_sair)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

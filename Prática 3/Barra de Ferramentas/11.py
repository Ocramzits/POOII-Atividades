import sys
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QApplication, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QAction com tooltip")
        self.setFixedSize(400, 300)

        barra = self.addToolBar("Principal")

        acao_abrir = QAction("Abrir", self)
        acao_abrir.setToolTip("Abrir arquivo")  # aparece ao passar o mouse por cima
        barra.addAction(acao_abrir)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

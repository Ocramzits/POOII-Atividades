import sys
from PySide6.QtCore import QSize
from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import QApplication, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QToolBar com iconSize")
        self.setFixedSize(400, 300)

        barra = self.addToolBar("Principal")
        barra.setIconSize(QSize(32, 32))

        acao = QAction(QIcon.fromTheme("document-open"), "Abrir", self)
        barra.addAction(acao)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

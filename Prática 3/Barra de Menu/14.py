import sys
from PySide6.QtGui import QAction, QKeySequence
from PySide6.QtWidgets import QApplication, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QAction Desfazer")
        self.setFixedSize(400, 300)

        menu_editar = self.menuBar().addMenu("Editar")

        acao_desfazer = QAction("Desfazer", self)
        acao_desfazer.setShortcut(QKeySequence("Ctrl+Z"))
        acao_desfazer.triggered.connect(self.desfazer)

        menu_editar.addAction(acao_desfazer)

    def desfazer(self):
        print("Última ação desfeita (Ctrl+Z)")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

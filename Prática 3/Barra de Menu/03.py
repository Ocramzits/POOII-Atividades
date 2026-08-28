import sys
from PySide6.QtGui import QAction, QKeySequence
from PySide6.QtWidgets import QApplication, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Menu Editar com shortcut")
        self.setFixedSize(400, 300)

        menu_editar = self.menuBar().addMenu("Editar")

        acao_copiar = QAction("Copiar", self)
        acao_copiar.setShortcut(QKeySequence("Ctrl+C"))
        acao_copiar.triggered.connect(self.copiar)

        menu_editar.addAction(acao_copiar)

    def copiar(self):
        print("Copiado (Ctrl+C)")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

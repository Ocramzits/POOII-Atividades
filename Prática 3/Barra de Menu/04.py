import sys
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QApplication, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Menu Ajuda com separador")
        self.setFixedSize(400, 300)

        menu_ajuda = self.menuBar().addMenu("Ajuda")

        menu_ajuda.addAction(QAction("Documentação", self))
        menu_ajuda.addAction(QAction("Verificar atualizações", self))
        menu_ajuda.addSeparator()  # linha divisória antes do item "Sobre"
        menu_ajuda.addAction(QAction("Sobre", self))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

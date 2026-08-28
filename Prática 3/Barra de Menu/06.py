import sys
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QApplication, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Submenu Exportar")
        self.setFixedSize(400, 300)

        menu_arquivo = self.menuBar().addMenu("Arquivo")
        menu_arquivo.addAction(QAction("Novo", self))

        # addMenu em um QMenu (não na menuBar) cria um submenu aninhado
        submenu_exportar = menu_arquivo.addMenu("Exportar")
        submenu_exportar.addAction(QAction("Exportar como PDF", self))
        submenu_exportar.addAction(QAction("Exportar como CSV", self))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

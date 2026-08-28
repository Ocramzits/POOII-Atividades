import sys
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QApplication, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Menu Janela com Minimizar")
        self.setFixedSize(400, 300)

        menu_janela = self.menuBar().addMenu("Janela")

        acao_minimizar = QAction("Minimizar", self)
        acao_minimizar.triggered.connect(self.showMinimized)  # slot nativo de QWidget

        menu_janela.addAction(acao_minimizar)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

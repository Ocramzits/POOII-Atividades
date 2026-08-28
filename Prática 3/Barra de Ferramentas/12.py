import sys
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QApplication, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QToolBar fixa (não movível)")
        self.setFixedSize(400, 300)

        barra = self.addToolBar("Principal")
        barra.setMovable(False)  # impede o usuário de arrastar a barra pra outro lugar

        barra.addAction(QAction("Novo", self))
        barra.addAction(QAction("Abrir", self))
        barra.addAction(QAction("Salvar", self))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

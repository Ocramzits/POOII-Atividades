import sys
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QApplication, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QToolBar flutuante")
        self.setFixedSize(400, 300)

        barra = self.addToolBar("Principal")
        barra.setFloatable(True)  # permite destacar a barra da janela, arrastando-a
        barra.setMovable(True)    # precisa estar movable para poder ser arrastada

        barra.addAction(QAction("Arraste-me para fora da janela", self))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

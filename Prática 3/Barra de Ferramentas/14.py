import sys
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QApplication, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QAction que muda texto")
        self.setFixedSize(400, 300)

        barra = self.addToolBar("Principal")

        self.acao = QAction("Clique em mim", self)
        self.acao.triggered.connect(self.mudar_texto)
        barra.addAction(self.acao)

    def mudar_texto(self):
        self.acao.setText("Já cliquei!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

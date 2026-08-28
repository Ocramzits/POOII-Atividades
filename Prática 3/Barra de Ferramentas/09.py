import sys
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QApplication, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QAction Copiar")
        self.setFixedSize(400, 300)

        barra = self.addToolBar("Principal")

        acao_copiar = QAction("Copiar", self)
        acao_copiar.triggered.connect(self.copiar)
        barra.addAction(acao_copiar)

    def copiar(self):
        print("Conteúdo copiado")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

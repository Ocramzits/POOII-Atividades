# 3. Configure uma QToolBar com QAction "Salvar" e conecte ao slot que
#    imprime "Salvo".
import sys
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QApplication, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QAction Salvar")
        self.setFixedSize(400, 300)

        barra = self.addToolBar("Principal")

        acao_salvar = QAction("Salvar", self)
        acao_salvar.triggered.connect(self.salvar)
        barra.addAction(acao_salvar)

    def salvar(self):
        print("Salvo")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

import sys
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QApplication, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QAction checkable")
        self.setFixedSize(400, 300)

        barra = self.addToolBar("Principal")

        acao_negrito = QAction("Negrito", self)
        acao_negrito.setCheckable(True)  # permite alternar entre marcado/desmarcado
        acao_negrito.toggled.connect(self.alternar_negrito)

        barra.addAction(acao_negrito)

    def alternar_negrito(self, marcado: bool):
        estado = "ativado" if marcado else "desativado"
        print(f"Negrito {estado}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

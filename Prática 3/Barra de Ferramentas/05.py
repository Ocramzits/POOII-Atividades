import sys
from PySide6.QtGui import QAction, QKeySequence
from PySide6.QtWidgets import QApplication, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QAction com shortcut")
        self.setFixedSize(400, 300)

        barra = self.addToolBar("Principal")

        acao_novo = QAction("Novo", self)
        acao_novo.setShortcut(QKeySequence("Ctrl+N"))
        acao_novo.triggered.connect(self.novo_arquivo)

        barra.addAction(acao_novo)

    def novo_arquivo(self):
        print("Novo arquivo criado (Ctrl+N)")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

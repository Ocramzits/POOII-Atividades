import sys
from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import QApplication, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QAction com ícone de tema")
        self.setFixedSize(400, 300)

        barra = self.addToolBar("Principal")

        # QIcon.fromTheme busca ícones do tema de ícones do sistema operacional
        # (funciona bem no Linux; em outros sistemas pode não encontrar o ícone
        # e retornar um ícone vazio).
        icone = QIcon.fromTheme("document-open")
        acao_abrir = QAction(icone, "Abrir", self)
        barra.addAction(acao_abrir)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

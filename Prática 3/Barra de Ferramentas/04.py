import sys
from PySide6.QtCore import Qt
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QApplication, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QToolBar com dois QAction")
        self.setFixedSize(400, 300)

        # QToolBar já nasce horizontal por padrão, mas deixamos explícito.
        barra = self.addToolBar("Principal")
        barra.setOrientation(Qt.Horizontal)

        acao_novo = QAction("Novo", self)
        acao_fechar = QAction("Fechar", self)
        acao_fechar.triggered.connect(self.close)

        barra.addAction(acao_novo)
        barra.addAction(acao_fechar)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

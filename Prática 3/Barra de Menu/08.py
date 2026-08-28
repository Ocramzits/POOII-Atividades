import sys
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QApplication, QMainWindow, QStyle


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QAction com ícone no menu")
        self.setFixedSize(400, 300)

        menu_editar = self.menuBar().addMenu("Editar")

        # Ícone padrão do próprio Qt, sem depender de tema do sistema.
        icone = self.style().standardIcon(QStyle.SP_DialogSaveButton)
        acao_colar = QAction(icone, "Colar", self)
        menu_editar.addAction(acao_colar)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

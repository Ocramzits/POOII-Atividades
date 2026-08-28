import sys
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QApplication, QMainWindow, QStyle


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QAction Imprimir com ícone padrão")
        self.setFixedSize(400, 300)

        barra = self.addToolBar("Principal")

        # Ícone padrão vem do próprio conjunto de estilos do Qt (QStyle),
        # sem depender de tema do sistema nem de arquivo externo.
        icone = self.style().standardIcon(QStyle.SP_FileDialogDetailedView)
        acao_imprimir = QAction(icone, "Imprimir", self)
        barra.addAction(acao_imprimir)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

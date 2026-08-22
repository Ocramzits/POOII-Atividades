import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QToolButton, QStyle


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QToolButton")
        self.setFixedSize(400, 300)

        self.botao = QToolButton(self)
        # Usa um ícone padrão do próprio sistema de estilos do Qt,
        # assim não depende de nenhum arquivo de imagem externo.
        icone = self.style().standardIcon(QStyle.SP_DialogOpenButton)
        self.botao.setIcon(icone)
        self.botao.setText("Abrir")
        self.botao.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.setCentralWidget(self.botao)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
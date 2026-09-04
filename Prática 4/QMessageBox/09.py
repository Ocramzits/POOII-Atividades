import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QMessageBox.about")
        self.setFixedSize(400, 300)

        botao = QPushButton("Sobre o aplicativo", self)
        botao.clicked.connect(self.mostrar_sobre)
        self.setCentralWidget(botao)

    def mostrar_sobre(self):
        # about() é uma variação de information() sem ícone de "?" e sem som,
        # pensada especificamente para telas de "Sobre"
        QMessageBox.about(
            self,
            "Sobre",
            "Meu Aplicativo v1.0\n"
            "Desenvolvido com PySide6",
        )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QMessageBox.question")
        self.setFixedSize(400, 300)

        botao = QPushButton("Sair", self)
        botao.clicked.connect(self.perguntar_saida)
        self.setCentralWidget(botao)

    def perguntar_saida(self):
        resposta = QMessageBox.question(
            self, "Confirmar", "Deseja sair?", QMessageBox.Yes | QMessageBox.No
        )
        if resposta == QMessageBox.Yes:
            self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

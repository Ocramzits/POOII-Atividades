import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QMessageBox.critical")
        self.setFixedSize(400, 300)

        botao = QPushButton("Simular erro", self)
        botao.clicked.connect(self.mostrar_erro)
        self.setCentralWidget(botao)

    def mostrar_erro(self):
        # critical() já exibe automaticamente o ícone de erro (X vermelho)
        QMessageBox.critical(self, "Erro", "Ocorreu um erro crítico na aplicação.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

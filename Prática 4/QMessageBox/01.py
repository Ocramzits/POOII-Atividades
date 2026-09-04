import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QMessageBox.information")
        self.setFixedSize(400, 300)

        botao = QPushButton("Mostrar mensagem", self)
        botao.clicked.connect(self.mostrar_sucesso)
        self.setCentralWidget(botao)

    def mostrar_sucesso(self):
        QMessageBox.information(self, "Sucesso", "Operação concluída")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QMessageBox com título vazio")
        self.setFixedSize(400, 300)

        botao = QPushButton("Mostrar mensagem", self)
        botao.clicked.connect(self.mostrar_mensagem)
        self.setCentralWidget(botao)

    def mostrar_mensagem(self):
        caixa = QMessageBox(self)
        caixa.setWindowTitle("")  # título vazio na barra da janela
        caixa.setText("Apenas uma mensagem simples, sem título.")
        caixa.exec()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

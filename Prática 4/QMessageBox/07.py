import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QMessageBox com Ok/Cancel")
        self.setFixedSize(400, 300)

        botao = QPushButton("Mostrar alerta", self)
        botao.clicked.connect(self.mostrar_alerta)
        self.setCentralWidget(botao)

    def mostrar_alerta(self):
        caixa = QMessageBox(self)
        caixa.setWindowTitle("Confirmação")
        caixa.setText("Deseja continuar com a operação?")
        caixa.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

        resultado = caixa.exec()
        if resultado == QMessageBox.Ok:
            print("Usuário confirmou")
        else:
            print("Usuário cancelou")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

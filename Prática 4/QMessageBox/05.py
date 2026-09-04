import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QMessageBox com exec()")
        self.setFixedSize(400, 300)

        botao = QPushButton("Abrir caixa customizada", self)
        botao.clicked.connect(self.abrir_caixa)
        self.setCentralWidget(botao)

    def abrir_caixa(self):
        caixa = QMessageBox(self)
        caixa.setWindowTitle("Escolha uma opção")
        caixa.setText("O que você deseja fazer?")
        caixa.setStandardButtons(
            QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel
        )

        # exec() retorna o valor do botão que o usuário efetivamente clicou
        resultado = caixa.exec()

        if resultado == QMessageBox.Save:
            print("Usuário clicou em Salvar")
        elif resultado == QMessageBox.Discard:
            print("Usuário clicou em Descartar")
        else:
            print("Usuário cancelou")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

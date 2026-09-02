import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QDialog, QVBoxLayout, QCheckBox, QPushButton
)


class MeuDialogo(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Diálogo não modal")
        self.setFixedSize(300, 150)

        layout = QVBoxLayout()
        layout.addWidget(QCheckBox("Aceito os termos"))
        self.setLayout(layout)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Janela principal")
        self.setFixedSize(400, 300)

        # Guarda referência do diálogo na própria janela para evitar que o
        # garbage collector do Python destrua o objeto assim que a função
        # abrir_dialogo() termina de executar.
        self.dialogo = None

        botao = QPushButton("Abrir diálogo não modal", self)
        botao.clicked.connect(self.abrir_dialogo)
        self.setCentralWidget(botao)

    def abrir_dialogo(self):
        self.dialogo = MeuDialogo()
        # show() (em vez de exec()) permite continuar interagindo com a
        # janela principal enquanto o diálogo está aberto.
        self.dialogo.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

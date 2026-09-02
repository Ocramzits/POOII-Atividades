import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QDialog, QVBoxLayout, QLabel, QPushButton
)


class MeuDialogo(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Diálogo modal")
        self.setFixedSize(300, 200)

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Este diálogo é modal — bloqueia a janela principal."))
        self.setLayout(layout)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Janela principal")
        self.setFixedSize(400, 300)

        botao = QPushButton("Abrir diálogo modal", self)
        botao.clicked.connect(self.abrir_dialogo)
        self.setCentralWidget(botao)

    def abrir_dialogo(self):
        dialogo = MeuDialogo()
        # exec() abre o diálogo em modo modal: bloqueia a interação com a
        # janela principal até que o diálogo seja fechado.
        dialogo.exec()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

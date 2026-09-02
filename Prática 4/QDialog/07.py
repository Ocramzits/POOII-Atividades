import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QDialog, QVBoxLayout, QLabel, QPushButton
)


class MeuDialogo(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Diálogo aberto pela janela principal")
        self.setFixedSize(300, 150)

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Olá! Fui aberto por um clique."))
        self.setLayout(layout)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Janela principal")
        self.setFixedSize(400, 300)

        botao = QPushButton("Abrir diálogo", self)
        botao.clicked.connect(self.abrir_dialogo)
        self.setCentralWidget(botao)

    def abrir_dialogo(self):
        dialogo = MeuDialogo()
        dialogo.exec()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

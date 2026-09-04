import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel


class JanelaModal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Janela Modal (bloqueia tudo)")
        self.setFixedSize(300, 200)
        self.setCentralWidget(QLabel("Enquanto estiver aberta, bloqueia toda a aplicação"))

        # ApplicationModal bloqueia a interação com QUALQUER outra janela da
        # aplicação (diferente de WindowModal, que bloqueia só o pai direto).
        self.setWindowModality(Qt.ApplicationModal)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Janela Principal")
        self.setFixedSize(400, 300)

        self.modal = None

        botao = QPushButton("Abrir janela modal", self)
        botao.clicked.connect(self.abrir_modal)
        self.setCentralWidget(botao)

    def abrir_modal(self):
        self.modal = JanelaModal()
        self.modal.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

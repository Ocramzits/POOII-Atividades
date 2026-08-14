import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton
)
from PySide6.QtCore import Signal

class MainWindow(QMainWindow):
    lista_pronta = Signal(list)

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Slot com lista")

        self.lista_pronta.connect(self.mostrar_comprimento)

        self.botao = QPushButton("Emitir lista")
        self.botao.clicked.connect(self.disparar_sinal)

        layout = QVBoxLayout()
        layout.addWidget(self.botao)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def disparar_sinal(self):
        minha_lista = [1, 2, 3, 4, 5]
        self.lista_pronta.emit(minha_lista)

    def mostrar_comprimento(self, lista: list):
        print(f"Comprimento da lista: {len(lista)}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
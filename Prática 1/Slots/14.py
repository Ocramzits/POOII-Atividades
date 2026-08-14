import sys
from enum import Enum
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel
)
from PySide6.QtCore import Signal

class Status(Enum):
    ATIVO = 1
    INATIVO = 2
    PENDENTE = 3

class MainWindow(QMainWindow):
    status_alterado = Signal(Status)

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Slot com Enum")

        self.status_alterado.connect(self.mostrar_status)

        self.label = QLabel("Status: (nenhum ainda)")
        self.botao = QPushButton("Definir como ATIVO")

        self.botao.clicked.connect(self.disparar_sinal)

        layout = QVBoxLayout()
        layout.addWidget(self.botao)
        layout.addWidget(self.label)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def disparar_sinal(self):
        self.status_alterado.emit(Status.ATIVO)

    def mostrar_status(self, status: Status):
        print(f"Status recebido: {status.name}")
        self.label.setText(f"Status: {status.name}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
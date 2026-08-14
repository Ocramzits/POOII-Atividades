import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel
)
from PySide6.QtCore import Signal

class MainWindow(QMainWindow):
    dados_prontos = Signal(dict)

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Slot com dicionário")

        self.dados_prontos.connect(self.mostrar_nome)

        self.label = QLabel("Nome: (nenhum ainda)")
        self.botao = QPushButton("Emitir dados")
        self.botao.clicked.connect(self.disparar_sinal)

        layout = QVBoxLayout()
        layout.addWidget(self.botao)
        layout.addWidget(self.label)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def disparar_sinal(self):
        meus_dados = {"nome": "Marco", "idade": 21, "curso": "Sistemas de Informação"}
        self.dados_prontos.emit(meus_dados)

    def mostrar_nome(self, dados: dict):
        nome = dados.get("nome", "não encontrado")
        self.label.setText(f"Nome: {nome}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
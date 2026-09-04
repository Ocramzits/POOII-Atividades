import sys
from PySide6.QtCore import Signal
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton,
    QDialog, QLineEdit, QMessageBox, QTableWidget, QTableWidgetItem
)


class MeuDialogo(QDialog):
    # Sinal que carrega o texto digitado para ser inserido na tabela
    item_adicionado = Signal(str)

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Adicionar item")
        self.setFixedSize(300, 150)

        self.campo = QLineEdit()
        self.campo.setPlaceholderText("Nome do item...")

        botao_aceitar = QPushButton("Aceitar")
        botao_aceitar.clicked.connect(self.aceitar_item)

        layout = QVBoxLayout()
        layout.addWidget(self.campo)
        layout.addWidget(botao_aceitar)
        self.setLayout(layout)

    def aceitar_item(self):
        texto = self.campo.text().strip()
        if texto:
            QMessageBox.information(self, "Sucesso", f"Item '{texto}' adicionado!")
            self.item_adicionado.emit(texto)
            self.accept()
        else:
            QMessageBox.warning(self, "Aviso", "Digite um nome antes de aceitar.")


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Exercício 5 - QDialog + QTableWidget")
        self.setFixedSize(400, 300)

        self.tabela = QTableWidget(0, 1)
        self.tabela.setHorizontalHeaderLabels(["Item"])

        botao_abrir_dialogo = QPushButton("Adicionar item via diálogo")
        botao_abrir_dialogo.clicked.connect(self.abrir_dialogo)

        layout = QVBoxLayout()
        layout.addWidget(self.tabela)
        layout.addWidget(botao_abrir_dialogo)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def abrir_dialogo(self):
        dialogo = MeuDialogo()
        dialogo.item_adicionado.connect(self.adicionar_na_tabela)
        dialogo.exec()

    def adicionar_na_tabela(self, texto: str):
        linha = self.tabela.rowCount()
        self.tabela.insertRow(linha)
        self.tabela.setItem(linha, 0, QTableWidgetItem(texto))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

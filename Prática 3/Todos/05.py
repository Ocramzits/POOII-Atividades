import sys
from PySide6.QtCore import Signal
from PySide6.QtGui import QAction
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QTableWidget,
    QTableWidgetItem
)


class TabelaClicavel(QTableWidget):
    # Sinal customizado, emitido quando o usuário clica dentro da tabela
    clicada = Signal()

    def mousePressEvent(self, event):
        self.clicada.emit()
        super().mousePressEvent(event)  # mantém o comportamento normal de seleção


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Exercício 5 - QTableWidget + mousePress")
        self.setFixedSize(400, 300)

        # --- Layout central (QVBoxLayout) ---
        self.tabela = TabelaClicavel(0, 2)
        self.tabela.setHorizontalHeaderLabels(["Item", "Status"])
        self.tabela.clicada.connect(self.registrar_clique)

        layout = QVBoxLayout()
        layout.addWidget(self.tabela)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # --- QToolBar "Adicionar" ---
        barra = self.addToolBar("Principal")
        acao_adicionar = QAction("Adicionar", self)
        acao_adicionar.triggered.connect(self.adicionar_linha)
        barra.addAction(acao_adicionar)

        # --- Menu "Arquivo" ---
        self.menuBar().addMenu("Arquivo")

    def adicionar_linha(self):
        linha = self.tabela.rowCount()
        self.tabela.insertRow(linha)
        self.tabela.setItem(linha, 0, QTableWidgetItem(f"Item {linha + 1}"))
        self.tabela.setItem(linha, 1, QTableWidgetItem("Pendente"))

    def registrar_clique(self):
        print("Tabela foi clicada")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

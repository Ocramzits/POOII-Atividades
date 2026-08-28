import sys
from PySide6.QtCore import Qt
from PySide6.QtGui import QAction
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Exercício 1 - Layout + Toolbar + Menu")
        self.setFixedSize(400, 300)

        # --- Layout central (QVBoxLayout) ---
        self.label = QLabel("Aguardando ação...")
        self.label.setAlignment(Qt.AlignCenter)
        botao = QPushButton("Clique para atualizar")
        botao.clicked.connect(self.atualizar_label)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(botao)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # --- QToolBar com QAction "Salvar" ---
        barra = self.addToolBar("Principal")
        acao_salvar = QAction("Salvar", self)
        acao_salvar.triggered.connect(self.salvar)
        barra.addAction(acao_salvar)

        # --- QMenuBar: Arquivo > Novo ---
        menu_arquivo = self.menuBar().addMenu("Arquivo")
        acao_novo = QAction("Novo", self)
        acao_novo.triggered.connect(self.novo_arquivo)
        menu_arquivo.addAction(acao_novo)

    def atualizar_label(self):
        self.label.setText("Botão clicado!")

    def salvar(self):
        self.label.setText("Salvo pela toolbar")

    def novo_arquivo(self):
        self.label.setText("Novo arquivo criado")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

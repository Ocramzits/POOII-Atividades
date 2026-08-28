import sys
from PySide6.QtGui import QAction
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QHBoxLayout, QLineEdit, QPushButton
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Exercício 10 - QPushButton + clicked")
        self.setFixedSize(400, 300)

        # --- Layout central (QHBoxLayout) ---
        self.campo = QLineEdit()
        self.campo.setPlaceholderText("Digite algo...")
        botao_limpar = QPushButton("Limpar campo")
        botao_limpar.clicked.connect(self.limpar_campo)

        layout = QHBoxLayout()
        layout.addWidget(self.campo)
        layout.addWidget(botao_limpar)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # --- QToolBar "Limpar" (mesma ação, acessível pela barra também) ---
        barra = self.addToolBar("Principal")
        acao_limpar = QAction("Limpar", self)
        acao_limpar.triggered.connect(self.limpar_campo)
        barra.addAction(acao_limpar)

        # --- Menu "Editar" ---
        self.menuBar().addMenu("Editar")

    def limpar_campo(self):
        self.campo.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

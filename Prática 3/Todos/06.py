import sys
from PySide6.QtGui import QAction
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QHBoxLayout, QTextEdit, QLabel
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Exercício 6 - QTextEdit + textChanged")
        self.setFixedSize(400, 300)

        # --- Layout central (QHBoxLayout) ---
        self.texto = QTextEdit()
        self.texto.setPlaceholderText("Digite algo...")
        self.contador = QLabel("Caracteres: 0")

        self.texto.textChanged.connect(self.atualizar_contador)

        layout = QHBoxLayout()
        layout.addWidget(self.texto)
        layout.addWidget(self.contador)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # --- QToolBar com QAction "Copiar" ---
        barra = self.addToolBar("Principal")
        acao_copiar = QAction("Copiar", self)
        acao_copiar.triggered.connect(self.texto.copy)  # slot nativo de QTextEdit
        barra.addAction(acao_copiar)

        # --- Menu "Editar" ---
        self.menuBar().addMenu("Editar")

    def atualizar_contador(self):
        quantidade = len(self.texto.toPlainText())
        self.contador.setText(f"Caracteres: {quantidade}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

import sys
from PySide6.QtGui import QAction
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QHBoxLayout, QLineEdit, QLabel
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Exercício 2 - keyPressEvent")
        self.setFixedSize(400, 300)

        # --- Layout central (QHBoxLayout) ---
        self.instrucao = QLabel("Digite:")
        self.campo = QLineEdit()
        self.campo.setReadOnly(True)  # só é atualizado via keyPressEvent da janela

        layout = QHBoxLayout()
        layout.addWidget(self.instrucao)
        layout.addWidget(self.campo)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # --- QToolBar com QAction "Abrir" ---
        barra = self.addToolBar("Principal")
        barra.addAction(QAction("Abrir", self))

        # --- Menu "Editar" ---
        self.menuBar().addMenu("Editar")

        self.texto_acumulado = ""

    def keyPressEvent(self, event):
        # Cada tecla pressionada (com a janela em foco) é anexada ao campo
        self.texto_acumulado += event.text()
        self.campo.setText(self.texto_acumulado)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

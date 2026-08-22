# 9. Use QVBoxLayout dentro de um QHBoxLayout principal (layout aninhado simples).
import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QLabel, QPushButton
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Layout aninhado")
        self.setFixedSize(400, 300)

        # Layout interno (vertical): fica dentro de uma "coluna" do layout externo
        layout_interno = QVBoxLayout()
        layout_interno.addWidget(QLabel("Item 1"))
        layout_interno.addWidget(QLabel("Item 2"))
        layout_interno.addWidget(QPushButton("Botão"))

        # Layout externo (horizontal): recebe o layout interno como se fosse um widget
        layout_externo = QHBoxLayout()
        layout_externo.addWidget(QLabel("Coluna esquerda"))
        layout_externo.addLayout(layout_interno)  # aninhamento acontece aqui

        container = QWidget()
        container.setLayout(layout_externo)
        self.setCentralWidget(container)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QVBoxLayout com stretch")
        self.setFixedSize(400, 300)

        layout = QVBoxLayout()

        botao_1 = QPushButton("Sem stretch (tamanho normal)")
        botao_2 = QPushButton("Com stretch=1 (ocupa espaço extra)")
        botao_3 = QPushButton("Sem stretch (tamanho normal)")

        layout.addWidget(botao_1)
        layout.addWidget(botao_2, 1)  # segundo argumento é o stretch factor
        layout.addWidget(botao_3)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
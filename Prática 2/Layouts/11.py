import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QHBoxLayout com alignment")
        self.setFixedSize(400, 300)

        layout = QHBoxLayout()

        botao = QPushButton("Botão à direita")
        layout.addWidget(botao)
        layout.setAlignment(botao, Qt.AlignRight)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
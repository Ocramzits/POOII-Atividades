import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QVBoxLayout")
        self.setFixedSize(400, 300)

        layout = QVBoxLayout()
        layout.addWidget(QPushButton("Botão 1"))
        layout.addWidget(QPushButton("Botão 2"))

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
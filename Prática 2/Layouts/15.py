import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QRadioButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QHBoxLayout com margin")
        self.setFixedSize(400, 300)

        layout = QHBoxLayout()
        layout.setContentsMargins(10, 10, 10, 10)  # margin=10 nos 4 lados

        layout.addWidget(QRadioButton("Opção 1"))
        layout.addWidget(QRadioButton("Opção 2"))
        layout.addWidget(QRadioButton("Opção 3"))

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
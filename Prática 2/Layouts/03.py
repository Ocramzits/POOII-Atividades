import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QLineEdit


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QGridLayout 2x2")
        self.setFixedSize(400, 300)

        layout = QGridLayout()
        layout.addWidget(QLineEdit(), 0, 0)  # linha 0, coluna 0
        layout.addWidget(QLineEdit(), 0, 1)  # linha 0, coluna 1
        layout.addWidget(QLineEdit(), 1, 0)  # linha 1, coluna 0
        layout.addWidget(QLineEdit(), 1, 1)  # linha 1, coluna 1

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QStackedLayout, QLabel, QPushButton
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QStackedLayout")
        self.setFixedSize(400, 300)

        layout = QStackedLayout()
        layout.addWidget(QLabel("Sou um QLabel"))       # índice 0
        layout.addWidget(QPushButton("Sou um QPushButton"))  # índice 1

        layout.setCurrentIndex(0)  # começa mostrando o QLabel

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
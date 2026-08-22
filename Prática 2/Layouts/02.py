import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QLabel


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QHBoxLayout")
        self.setFixedSize(400, 300)

        layout = QHBoxLayout()
        layout.addWidget(QLabel("Label 1"))
        layout.addWidget(QLabel("Label 2"))
        layout.addWidget(QLabel("Label 3"))

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
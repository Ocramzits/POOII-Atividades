import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QSpinBox


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QSpinBox")
        self.setFixedSize(400, 300)

        self.spinbox = QSpinBox(self)
        self.spinbox.setRange(0, 100)
        self.setCentralWidget(self.spinbox)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
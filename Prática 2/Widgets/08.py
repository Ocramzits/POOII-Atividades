import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QProgressBar


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QProgressBar")
        self.setFixedSize(400, 300)

        self.barra = QProgressBar(self)
        self.barra.setRange(0, 100)
        self.barra.setValue(75)
        self.setCentralWidget(self.barra)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
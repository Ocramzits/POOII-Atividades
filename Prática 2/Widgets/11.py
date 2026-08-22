import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QCalendarWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QCalendarWidget")
        self.setFixedSize(400, 300)

        self.calendario = QCalendarWidget(self)
        self.setCentralWidget(self.calendario)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
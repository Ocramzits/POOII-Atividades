import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QLabel")
        self.setFixedSize(400, 300)

        self.label = QLabel("Olá, PySide6!", self)
        self.label.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(self.label)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
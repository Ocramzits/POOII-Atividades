import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("enterEvent")
        self.setFixedSize(400, 300)

        self.label = QLabel("Passe o mouse sobre a janela", self)
        self.label.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(self.label)

    def enterEvent(self, event):
        self.setCursor(Qt.PointingHandCursor)
        super().enterEvent(event)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
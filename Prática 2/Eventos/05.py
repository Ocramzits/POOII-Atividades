import sys
from PySide6.QtCore import Qt
from PySide6.QtGui import QPainter, QPen
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget


class AreaDesenho(QWidget):
    def paintEvent(self, event):
        painter = QPainter(self)
        caneta = QPen(Qt.black, 2)
        painter.setPen(caneta)
        painter.drawLine(20, 20, self.width() - 20, self.height() - 20)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("paintEvent")
        self.setFixedSize(400, 300)
        self.setCentralWidget(AreaDesenho(self))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
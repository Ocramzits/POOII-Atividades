import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLineEdit, QLabel


class CampoDestacavel(QLineEdit):
    def focusInEvent(self, event):
        self.setStyleSheet("border: 2px solid blue;")
        super().focusInEvent(event)

    def focusOutEvent(self, event):
        self.setStyleSheet("")
        super().focusOutEvent(event)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("focusInEvent")
        self.setFixedSize(400, 300)

        self.info = QLabel("Clique no campo abaixo para destacar a borda")
        self.info.setAlignment(Qt.AlignCenter)
        self.campo = CampoDestacavel()

        layout = QVBoxLayout()
        layout.addWidget(self.info)
        layout.addWidget(self.campo)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
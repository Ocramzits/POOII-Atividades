import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QComboBox


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QComboBox")
        self.setFixedSize(400, 300)

        self.combo = QComboBox(self)
        self.combo.addItems(["Opção 1", "Opção 2", "Opção 3"])
        self.setCentralWidget(self.combo)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QCheckBox


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QCheckBox")
        self.setFixedSize(400, 300)

        self.checkbox = QCheckBox("Marcar opção", self)
        self.checkbox.setChecked(True)
        self.setCentralWidget(self.checkbox)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
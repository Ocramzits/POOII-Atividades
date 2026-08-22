import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QCheckBox


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QHBoxLayout com spacing")
        self.setFixedSize(400, 300)

        layout = QHBoxLayout()
        layout.setSpacing(20)

        layout.addWidget(QCheckBox("Opção 1"))
        layout.addWidget(QCheckBox("Opção 2"))
        layout.addWidget(QCheckBox("Opção 3"))

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel


class AreaComHover(QWidget):
    def __init__(self, label: QLabel):
        super().__init__()
        self.label = label
        self.setAttribute(Qt.WA_Hover, True)

    def hoverMoveEvent(self, event):
        pos = event.position()
        self.label.setText(f"Mouse em: ({pos.x():.0f}, {pos.y():.0f})")
        super().hoverMoveEvent(event)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("hoverMoveEvent")
        self.setFixedSize(400, 300)

        self.label = QLabel("Mova o mouse sobre a área")
        self.label.setAlignment(Qt.AlignCenter)

        area = AreaComHover(self.label)
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        area.setLayout(layout)

        self.setCentralWidget(area)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
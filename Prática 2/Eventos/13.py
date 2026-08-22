import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("tabletEvent")
        self.setFixedSize(400, 300)

        self.label = QLabel(
            "Use uma caneta/tablet sobre a janela\n"
            "(sem hardware de tablet, nada acontece)",
            self,
        )
        self.label.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(self.label)

    def tabletEvent(self, event):
        pressao = event.pressure()
        print(f"Pressão da caneta: {pressao}")
        self.label.setText(f"Pressão: {pressao:.2f}")
        super().tabletEvent(event)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
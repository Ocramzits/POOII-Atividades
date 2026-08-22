import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("wheelEvent")
        self.setFixedSize(400, 300)

        self.label = QLabel("Use a roda do mouse sobre a janela", self)
        self.label.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(self.label)

    def wheelEvent(self, event):
        direcao = "para cima" if event.angleDelta().y() > 0 else "para baixo"
        print(f"Roda do mouse: {direcao}")
        self.label.setText(f"Última rolagem: {direcao}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
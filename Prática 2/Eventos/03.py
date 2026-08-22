import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("resizeEvent")
        self.resize(400, 300)

        self.label = QLabel(self)
        self.label.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(self.label)
        self.atualizar_label_tamanho()

    def resizeEvent(self, event):
        self.atualizar_label_tamanho()
        super().resizeEvent(event)

    def atualizar_label_tamanho(self):
        self.label.setText(f"Tamanho: {self.width()}x{self.height()}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
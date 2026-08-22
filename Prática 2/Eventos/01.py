import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel
from PySide6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("keyPressEvent")
        self.setFixedSize(400, 300)

        self.label = QLabel("Aperte uma tecla do teclado...", self)
        self.setCentralWidget(self.label)
        self.label.setAlignment(Qt.AlignCenter)

    def keyPressEvent(self, event):
        tecla = event.text()
        print(f"Tecla pressionada: {tecla})")
        self.label.setText(f"Você apertou: {tecla}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
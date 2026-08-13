from PySide6.QtWidgets import QApplication, QSlider
import sys

class Classe_Slider(QSlider):
    def __init__(self):
        super().__init__()

    def emitir(self, valor):
        self.valueChanged.emit(valor)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    slider = Classe_Slider()
    slider.emitir(42)

    sys.exit(app.exec())
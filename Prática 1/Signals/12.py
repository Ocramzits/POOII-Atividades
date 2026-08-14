import sys
from PySide6.QtWidgets import QApplication, QComboBox

class SinalComboBox(QComboBox):
    def __init__(self):
        super().__init__()

    def emitir(self, indice):
        self.currentIndexChanged.emit(indice)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    combo = SinalComboBox()
    combo.emitir(0)

    sys.exit(app.exec())
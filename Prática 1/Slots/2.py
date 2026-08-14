import sys
from PySide6.QtWidgets import QApplication, QSpinBox

class SlotSpinBox(QSpinBox):
    def __init__(self):
        super().__init__()
        self.valueChanged.connect(self.receber)

    def receber(self, valor):
        print(valor)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    spin = SlotSpinBox()
    spin.show()

    sys.exit(app.exec())
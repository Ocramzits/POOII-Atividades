import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QDoubleSpinBox, QLabel
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Slot com float")

        self.spinbox = QDoubleSpinBox()
        self.spinbox.setRange(0, float("inf"))
        self.label = QLabel("Valor: 0.00")

        self.spinbox.valueChanged.connect(self.formatar_valor)

        layout = QVBoxLayout()
        layout.addWidget(self.spinbox)
        layout.addWidget(self.label)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def formatar_valor(self, valor: float):
        self.label.setText(f"Valor: {valor:.2f}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
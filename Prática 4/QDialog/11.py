import sys
from PySide6.QtWidgets import QApplication, QDialog, QVBoxLayout, QSpinBox, QLabel


class MeuDialogo(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Diálogo com QSpinBox")
        self.setFixedSize(300, 150)

        spinbox = QSpinBox()
        spinbox.setRange(0, 100)

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Escolha um valor:"))
        layout.addWidget(spinbox)
        self.setLayout(layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialogo = MeuDialogo()
    dialogo.show()
    sys.exit(app.exec())

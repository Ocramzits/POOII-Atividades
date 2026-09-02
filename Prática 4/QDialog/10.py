import sys
from PySide6.QtWidgets import QApplication, QDialog, QVBoxLayout, QComboBox


class MeuDialogo(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Diálogo com QComboBox")
        self.setFixedSize(300, 150)

        combo = QComboBox()
        combo.addItems(["Opção 1", "Opção 2", "Opção 3"])

        layout = QVBoxLayout()
        layout.addWidget(combo)
        self.setLayout(layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialogo = MeuDialogo()
    dialogo.show()
    sys.exit(app.exec())

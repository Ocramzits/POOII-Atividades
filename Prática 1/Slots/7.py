import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QComboBox
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Slot com QComboBox")

        self.combo = QComboBox()
        self.combo.addItems(["Opção 1", "Opção 2", "Opção 3"])

        self.combo.currentIndexChanged.connect(self.mostrar_indice)

        layout = QVBoxLayout()
        layout.addWidget(self.combo)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def mostrar_indice(self, indice: int):
        print(f"Índice atual: {indice}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
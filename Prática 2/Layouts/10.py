import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QGridLayout, QProgressBar, QLabel
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QProgressBar em QGridLayout")
        self.setFixedSize(400, 300)

        layout = QGridLayout()

        # Só pra dar contexto visual às outras células da linha 0
        layout.addWidget(QLabel("Coluna 0"), 0, 0)
        layout.addWidget(QLabel("Coluna 1"), 0, 1)

        barra = QProgressBar()
        barra.setValue(60)
        layout.addWidget(barra, 0, 2)  # linha 0, coluna 2

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
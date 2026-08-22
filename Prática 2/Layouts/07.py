import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QSlider


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QGridLayout 3x3")
        self.setFixedSize(400, 300)

        layout = QGridLayout()

        # Define explicitamente que a grade tem 3 linhas e 3 colunas,
        # mesmo só preenchendo uma célula — as demais ficam vazias.
        layout.setRowStretch(0, 1)
        layout.setRowStretch(1, 1)
        layout.setRowStretch(2, 1)
        layout.setColumnStretch(0, 1)
        layout.setColumnStretch(1, 1)
        layout.setColumnStretch(2, 1)

        slider = QSlider(Qt.Horizontal)
        layout.addWidget(slider, 1, 1)  # linha 1, coluna 1 (centro da grade)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
import sys
from PySide6.QtCore import Qt
from PySide6.QtGui import QAction
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QGridLayout, QSlider, QLabel
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Exercício 7 - QSlider + valueChanged")
        self.setFixedSize(400, 300)

        # --- Layout central (QGridLayout) ---
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setRange(50, 200)  # simula porcentagem de zoom
        self.slider.setValue(100)

        self.label_zoom = QLabel("Zoom: 100%")
        self.label_zoom.setAlignment(Qt.AlignCenter)

        self.slider.valueChanged.connect(self.atualizar_zoom)

        layout = QGridLayout()
        layout.addWidget(self.label_zoom, 0, 0)
        layout.addWidget(self.slider, 1, 0)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # --- QToolBar "Zoom" ---
        barra = self.addToolBar("Zoom")
        acao_resetar = QAction("Resetar Zoom", self)
        acao_resetar.triggered.connect(lambda: self.slider.setValue(100))
        barra.addAction(acao_resetar)

        # --- Menu "Ver" ---
        self.menuBar().addMenu("Ver")

    def atualizar_zoom(self, valor: int):
        self.label_zoom.setText(f"Zoom: {valor}%")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

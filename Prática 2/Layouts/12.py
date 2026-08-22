import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QStackedLayout, QComboBox, QLabel
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QStackedLayout + QComboBox")
        self.setFixedSize(400, 300)

        self.combo = QComboBox()
        self.combo.addItems(["Página 0", "Página 1", "Página 2"])
        self.combo.currentIndexChanged.connect(self.mudar_pagina)

        self.paginas = QStackedLayout()
        self.paginas.addWidget(QLabel("Conteúdo da página 0"))
        self.paginas.addWidget(QLabel("Conteúdo da página 1"))
        self.paginas.addWidget(QLabel("Conteúdo da página 2"))

        layout_principal = QVBoxLayout()
        layout_principal.addWidget(self.combo)
        layout_principal.addLayout(self.paginas)

        container = QWidget()
        container.setLayout(layout_principal)
        self.setCentralWidget(container)

    def mudar_pagina(self, indice: int):
        self.paginas.setCurrentIndex(indice)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
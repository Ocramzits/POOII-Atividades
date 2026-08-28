import sys
from PySide6.QtCore import Qt
from PySide6.QtGui import QAction
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QStackedLayout, QLabel
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Exercício 9 - QStackedLayout + resizeEvent")
        self.resize(400, 300)  # tamanho inicial, mas redimensionável

        # --- QStackedLayout ---
        self.paginas = QStackedLayout()
        self.label_pagina_1 = QLabel("Página 1")
        self.label_pagina_1.setAlignment(Qt.AlignCenter)
        self.paginas.addWidget(self.label_pagina_1)
        self.paginas.addWidget(QLabel("Página 2"))

        container = QWidget()
        container.setLayout(self.paginas)
        self.setCentralWidget(container)

        # --- QToolBar com QAction "Página 1" ---
        barra = self.addToolBar("Principal")
        acao_pagina_1 = QAction("Página 1", self)
        acao_pagina_1.triggered.connect(lambda: self.paginas.setCurrentIndex(0))
        barra.addAction(acao_pagina_1)

        # --- Menu "Navegação" ---
        self.menuBar().addMenu("Navegação")

    def resizeEvent(self, event):
        # Atualiza o texto da primeira página mostrando o tamanho atual da janela
        tamanho = event.size()
        self.label_pagina_1.setText(f"Página 1\nTamanho: {tamanho.width()}x{tamanho.height()}")
        super().resizeEvent(event)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

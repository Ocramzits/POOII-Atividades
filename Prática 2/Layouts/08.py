import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QStackedLayout, QLabel


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QStackedLayout com 3 páginas")
        self.setFixedSize(400, 300)

        self.layout_empilhado = QStackedLayout()
        self.layout_empilhado.addWidget(QLabel("Página 0"))  # índice 0
        self.layout_empilhado.addWidget(QLabel("Página 1"))  # índice 1
        self.layout_empilhado.addWidget(QLabel("Página 2"))  # índice 2

        # Muda diretamente para a página de índice 2
        self.layout_empilhado.setCurrentIndex(2)

        container = QWidget()
        container.setLayout(self.layout_empilhado)
        self.setCentralWidget(container)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QGridLayout com stretch igual")
        self.setFixedSize(400, 300)

        layout = QGridLayout()

        layout.addWidget(QPushButton("(0,0)"), 0, 0)
        layout.addWidget(QPushButton("(0,1)"), 0, 1)
        layout.addWidget(QPushButton("(1,0)"), 1, 0)
        layout.addWidget(QPushButton("(1,1)"), 1, 1)

        # Todas as linhas e colunas crescem na mesma proporção ao redimensionar
        # a janela, já que todo mundo tem stretch = 1 (nenhuma "ganha" espaço extra).
        layout.setRowStretch(0, 1)
        layout.setRowStretch(1, 1)
        layout.setColumnStretch(0, 1)
        layout.setColumnStretch(1, 1)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
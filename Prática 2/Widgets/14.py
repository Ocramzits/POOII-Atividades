import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QTabWidget, QLabel


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QTabWidget")
        self.setFixedSize(400, 300)

        abas = QTabWidget(self)

        aba_1 = QLabel("Conteúdo da primeira aba")
        aba_2 = QLabel("Conteúdo da segunda aba")

        abas.addTab(aba_1, "Aba 1")
        abas.addTab(aba_2, "Aba 2")

        self.setCentralWidget(abas)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QTableWidget")
        self.setFixedSize(400, 300)

        self.tabela = QTableWidget(2, 2, self)
        self.tabela.setHorizontalHeaderLabels(["Coluna 1", "Coluna 2"])
        self.tabela.setVerticalHeaderLabels(["Linha 1", "Linha 2"])

        self.tabela.setItem(0, 0, QTableWidgetItem("A1"))
        self.tabela.setItem(0, 1, QTableWidgetItem("B1"))
        self.tabela.setItem(1, 0, QTableWidgetItem("A2"))
        self.tabela.setItem(1, 1, QTableWidgetItem("B2"))

        self.setCentralWidget(self.tabela)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel
)
from PySide6.QtCore import QDate

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Slot com data atual")

        self.label = QLabel("Data: (clique no botão)")
        self.botao = QPushButton("Atualizar data")

        self.botao.clicked.connect(self.atualizar_data)

        layout = QVBoxLayout()
        layout.addWidget(self.botao)
        layout.addWidget(self.label)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def atualizar_data(self):
        data_atual = QDate.currentDate()
        self.label.setText(f"Data: {data_atual.toString('dd/MM/yyyy')}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
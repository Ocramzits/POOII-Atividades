import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel
)
from PySide6.QtCore import QTimer, QTime

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Slot com QTimer")

        self.label = QLabel("00:00:00")

        layout = QVBoxLayout()
        layout.addWidget(self.label)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.atualizar_relogio)
        self.timer.start(1000)  # dispara a cada 1000ms (1 segundo)

        self.atualizar_relogio()  # mostra a hora certa já de início, sem esperar 1s

    def atualizar_relogio(self):
        hora_atual = QTime.currentTime()
        self.label.setText(hora_atual.toString("hh:mm:ss"))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
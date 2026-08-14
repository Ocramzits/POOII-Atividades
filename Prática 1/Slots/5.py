import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Slot sem parâmetros")

        self.botao_sair = QPushButton("Sair")
        self.botao_sair.clicked.connect(self.fechar_janela)

        layout = QVBoxLayout()
        layout.addWidget(self.botao_sair)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def fechar_janela(self):
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
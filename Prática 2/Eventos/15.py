import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("showEvent")
        self.setFixedSize(400, 300)

        self.dados = None
        self.label = QLabel("Aguardando exibição da janela...", self)
        self.label.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(self.label)

    def showEvent(self, event):
        print("Janela sendo exibida — inicializando dados...")
        self.dados = {"carregado": True, "usuario": "Marco"}
        self.label.setText(f"Dados carregados: {self.dados}")
        super().showEvent(event)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
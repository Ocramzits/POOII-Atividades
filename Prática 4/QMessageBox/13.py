import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QMessageBox


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Confirmação ao fechar")
        self.setFixedSize(400, 300)

        self.setCentralWidget(QLabel("Feche a janela (X) para ver a confirmação"))

    def closeEvent(self, event):
        resposta = QMessageBox.question(
            self,
            "Confirmar saída",
            "Tem certeza que deseja fechar a aplicação?",
            QMessageBox.Yes | QMessageBox.No,
        )
        if resposta == QMessageBox.Yes:
            event.accept()  # permite o fechamento
        else:
            event.ignore()  # cancela o fechamento, janela continua aberta


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QMessageBox


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("closeEvent")
        self.setFixedSize(400, 300)

        self.label = QLabel("Feche a janela para ver a confirmação", self)
        self.label.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(self.label)

    def closeEvent(self, event):
        resposta = QMessageBox.question(
            self,
            "Confirmar saída",
            "Tem certeza que deseja sair?",
            QMessageBox.Yes | QMessageBox.No,
        )
        if resposta == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
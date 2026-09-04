import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QMessageBox.warning")
        self.setFixedSize(400, 300)

        botao = QPushButton("Mostrar aviso", self)
        botao.clicked.connect(self.mostrar_aviso)
        self.setCentralWidget(botao)

    def mostrar_aviso(self):
        # QMessageBox.Ok é o botão padrão de warning(), mas deixamos explícito
        QMessageBox.warning(
            self, "Atenção", "Algo pode não estar correto.", QMessageBox.Ok
        )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

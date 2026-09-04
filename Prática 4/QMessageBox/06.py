import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QMessageBox com HTML")
        self.setFixedSize(400, 300)

        botao = QPushButton("Mostrar mensagem formatada", self)
        botao.clicked.connect(self.mostrar_mensagem_html)
        self.setCentralWidget(botao)

    def mostrar_mensagem_html(self):
        caixa = QMessageBox(self)
        caixa.setWindowTitle("Mensagem formatada")
        # QMessageBox.setText aceita HTML básico: negrito, itálico, cor, links etc.
        caixa.setText(
            "<b>Operação concluída!</b><br>"
            "Consulte o <a href='https://doc.qt.io'>manual do Qt</a> para mais detalhes."
        )
        caixa.exec()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

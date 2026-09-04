import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QMessageBox Sim/Não/Cancelar")
        self.setFixedSize(400, 300)

        botao = QPushButton("Salvar alterações?", self)
        botao.clicked.connect(self.perguntar_salvar)
        self.setCentralWidget(botao)

    def perguntar_salvar(self):
        # Yes/No/Cancel são os nomes internos do Qt; o texto exibido
        # ("Sim"/"Não"/"Cancelar") já vem traduzido automaticamente conforme
        # o idioma do sistema operacional.
        resultado = QMessageBox.question(
            self,
            "Salvar alterações",
            "Deseja salvar as alterações antes de sair?",
            QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel,
        )

        if resultado == QMessageBox.Yes:
            print("Salvando e saindo...")
        elif resultado == QMessageBox.No:
            print("Saindo sem salvar...")
        else:
            print("Operação cancelada")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

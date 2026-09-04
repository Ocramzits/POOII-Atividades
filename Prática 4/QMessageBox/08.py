import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QMessageBox via slot")
        self.setFixedSize(400, 300)

        botao = QPushButton("Executar ação", self)
        botao.clicked.connect(self.executar_acao)  # conecta ao slot abaixo
        self.setCentralWidget(botao)

    def executar_acao(self):
        # Este é o slot: qualquer lógica pode rodar aqui antes de mostrar o aviso
        print("Executando ação...")
        QMessageBox.information(self, "Concluído", "Ação executada com sucesso.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

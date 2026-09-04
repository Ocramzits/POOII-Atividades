import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QMessageBox com texto detalhado")
        self.setFixedSize(400, 300)

        botao = QPushButton("Mostrar erro com detalhes", self)
        botao.clicked.connect(self.mostrar_erro_detalhado)
        self.setCentralWidget(botao)

    def mostrar_erro_detalhado(self):
        caixa = QMessageBox(self)
        caixa.setIcon(QMessageBox.Critical)
        caixa.setWindowTitle("Erro na operação")
        caixa.setText("Não foi possível concluir a operação.")

        # setDetailedText adiciona um botão "Mostrar Detalhes..." que expande
        # a caixa revelando um texto mais longo (útil para logs, stack traces).
        caixa.setDetailedText(
            "Log completo...\n"
            "[10:32:01] Iniciando operação\n"
            "[10:32:02] Erro: conexão recusada\n"
            "[10:32:02] Operação abortada"
        )

        caixa.exec()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

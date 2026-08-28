import sys
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QApplication, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QAction com slot de mensagem")
        self.setFixedSize(400, 300)

        menu_arquivo = self.menuBar().addMenu("Arquivo")

        acao_teste = QAction("Testar ação", self)
        acao_teste.triggered.connect(self.exibir_mensagem)
        menu_arquivo.addAction(acao_teste)

    def exibir_mensagem(self):
        print("Ação do menu executada com sucesso!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

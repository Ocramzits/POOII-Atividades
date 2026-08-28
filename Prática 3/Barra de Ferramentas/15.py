import sys
from PySide6.QtWidgets import QApplication, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QToolBar vazia + addAction")
        self.setFixedSize(400, 300)

        barra = self.addToolBar("Principal")  # começa vazia, sem nenhuma ação

        # addAction (com string) cria e adiciona o QAction em um único passo,
        # sem precisar instanciar QAction manualmente antes.
        acao = barra.addAction("Nova ação")
        acao.triggered.connect(lambda: print("Ação executada"))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

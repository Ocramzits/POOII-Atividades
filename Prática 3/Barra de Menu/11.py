import sys
from PySide6.QtWidgets import QApplication, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Menu Ferramentas vazio")
        self.setFixedSize(400, 300)

        menu_ferramentas = self.menuBar().addMenu("Ferramentas")  # começa vazio

        # addAction (com string) cria e adiciona o QAction em um único passo.
        acao = menu_ferramentas.addAction("Opções")
        acao.triggered.connect(lambda: print("Opções abertas"))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

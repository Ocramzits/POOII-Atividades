import sys
from PySide6.QtGui import QAction
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QStackedWidget, QLabel
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Exercício 4 - QStackedWidget + currentChanged")
        self.setFixedSize(400, 300)

        # QStackedWidget é usado aqui (em vez de QStackedLayout puro) porque
        # ele já emite o sinal currentChanged nativamente — QStackedLayout
        # sozinho não tem esse sinal embutido.
        self.paginas = QStackedWidget()
        self.paginas.addWidget(QLabel("Página 1"))
        self.paginas.addWidget(QLabel("Página 2"))
        self.paginas.addWidget(QLabel("Página 3"))
        self.paginas.currentChanged.connect(self.pagina_mudou)

        layout = QVBoxLayout()
        layout.addWidget(self.paginas)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # --- QToolBar "Próxima" ---
        barra = self.addToolBar("Principal")
        acao_proxima = QAction("Próxima", self)
        acao_proxima.triggered.connect(self.ir_para_proxima)
        barra.addAction(acao_proxima)

        # --- Menu "Navegação" ---
        self.menuBar().addMenu("Navegação")

    def ir_para_proxima(self):
        proximo_indice = (self.paginas.currentIndex() + 1) % self.paginas.count()
        self.paginas.setCurrentIndex(proximo_indice)

    def pagina_mudou(self, indice: int):
        print(f"Página atual agora é: {indice}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

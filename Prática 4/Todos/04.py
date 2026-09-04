import sys
from PySide6.QtCore import Signal
from PySide6.QtGui import QAction
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QStackedLayout, QLabel, QPushButton,
    QVBoxLayout
)


class JanelaSecundaria(QMainWindow):
    # Sinal que carrega o índice da página que deve ser exibida na principal
    pagina_selecionada = Signal(int)

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Janela Secundária - Seletor de página")
        self.setFixedSize(300, 200)

        botao_pagina_0 = QPushButton("Mostrar Página 0")
        botao_pagina_1 = QPushButton("Mostrar Página 1")
        botao_pagina_0.clicked.connect(lambda: self.pagina_selecionada.emit(0))
        botao_pagina_1.clicked.connect(lambda: self.pagina_selecionada.emit(1))

        layout = QVBoxLayout()
        layout.addWidget(botao_pagina_0)
        layout.addWidget(botao_pagina_1)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Exercício 4 - QStackedLayout + janela secundária")
        self.setFixedSize(400, 300)

        self.janela_secundaria = None

        # --- QStackedLayout ---
        self.paginas = QStackedLayout()
        self.paginas.addWidget(QLabel("Conteúdo da Página 0"))
        self.paginas.addWidget(QLabel("Conteúdo da Página 1"))

        container = QWidget()
        container.setLayout(self.paginas)
        self.setCentralWidget(container)

        # --- QToolBar com QAction "Janela 2" ---
        barra = self.addToolBar("Principal")
        acao_janela_2 = QAction("Janela 2", self)
        acao_janela_2.triggered.connect(self.abrir_janela_secundaria)
        barra.addAction(acao_janela_2)

    def abrir_janela_secundaria(self):
        self.janela_secundaria = JanelaSecundaria()
        self.janela_secundaria.pagina_selecionada.connect(self.paginas.setCurrentIndex)
        self.janela_secundaria.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

# 2. Use QHBoxLayout, QAction no menu "Ajuda > Sobre" que mostra QMessageBox,
#    e botão que abre janela secundária simples.
import sys
from PySide6.QtGui import QAction
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QHBoxLayout, QPushButton,
    QLabel, QMessageBox
)


class JanelaSecundaria(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Janela Secundária")
        self.setFixedSize(300, 200)
        self.setCentralWidget(QLabel("Janela simples aberta pelo botão"))


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Exercício 2 - HBox + menu Sobre + janela")
        self.setFixedSize(400, 300)

        self.janela_secundaria = None

        # --- Layout central (QHBoxLayout) ---
        botao_abrir_janela = QPushButton("Abrir janela secundária")
        botao_abrir_janela.clicked.connect(self.abrir_janela_secundaria)

        layout = QHBoxLayout()
        layout.addWidget(botao_abrir_janela)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # --- Menu Ajuda > Sobre ---
        menu_ajuda = self.menuBar().addMenu("Ajuda")
        acao_sobre = QAction("Sobre", self)
        acao_sobre.triggered.connect(self.mostrar_sobre)
        menu_ajuda.addAction(acao_sobre)

    def mostrar_sobre(self):
        QMessageBox.information(self, "Sobre", "Aplicativo de exemplo PySide6.")

    def abrir_janela_secundaria(self):
        self.janela_secundaria = JanelaSecundaria()
        self.janela_secundaria.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

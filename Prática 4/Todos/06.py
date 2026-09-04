# 6. Use menu "Janela > Nova" que abre QMainWindow secundária com QToolBar e
#    botão que dispara QMessageBox.
import sys
from PySide6.QtGui import QAction
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QMessageBox
)


class JanelaSecundaria(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Janela Secundária")
        self.setFixedSize(300, 200)

        # --- QToolBar da janela secundária ---
        barra = self.addToolBar("Principal")
        barra.addAction(QAction("Ação da secundária", self))

        botao = QPushButton("Mostrar aviso", self)
        botao.clicked.connect(self.mostrar_aviso)
        self.setCentralWidget(botao)

    def mostrar_aviso(self):
        QMessageBox.information(self, "Aviso", "Mensagem da janela secundária!")


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Exercício 6 - Menu Janela > Nova")
        self.setFixedSize(400, 300)

        self.janela_secundaria = None

        # --- Menu Janela > Nova ---
        menu_janela = self.menuBar().addMenu("Janela")
        acao_nova = QAction("Nova", self)
        acao_nova.triggered.connect(self.abrir_janela_secundaria)
        menu_janela.addAction(acao_nova)

    def abrir_janela_secundaria(self):
        self.janela_secundaria = JanelaSecundaria()
        self.janela_secundaria.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

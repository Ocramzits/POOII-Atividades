# 8. Configure QVBoxLayout + QToolBar, menu "Arquivo > Sair" mostra
#    QMessageBox.confirm e, se sim, fecha todas janelas.
#
# Observação: o método correto no PySide6 é QMessageBox.question() — não
# existe QMessageBox.confirm(). Usamos question() com botões Yes/No, que é
# o jeito padrão de pedir confirmação no Qt.
import sys
from PySide6.QtGui import QAction
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QMessageBox
)


class JanelaExtra(QMainWindow):
    def __init__(self, titulo: str):
        super().__init__()
        self.setWindowTitle(titulo)
        self.setFixedSize(250, 150)
        self.setCentralWidget(QLabel(f"Sou a {titulo}"))


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Exercício 8 - Sair fecha todas as janelas")
        self.setFixedSize(400, 300)

        # Duas janelas extras abertas junto com a principal, só para
        # demonstrar o fechamento de todas de uma vez.
        self.janela_extra_1 = JanelaExtra("Janela Extra 1")
        self.janela_extra_2 = JanelaExtra("Janela Extra 2")
        self.janela_extra_1.show()
        self.janela_extra_2.show()

        # --- Layout central (QVBoxLayout) ---
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Use o menu Arquivo > Sair para fechar tudo"))

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # --- QToolBar ---
        barra = self.addToolBar("Principal")
        barra.addAction(QAction("Ferramenta", self))

        # --- Menu Arquivo > Sair ---
        menu_arquivo = self.menuBar().addMenu("Arquivo")
        acao_sair = QAction("Sair", self)
        acao_sair.triggered.connect(self.confirmar_saida)
        menu_arquivo.addAction(acao_sair)

    def confirmar_saida(self):
        resposta = QMessageBox.question(
            self, "Confirmar saída", "Deseja fechar todas as janelas?",
            QMessageBox.Yes | QMessageBox.No
        )
        if resposta == QMessageBox.Yes:
            # closeAllWindows() fecha todas as janelas de nível superior
            # abertas pela aplicação, não só a principal.
            QApplication.instance().closeAllWindows()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox, QStyle


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QMessageBox com ícone personalizado")
        self.setFixedSize(400, 300)

        botao = QPushButton("Mostrar caixa com ícone", self)
        botao.clicked.connect(self.mostrar_caixa)
        self.setCentralWidget(botao)

    def mostrar_caixa(self):
        caixa = QMessageBox(self)
        caixa.setWindowTitle("Ícone personalizado")
        caixa.setText("Esta caixa usa um ícone customizado via setIconPixmap.")

        # Pega um ícone padrão do Qt e converte para QPixmap num tamanho customizado
        icone_padrao = self.style().standardIcon(QStyle.SP_DriveHDIcon)
        caixa.setIconPixmap(icone_padrao.pixmap(48, 48))

        caixa.exec()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

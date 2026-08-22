import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QMenu


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("contextMenuEvent")
        self.setFixedSize(400, 300)

        self.label = QLabel("Clique com o botão direito para abrir o menu", self)
        self.label.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(self.label)

    def contextMenuEvent(self, event):
        menu = QMenu(self)
        acao_1 = menu.addAction("Opção 1")
        acao_2 = menu.addAction("Opção 2")
        acao_sair = menu.addAction("Sair")

        acao_escolhida = menu.exec(event.globalPos())

        if acao_escolhida == acao_1:
            self.label.setText("Você escolheu: Opção 1")
        elif acao_escolhida == acao_2:
            self.label.setText("Você escolheu: Opção 2")
        elif acao_escolhida == acao_sair:
            self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
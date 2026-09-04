import sys
from PySide6.QtCore import Qt
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel


class JanelaPopup(QMainWindow):
    def __init__(self):
        # Qt.Popup faz a janela se comportar como um popup: sem barra de
        # título, e fecha sozinha ao perder o foco (clique fora dela).
        super().__init__(flags=Qt.Popup)
        self.setFixedSize(250, 150)
        self.setCentralWidget(QLabel("Sou um popup com menuBar"))

        menu = self.menuBar().addMenu("Opções")
        menu.addAction(QAction("Item 1", self))
        menu.addAction(QAction("Item 2", self))


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Janela Principal")
        self.setFixedSize(400, 300)

        self.popup = None

        botao = QPushButton("Abrir popup", self)
        botao.clicked.connect(self.abrir_popup)
        self.setCentralWidget(botao)

    def abrir_popup(self):
        self.popup = JanelaPopup()
        self.popup.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

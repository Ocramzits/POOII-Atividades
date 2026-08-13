from PySide6.QtWidgets import QApplication, QPushButton
from PySide6.QtCore import QObject, Signal
import sys

class SinalBotao(QObject):
    meuSinal = Signal()

    def __init__(self):
        super().__init__()

    def emitir(self):
        self.meuSinal.emit()

app = QApplication(sys.argv)
sinal_obj = SinalBotao()
window = QPushButton("Clique aqui")
window.clicked.connect(sinal_obj.emitir)

window.show()
sys.exit(app.exec())
from PySide6.QtCore import QObject, Signal

class Sinal(QObject):
    meuSinal = Signal() 

    def __init__(self):
        super().__init__()

    def emitir(self):
        self.meuSinal.emit()

obj = Sinal()
obj.emitir() 
from PySide6.QtCore import QObject, Signal

class SinalInteiro(QObject):
    sinal_int = Signal(int)

    def __init__(self):
        super().__init__()

    def emitir(self, valor):
        self.sinal_int.emit(valor)

obj = SinalInteiro()
obj.emitir(42)
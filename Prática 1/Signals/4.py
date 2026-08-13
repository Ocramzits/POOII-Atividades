from PySide6.QtCore import QObject, Signal

class SinalString(QObject):
    sinal_str = Signal(str)

    def __init__(self):
        super().__init__()

    def emitir(self, string):
        self.sinal_str.emit(string)

obj = SinalString()
obj.emitir("Olá, mundo!")
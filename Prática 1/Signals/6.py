from PySide6.QtCore import QObject, Signal

class SinalBooleano (QObject):
    Sinal_bool = Signal(bool)

    def __init__ (self):
        super().__init__()
        self.estado = True

    def emitir(self):
        self.Sinal_bool.emit(self.estado)
        self.estado = not self.estado

obj = SinalBooleano()
obj.emitir()
obj.emitir()
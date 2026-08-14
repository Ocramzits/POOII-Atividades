from PySide6.QtCore import Signal, QObject

class SinalFloat (QObject):
    sinal_real = Signal(float)

    def __init__ (self):
        super().__init__()

    def emitir (self, valor):
        self.sinal_real.emit(valor)

if __name__ == "__main__":
    obj = SinalFloat()
    obj.emitir(3.14)
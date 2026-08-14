from PySide6.QtCore import Signal, QObject

class SinalLista(QObject):
    SinalLista = Signal(list)

    def __init__(self):
        super().__init__()

    def emitir(self, lista):
        self.SinalLista.emit(lista)

obj = SinalLista()
obj.emitir([])
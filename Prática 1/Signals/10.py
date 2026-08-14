from PySide6.QtCore import Signal, QObject

class SinalDicionario(QObject):
    SinalDict = Signal(dict)

    def __init__ (self):
        super().__init__()

    def emitir (self, dicionario):
        self.SinalDict.emit(dicionario)

if __name__ == "__main__":
    obj = SinalDicionario()
    obj.emitir({"Valor": 10})
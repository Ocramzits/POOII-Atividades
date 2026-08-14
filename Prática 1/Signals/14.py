from PySide6.QtCore import Signal, QObject

class Contador(QObject):
    valor_mudou = Signal(int)

    def __init__(self):
        super().__init__()
        self._valor = 0

    @property
    def valor(self):
        return self._valor

    @valor.setter
    def valor(self, novo_valor):
        if novo_valor != self._valor:
            self._valor = novo_valor
            self.valor_mudou.emit(self._valor)

if __name__ == "__main__":
    obj = Contador()
    obj.valor = 10
    obj.valor = 25
    obj.valor = 25  # não emite, pois o valor não mudou
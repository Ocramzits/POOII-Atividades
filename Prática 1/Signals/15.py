from PySide6.QtCore import Signal, QObject

class Pessoa:
    def __init__(self, nome=None, idade=None):
        self.nome = nome
        self.idade = idade

class SinalPessoa(QObject):
    sinal_pessoa = Signal(object)

    def __init__(self):
        super().__init__()

    def emitir(self, pessoa):
        self.sinal_pessoa.emit(pessoa)

if __name__ == "__main__":
    obj = SinalPessoa()
    obj.emitir(Pessoa())
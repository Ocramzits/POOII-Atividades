import sys
from PySide6.QtCore import QObject, Signal, QTimer
from PySide6.QtWidgets import QApplication

class SinalTimer(QObject):
    sinaltime = Signal()

    def __init__(self):
        super().__init__()
        self.timer = QTimer()
        self.timer.timeout.connect(self.emitir)

    def emitir(self):
        self.sinaltime.emit()

    def iniciar(self, intervalo_ms):
        self.timer.start(intervalo_ms)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    obj = SinalTimer()
    obj.iniciar(1000)  # a cada 1 segundo

    app.exec()

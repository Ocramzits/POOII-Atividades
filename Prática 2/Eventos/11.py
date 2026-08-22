import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("dragEnterEvent + dropEvent")
        self.setFixedSize(400, 300)
        self.setAcceptDrops(True)

        self.label = QLabel("Arraste e solte um texto aqui", self)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.setCentralWidget(self.label)

    def dragEnterEvent(self, event):
        if event.mimeData().hasText():
            event.acceptProposedAction()

    def dropEvent(self, event):
        texto = event.mimeData().text()
        print(f"Texto dropado: {texto}")
        self.label.setText(f"Recebido: {texto}")
        event.acceptProposedAction()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
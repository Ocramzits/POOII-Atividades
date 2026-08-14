import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QCheckBox, QLabel
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Slot booleano com QCheckBox")

        self.label = QLabel("Estou visível!")
        self.checkbox = QCheckBox("Mostrar label")
        self.checkbox.setChecked(True)  # começa marcado, label visível

        self.checkbox.stateChanged.connect(self.alterar_visibilidade)

        layout = QVBoxLayout()
        layout.addWidget(self.checkbox)
        layout.addWidget(self.label)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def alterar_visibilidade(self, estado: int):
        self.label.setVisible(bool(estado))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
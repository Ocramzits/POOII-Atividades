import sys
from PySide6.QtGui import QAction
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QGridLayout, QCheckBox, QLabel
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Exercício 3 - QAction toggleable")
        self.setFixedSize(400, 300)

        # --- Layout central (QGridLayout) ---
        self.checkbox = QCheckBox("Mostrar mensagem")
        self.checkbox.setChecked(True)
        self.checkbox.stateChanged.connect(self.alternar_visibilidade)

        self.label_secreto = QLabel("Você está me vendo!")

        layout = QGridLayout()
        layout.addWidget(self.checkbox, 0, 0)
        layout.addWidget(self.label_secreto, 1, 0)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # --- QToolBar com QAction toggleable ---
        barra = self.addToolBar("Principal")
        acao_alternar = QAction("Alternar mensagem", self)
        acao_alternar.setCheckable(True)
        acao_alternar.setChecked(True)
        acao_alternar.toggled.connect(self.checkbox.setChecked)
        barra.addAction(acao_alternar)

        # --- Menu "Ver" ---
        self.menuBar().addMenu("Ver")

    def alternar_visibilidade(self, estado: int):
        self.label_secreto.setVisible(bool(estado))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QRadioButton, QGroupBox
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QRadioButton em grupo")
        self.setFixedSize(400, 300)

        grupo = QGroupBox("Escolha uma opção")
        layout_grupo = QVBoxLayout()

        self.opcao_1 = QRadioButton("Opção 1")
        self.opcao_2 = QRadioButton("Opção 2")
        self.opcao_3 = QRadioButton("Opção 3")
        self.opcao_1.setChecked(True)

        layout_grupo.addWidget(self.opcao_1)
        layout_grupo.addWidget(self.opcao_2)
        layout_grupo.addWidget(self.opcao_3)
        grupo.setLayout(layout_grupo)

        layout = QVBoxLayout()
        layout.addWidget(grupo)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QGroupBox, QVBoxLayout, QLabel, QLineEdit, QCheckBox
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QGroupBox")
        self.setFixedSize(400, 300)

        grupo = QGroupBox("Dados do usuário")
        layout_grupo = QVBoxLayout()

        layout_grupo.addWidget(QLabel("Nome:"))
        layout_grupo.addWidget(QLineEdit())
        layout_grupo.addWidget(QCheckBox("Aceito os termos"))

        grupo.setLayout(layout_grupo)
        self.setCentralWidget(grupo)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
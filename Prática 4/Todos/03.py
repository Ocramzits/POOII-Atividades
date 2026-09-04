import sys
from PySide6.QtGui import QAction
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QGridLayout, QLabel,
    QDialog, QVBoxLayout, QMessageBox
)


class MeuDialogo(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Diálogo condicional")
        self.setFixedSize(300, 150)

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Você confirmou! Este diálogo só abre com Yes."))
        self.setLayout(layout)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Exercício 3 - Grid + Alert + question + dialog")
        self.setFixedSize(400, 300)

        # --- Layout central (QGridLayout) ---
        layout = QGridLayout()
        layout.addWidget(QLabel("Use a toolbar 'Alert' para testar"), 0, 0)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # --- QToolBar "Alert" ---
        barra = self.addToolBar("Principal")
        acao_alert = QAction("Alert", self)
        acao_alert.triggered.connect(self.perguntar_e_abrir)
        barra.addAction(acao_alert)

        # --- Menu "Editar" ---
        self.menuBar().addMenu("Editar")

    def perguntar_e_abrir(self):
        resposta = QMessageBox.question(
            self, "Confirmação", "Deseja abrir o diálogo?",
            QMessageBox.Yes | QMessageBox.No
        )
        if resposta == QMessageBox.Yes:
            dialogo = MeuDialogo()
            dialogo.exec()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

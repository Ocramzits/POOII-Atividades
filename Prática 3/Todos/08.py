import sys
from PySide6.QtCore import Qt
from PySide6.QtGui import QAction
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QMessageBox
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Exercício 8 - closeEvent")
        self.setFixedSize(400, 300)

        # --- Layout central (QVBoxLayout) ---
        self.label = QLabel("Feche a janela para ver a confirmação")
        self.label.setAlignment(Qt.AlignCenter)

        layout = QVBoxLayout()
        layout.addWidget(self.label)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # --- QToolBar "Imprimir" ---
        barra = self.addToolBar("Principal")
        acao_imprimir = QAction("Imprimir", self)
        acao_imprimir.triggered.connect(self.imprimir)
        barra.addAction(acao_imprimir)

        # --- Menu "Arquivo" ---
        self.menuBar().addMenu("Arquivo")

    def imprimir(self):
        self.label.setText("Imprimindo...")

    def closeEvent(self, event):
        resposta = QMessageBox.question(
            self,
            "Confirmar saída",
            "Tem certeza que deseja sair?",
            QMessageBox.Yes | QMessageBox.No,
        )
        if resposta == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

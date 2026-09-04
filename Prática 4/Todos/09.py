import sys
from PySide6.QtGui import QAction
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QDialog, QVBoxLayout, QLabel, QMessageBox
)


class MeuDialogo(QDialog):
    def __init__(self, janela_principal):
        super().__init__()
        self.janela_principal = janela_principal
        self.setWindowTitle("Diálogo modal com alerta")
        self.setFixedSize(300, 150)

        # Alerta mostrado assim que o diálogo é aberto
        QMessageBox.information(self, "Alerta", "Este é um diálogo modal.")

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Feche esta janela para atualizar a status bar"))
        self.setLayout(layout)

    def closeEvent(self, event):
        # Atualiza a status bar da janela principal quando o diálogo fecha
        self.janela_principal.statusBar().showMessage("Diálogo foi fechado", 5000)
        event.accept()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Exercício 9 - Diálogo + closeEvent + statusBar")
        self.setFixedSize(400, 300)

        self.statusBar().showMessage("Pronto")

        barra = self.addToolBar("Principal")
        acao_dialogo = QAction("Diálogo", self)
        acao_dialogo.triggered.connect(self.abrir_dialogo)
        barra.addAction(acao_dialogo)

    def abrir_dialogo(self):
        dialogo = MeuDialogo(self)
        dialogo.exec()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

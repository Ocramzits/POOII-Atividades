# 7. Crie QDialog com QLineEdit, botão OK mostra QMessageBox e fecha,
#    enviando texto via sinal para QLabel da principal.
import sys
from PySide6.QtCore import Signal
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton,
    QDialog, QLineEdit, QMessageBox, QLabel
)


class MeuDialogo(QDialog):
    texto_enviado = Signal(str)

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Diálogo com envio de texto")
        self.setFixedSize(300, 150)

        self.campo = QLineEdit()
        self.campo.setPlaceholderText("Digite seu nome...")

        botao_ok = QPushButton("OK")
        botao_ok.clicked.connect(self.confirmar_e_fechar)

        layout = QVBoxLayout()
        layout.addWidget(self.campo)
        layout.addWidget(botao_ok)
        self.setLayout(layout)

    def confirmar_e_fechar(self):
        texto = self.campo.text()
        QMessageBox.information(self, "Confirmado", f"Texto enviado: {texto}")
        self.texto_enviado.emit(texto)
        self.accept()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Exercício 7 - QDialog + sinal de texto")
        self.setFixedSize(400, 300)

        self.label = QLabel("Aguardando texto do diálogo...")

        botao_abrir = QPushButton("Abrir diálogo")
        botao_abrir.clicked.connect(self.abrir_dialogo)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(botao_abrir)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def abrir_dialogo(self):
        dialogo = MeuDialogo()
        dialogo.texto_enviado.connect(self.atualizar_label)
        dialogo.exec()

    def atualizar_label(self, texto: str):
        self.label.setText(f"Texto recebido: {texto}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

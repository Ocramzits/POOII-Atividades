import sys
from PySide6.QtWidgets import QApplication, QDialog, QVBoxLayout, QLabel, QDialogButtonBox


class MeuDialogo(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Diálogo com QDialogButtonBox")
        self.setFixedSize(300, 150)

        botoes = QDialogButtonBox(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        )
        botoes.accepted.connect(self.accept)  # botão OK dispara accept()
        botoes.rejected.connect(self.reject)  # botão Cancel dispara reject()

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Confirme ou cancele a ação"))
        layout.addWidget(botoes)
        self.setLayout(layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialogo = MeuDialogo()
    resultado = dialogo.exec()
    print("Aceito" if resultado == QDialog.Accepted else "Cancelado")

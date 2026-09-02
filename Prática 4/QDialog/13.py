import sys
from PySide6.QtWidgets import QApplication, QDialog, QVBoxLayout, QHBoxLayout, QPushButton, QLabel


class MeuDialogo(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Diálogo com accept/reject manuais")
        self.setFixedSize(300, 150)

        botao_ok = QPushButton("OK")
        botao_cancelar = QPushButton("Cancelar")

        # accept() e reject() são métodos nativos de QDialog: fecham a janela
        # e definem o valor de retorno de exec() (Accepted ou Rejected).
        botao_ok.clicked.connect(self.accept)
        botao_cancelar.clicked.connect(self.reject)

        layout_botoes = QHBoxLayout()
        layout_botoes.addWidget(botao_ok)
        layout_botoes.addWidget(botao_cancelar)

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Deseja continuar?"))
        layout.addLayout(layout_botoes)
        self.setLayout(layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialogo = MeuDialogo()
    resultado = dialogo.exec()
    print("Aceito" if resultado == QDialog.Accepted else "Rejeitado")

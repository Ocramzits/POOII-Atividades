import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QLabel

class Janela(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Slot com QLabel")

        layout = QVBoxLayout(self)

        self.campo_texto = QLineEdit()
        self.label_exibicao = QLabel("Digite algo acima...")

        layout.addWidget(self.campo_texto)
        layout.addWidget(self.label_exibicao)

        # Conecta o sinal textChanged ao slot
        self.campo_texto.textChanged.connect(self.atualizar_label)

    def atualizar_label(self, texto: str):
        self.label_exibicao.setText(texto)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = Janela()
    janela.show()
    sys.exit(app.exec())
import sys
from PySide6.QtWidgets import QApplication, QDialog, QVBoxLayout, QLabel, QStyle


class MeuDialogo(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Diálogo com ícone")
        self.setFixedSize(300, 150)

        # Usa um ícone padrão do próprio conjunto de estilos do Qt,
        # sem depender de arquivo de imagem externo.
        icone = self.style().standardIcon(QStyle.SP_MessageBoxInformation)
        self.setWindowIcon(icone)

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Este diálogo tem um ícone na barra de título"))
        self.setLayout(layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialogo = MeuDialogo()
    dialogo.show()
    sys.exit(app.exec())

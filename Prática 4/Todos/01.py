import sys
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QAction
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel,
    QDialog, QPushButton, QMessageBox
)


class MeuDialogo(QDialog):
    # Sinal customizado que carrega um texto para a janela principal
    dados_confirmados = Signal(str)

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Diálogo de boas-vindas")
        self.setFixedSize(300, 150)

        # QMessageBox de boas-vindas, mostrado assim que o diálogo é criado
        QMessageBox.information(self, "Bem-vindo", "Diálogo aberto com sucesso!")

        botao = QPushButton("Confirmar e fechar")
        botao.clicked.connect(self.confirmar)

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Clique para confirmar"))
        layout.addWidget(botao)
        self.setLayout(layout)

    def confirmar(self):
        self.dados_confirmados.emit("Diálogo confirmado pelo usuário")
        self.accept()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Exercício 1 - Integração completa")
        self.setFixedSize(400, 300)

        # --- Layout central (QVBoxLayout) ---
        self.label = QLabel("Aguardando ação do diálogo...")
        self.label.setAlignment(Qt.AlignCenter)

        layout = QVBoxLayout()
        layout.addWidget(self.label)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # --- QToolBar "Nova Janela" ---
        barra = self.addToolBar("Principal")
        barra.addAction(QAction("Nova Janela", self))

        # --- Menu Arquivo > Abrir Diálogo ---
        menu_arquivo = self.menuBar().addMenu("Arquivo")
        acao_abrir_dialogo = QAction("Abrir Diálogo", self)
        acao_abrir_dialogo.triggered.connect(self.abrir_dialogo)
        menu_arquivo.addAction(acao_abrir_dialogo)

    def abrir_dialogo(self):
        dialogo = MeuDialogo()
        dialogo.dados_confirmados.connect(self.atualizar_label)
        dialogo.exec()

    def atualizar_label(self, texto: str):
        self.label.setText(texto)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

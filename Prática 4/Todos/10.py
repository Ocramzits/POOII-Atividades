# 10. Use QHBoxLayout, menu "Ver > Alerta", clique mostra QMessageBox e abre
#     janela secundária com QLabel atualizado via slot.
import sys
from PySide6.QtCore import Signal
from PySide6.QtGui import QAction
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QHBoxLayout, QLabel, QMessageBox,
    QPushButton, QVBoxLayout
)


class JanelaSecundaria(QMainWindow):
    # Sinal emitido quando o usuário clica no botão desta janela
    atualizar_solicitado = Signal(str)

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Janela Secundária")
        self.setFixedSize(300, 200)

        self.label = QLabel("Aguardando atualização...")
        botao = QPushButton("Atualizar label")
        botao.clicked.connect(self.solicitar_atualizacao)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(botao)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def solicitar_atualizacao(self):
        self.atualizar_solicitado.emit("Label atualizado via sinal!")

    def atualizar_label(self, texto: str):
        # Este é o slot conectado ao próprio sinal desta janela
        self.label.setText(texto)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Exercício 10 - HBox + menu Alerta + janela")
        self.setFixedSize(400, 300)

        self.janela_secundaria = None

        # --- Layout central (QHBoxLayout) ---
        layout = QHBoxLayout()
        layout.addWidget(QLabel("Use o menu Ver > Alerta"))

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # --- Menu Ver > Alerta ---
        menu_ver = self.menuBar().addMenu("Ver")
        acao_alerta = QAction("Alerta", self)
        acao_alerta.triggered.connect(self.mostrar_alerta_e_abrir_janela)
        menu_ver.addAction(acao_alerta)

    def mostrar_alerta_e_abrir_janela(self):
        QMessageBox.information(self, "Alerta", "Abrindo janela secundária...")

        self.janela_secundaria = JanelaSecundaria()
        # O próprio sinal da janela secundária é conectado ao seu próprio slot,
        # formando um ciclo interno de atualização controlado pelo botão dela.
        self.janela_secundaria.atualizar_solicitado.connect(
            self.janela_secundaria.atualizar_label
        )
        self.janela_secundaria.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

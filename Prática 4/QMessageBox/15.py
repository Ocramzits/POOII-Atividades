import sys
from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QMessageBox com timeout via QTimer")
        self.setFixedSize(400, 300)

        botao = QPushButton("Mostrar aviso temporário (fecha em 3s)", self)
        botao.clicked.connect(self.mostrar_aviso_temporario)
        self.setCentralWidget(botao)

    def mostrar_aviso_temporario(self):
        # QMessageBox.information() por si só não tem parâmetro de timeout
        # nativo — por isso criamos a caixa manualmente e usamos um QTimer
        # para fechá-la sozinha após alguns segundos, caso o usuário não
        # feche antes.
        caixa = QMessageBox(self)
        caixa.setWindowTitle("Aviso temporário")
        caixa.setText("Esta mensagem fecha sozinha em 3 segundos.")
        caixa.setStandardButtons(QMessageBox.NoButton)  # sem botão, só o timer fecha

        QTimer.singleShot(3000, caixa.close)  # fecha automaticamente após 3000ms

        caixa.exec()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

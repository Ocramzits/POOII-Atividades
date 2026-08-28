import sys
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QApplication, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Submenu Recente dinâmico")
        self.setFixedSize(400, 300)

        menu_arquivo = self.menuBar().addMenu("Arquivo")
        submenu_recente = menu_arquivo.addMenu("Recente")

        # Lista de arquivos "recentes" simulada — na prática viria de algum
        # histórico salvo (arquivo de config, banco de dados, etc.).
        arquivos_recentes = [
            "relatorio_final.docx",
            "planilha_vendas.xlsx",
            "apresentacao_projeto.pptx",
        ]

        # Cria os QAction dinamicamente, um para cada item da lista
        for caminho_arquivo in arquivos_recentes:
            acao = QAction(caminho_arquivo, self)
            # lambda com argumento padrão (arquivo=caminho_arquivo) evita o
            # problema clássico de closure tardia em loops
            acao.triggered.connect(
                lambda checked=False, arquivo=caminho_arquivo: self.abrir_recente(arquivo)
            )
            submenu_recente.addAction(acao)

    def abrir_recente(self, nome_arquivo: str):
        print(f"Abrindo arquivo recente: {nome_arquivo}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

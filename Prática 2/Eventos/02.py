import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel
 
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("mousePressEvent")
        self.setFixedSize(400, 300)
 
        self.label = QLabel("Clique em qualquer lugar da janela", self)
        self.label.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(self.label)
 
    def mousePressEvent(self, event):
        self.setStyleSheet("background-color: red")

    def mouseReleaseEvent(self, event):
        self.setStyleSheet("background-color: black;")      
 
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
 

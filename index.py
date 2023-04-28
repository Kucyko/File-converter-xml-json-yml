from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
def main():
    app = QApplication([])
    window = QWidget()
    window.setGeometry(100, 100, 200, 300)
    window.setWindowTitle("Konwerter")
    layout = QVBoxLayout()
    label = QLabel("Press")
    button = QPushButton("Press")
    button.clicked.connect(on_click)
    layout.addWidget(label)
    layout.addWidget(button)
    window.setLayout(layout)
    window.show()
    app.exec_()
def on_click():
    message = QMessageBox()
    message.setText("Hello world")
    message.exec_()
if __name__ == '__main__':
    main()
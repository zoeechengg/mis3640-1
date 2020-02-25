import sys

from PyQt5.QtWidgets import QApplication, QWidget, QTextBrowser, QPushButton, QVBoxLayout, QInputDialog


class SimpleWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('A Simple Example for PyQt')
        self.outputArea = QTextBrowser(self)
        self.helloButton = QPushButton("Greeting", self)
        self.setLayout(QVBoxLayout())
        self.layout().addWidget(self.outputArea)
        self.layout().addWidget(self.helloButton)

        self.helloButton.clicked.connect(self.sayHello)

    def sayHello(self):
        user_name, okay = QInputDialog.getText(self, "What is your name?", 'Name:')
        if not okay or user_name == '':
            self.outputArea.append("Hello, stranger!")
        else:
            self.outputArea.append(f"Hello, <b>{user_name}</b>.")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    testWidget = SimpleWidget()
    testWidget.show()
    sys.exit(app.exec_())

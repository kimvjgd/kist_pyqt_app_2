import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QStackedWidget

class HelpWindow(QWidget):
    def __init__(self, stack):
        super().__init__()
        self.stack = stack
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        
        label = QLabel('Help Window')
        layout.addWidget(label)

        info_button = QPushButton('Go to Info')
        info_button.clicked.connect(self.gotoInfo)
        layout.addWidget(info_button)

        self.setLayout(layout)

    def gotoInfo(self):
        self.stack.setCurrentIndex(1)  # Switch to the Info window

class InfoWindow(QWidget):
    def __init__(self, stack):
        super().__init__()
        self.stack = stack
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        
        label = QLabel('Info Window')
        layout.addWidget(label)

        back_button = QPushButton('Back to Help')
        back_button.clicked.connect(self.goBack)
        layout.addWidget(back_button)

        self.setLayout(layout)

    def goBack(self):
        self.stack.setCurrentIndex(0)  # Switch back to the Help window

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Main Window')
        self.setGeometry(300, 300, 400, 200)

        # Stack to manage the two windows
        self.stack = QStackedWidget(self)
        self.help_window = HelpWindow(self.stack)
        self.info_window = InfoWindow(self.stack)
        
        self.stack.addWidget(self.help_window)
        self.stack.addWidget(self.info_window)
        
        layout = QVBoxLayout()
        layout.addWidget(self.stack)
        self.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())

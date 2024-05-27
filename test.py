import sys
import requests
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QComboBox, QLabel
from PyQt6.QtGui import QFont
from datetime import datetime


class KibabApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        
        today = datetime.today()
        today_str = 'kibab_' + today.strftime('%Y%m%d')
        
        
        # Add a label
        label = QLabel('오늘의 키밥 메뉴:')
        temp_font = QFont()
        temp_font.setPointSize(20)
        label.setFont(temp_font)
        layout.addWidget(label)

        # Create a combo box
        self.combo_box = QComboBox(self)
        
        # Fetch the Python file from GitHub
        url = 'https://raw.githubusercontent.com/kimvjgd/kist_pyqt_app_2/main/kibab.py'
        response = requests.get(url)
        if response.status_code == 200:
            # Create a dictionary to hold the executed variables
            local_vars = {}
            # Execute the content of the fetched file
            exec(response.text, globals(), local_vars)
            # Access the variable from the local_vars dictionary

            kibab_20240528 = local_vars[today_str]
            # Add items to the combo box from kibab_20240528
            for item in kibab_20240528:
                self.combo_box.addItem(item[0])
        
        layout.addWidget(self.combo_box)
        
        self.setLayout(layout)
        self.setWindowTitle('Kibab Menu')
        self.setGeometry(300, 300, 400, 200)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    kibab_app = KibabApp()
    kibab_app.show()
    sys.exit(app.exec())

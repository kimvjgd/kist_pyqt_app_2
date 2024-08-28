import sys
from PyQt6.QtCore import Qt, QBasicTimer, QTime, QDate, QDateTime, QCoreApplication
from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QMenu, QCheckBox, QLabel, QPushButton, QToolTip, \
    QHBoxLayout, QVBoxLayout, QRadioButton, QLineEdit, QComboBox, QProgressBar, QSlider, QDial, QSplitter, QGroupBox, \
        QSpinBox, QDoubleSpinBox, QTabWidget, QTimeEdit, QDateTimeEdit, QDateEdit, QCalendarWidget, QTextEdit, QTextBrowser, \
        QInputDialog, QMessageBox, QFontDialog, QColorDialog, QFrame, QFileDialog, QTableWidget, QTableWidgetItem, QHeaderView
from PyQt6.QtGui import QIcon, QPixmap, QFont, QColor
import urllib.request
import json
import requests
from pathlib import Path
from datetime import datetime

# 메뉴 데이터
breakfast_menu = []
lunch_menu = []
dinner_menu = []

class kibab_tab5(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        today = datetime.today()
        # today_str = 'kibab_' + today.strftime('%Y%m%d')
        url = 'https://raw.githubusercontent.com/kimvjgd/kist_pyqt_app_2/main/kibab.py'
        response = requests.get(url)
        print(response.text)
        if response.status_code == 200:
            # Create a dictionary to hold the executed variables
            local_vars = {}
            # Execute the content of the fetched file
            exec(response.text, globals(), local_vars)
            # Access the variable from the local_vars dictionary

            # kibab_20240528 = local_vars[today_str]
            # print(kibab_20240528)
            # Add items to the combo box from kibab_20240528
            # breakfast_menu = [kibab_20240528[0]]
            # lunch_menu = kibab_20240528[1:4]
            # dinner_menu = [kibab_20240528[4]]

        layout = QVBoxLayout()
        # 타이틀 레이블
        title_label = QLabel("Today's Menu")
        title_label.setStyleSheet("font-size: 24px;")
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title_label)

        # 테이블 위젯
        menu_table = QTableWidget()
        menu_table.setRowCount(3)
        menu_table.setColumnCount(1)
        menu_table.setHorizontalHeaderLabels(['Menu'])
        menu_table.setVerticalHeaderLabels(['조  식', '중  식', '석  식'])
        
        # 메뉴 아이템 추가
        self.addMenuItems(menu_table, breakfast_menu, 0)
        self.addMenuItems(menu_table, lunch_menu, 1)
        self.addMenuItems(menu_table, dinner_menu, 2)

        menu_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        menu_table.verticalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        layout.addWidget(menu_table)

        self.setLayout(layout)
        self.setWindowTitle('Daily Menu')
        self.setGeometry(100, 100, 400, 300)

    def addMenuItems(self, table, menu, row):
        items = '\n\n'.join(menu)
        table.setItem(row, 0, QTableWidgetItem(items))
    

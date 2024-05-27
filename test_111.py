import sys
import requests
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QTableWidget, QTableWidgetItem, QHeaderView
from PyQt6.QtGui import QFont
from qt_material import apply_stylesheet
from PyQt6.QtCore import Qt, QBasicTimer, QTime, QDate, QDateTime, QCoreApplication

class KibabApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # 타이틀 레이블
        title_label = QLabel("오늘의 키밥 메뉴")
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        temp_font = QFont()
        temp_font.setPointSize(24)
        title_label.setFont(temp_font)
        layout.addWidget(title_label)

        # 테이블 위젯
        menu_table = QTableWidget()
        menu_table.setRowCount(3)
        menu_table.setColumnCount(1)
        menu_table.setHorizontalHeaderLabels(['메뉴'])
        menu_table.setVerticalHeaderLabels(['조식', '중식', '석식'])

        # GitHub에서 Python 파일 가져오기
        url = 'https://raw.githubusercontent.com/kimvjgd/kist_pyqt_app_2/main/kibab.py'
        response = requests.get(url)
        if response.status_code == 200:
            local_vars = {}
            exec(response.text, globals(), local_vars)
            kibab_20240528 = local_vars['kibab_20240528']
            
            # 메뉴 아이템 추가
            self.addMenuItems(menu_table, kibab_20240528[0], 0)  # 조식
            self.addMenuItems(menu_table, kibab_20240528[1:4], 1)  # 중식
            self.addMenuItems(menu_table, kibab_20240528[4], 2)  # 석식

        menu_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        menu_table.verticalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        layout.addWidget(menu_table)

        self.setLayout(layout)
        self.setWindowTitle('Kibab Menu')
        self.setGeometry(300, 300, 400, 300)

    def addMenuItems(self, table, menu, row):
        if isinstance(menu, list) and isinstance(menu[0], list):
            items = '\n'.join([item[0] for item in menu])
        else:
            items = menu[0]
        table.setItem(row, 0, QTableWidgetItem(items))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    apply_stylesheet(app, theme='dark_teal.xml')
    kibab_app = KibabApp()
    kibab_app.show()
    sys.exit(app.exec())

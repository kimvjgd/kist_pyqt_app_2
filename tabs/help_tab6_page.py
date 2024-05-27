import sys
from PyQt6.QtCore import Qt, QBasicTimer, QTime, QDate, QDateTime, QCoreApplication
from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QMenu, QCheckBox, QLabel, QPushButton, QToolTip, \
    QHBoxLayout, QVBoxLayout, QRadioButton, QLineEdit, QComboBox, QProgressBar, QSlider, QDial, QSplitter, QGroupBox, \
        QSpinBox, QDoubleSpinBox, QTabWidget, QTimeEdit, QDateTimeEdit, QDateEdit, QCalendarWidget, QTextEdit, QTextBrowser, \
        QTableWidget, QInputDialog, QMessageBox, QFontDialog, QColorDialog, QFrame, QFileDialog, QStackedWidget
from PyQt6.QtGui import QIcon, QPixmap, QFont, QColor
import urllib.request
import json
import requests
from pathlib import Path
import info
# import font_info

class help_tab6(QWidget):
    def __init__(self):
        super().__init__()
        # layout = QVBoxLayout()
        # layout.addWidget(QLabel('This is Tab 6'))
        # self.setLayout(layout)
        self.stack = QStackedWidget(self)
        self.help_main_window = Help_Main(self.stack)
        self.help_manual_window = Help_Manual(self.stack)
        self.help_version_window = Help_Software_Version(self.stack)

        self.stack.addWidget(self.help_main_window)
        self.stack.addWidget(self.help_manual_window)
        self.stack.addWidget(self.help_version_window)

        layout = QVBoxLayout()
        layout.addWidget(self.stack)
        self.setLayout(layout)

############################## Help Main Page ##############################
class Help_Main(QWidget):
    def __init__(self, stack):
        super().__init__()
        self.stack = stack
        layout = QVBoxLayout()

        manual_button = QPushButton('Go to Manual')
        manual_button.clicked.connect(self.gotoHelpManual)
        
        version_button = QPushButton('Go to Version Page')
        version_button.clicked.connect(self.gotoHelpVersion)
        
        layout.addStretch(1)
        layout.addWidget(manual_button)
        layout.addStretch(1)
        layout.addWidget(version_button)
        layout.addStretch(1)

        self.setLayout(layout)


    def gotoHelpManual(self):
        self.stack.setCurrentIndex(1)

    def gotoHelpVersion(self):
        self.stack.setCurrentIndex(2)
    
############################## Manual Page ##############################
class Help_Manual(QWidget):
    def __init__(self, stack):
        super().__init__()
        self.stack = stack
        layout = QVBoxLayout()
        label1 = QLabel('메뉴얼 창입니다.')
        # temp_font = QFont()
        # temp_font.setPointSize(3)
        # label1.setFont(temp_font)
        label2 = QLabel('Kwak & Kim\'s co lab. App 입니다. 관계자들만 사용해주세요.')
        label3 = QLabel('상위 6개 탭은 ctrl + n (ex ctrl + 1 -> Paper Research)로 간편하게 이동 가능합니다.')
        label4 = QLabel('관리자가 원할 때, S/W 버젼이 업데이트 됩니다.')
        label5 = QLabel('Help 탭에서 Go to Version Page로 들어가서 \nGet New Kist S/W APP을 눌러서 새로운 앱을 다운 받을 수 있습니다.')
        label6 = QLabel('추가적인 기능이 필요한 경우 카톡 : rladh로 문의 바랍니다!')

        layout.addStretch(1)
        layout.addWidget(label1)
        layout.addWidget(label2)
        layout.addStretch(1)
        layout.addWidget(label3)
        layout.addStretch(1)
        layout.addWidget(label4)
        layout.addWidget(label5)
        layout.addStretch(2)
        layout.addWidget(label6)
        layout.addStretch(1)
        # layout.addWidget(label1)

        back_button = QPushButton('Go Back')
        back_button.clicked.connect(self.gotoHelpMain)
        layout.addWidget(back_button)
        self.setLayout(layout)

    def gotoHelpMain(self):
        self.stack.setCurrentIndex(0)

############################## S/W Version Page ##############################
class Help_Software_Version(QWidget):
    def __init__(self, stack):
        super().__init__()
        self.stack = stack
        layout = QVBoxLayout()
        label = QLabel(f'Current Version : {info.current_version}\n\n\nThis Version Publish Date : {info.current_version_updated_date}')



        download_button = QPushButton('Get New Kist S/W APP')
        download_button.setFixedSize(self.size().width() // 2, download_button.sizeHint().height())
        self.resizeEvent = lambda event: download_button.setFixedSize(self.size().width() // 2, download_button.sizeHint().height())
        download_button.clicked.connect(self.download_file)

        back_button = QPushButton('Go Back')
        back_button.clicked.connect(self.gotoHelpMain)

        layout.addStretch(3)
        layout.addWidget(label)
        layout.addStretch(1)
        layout.addWidget(download_button, alignment = Qt.AlignmentFlag.AlignCenter)
        layout.addStretch(3)
        layout.addWidget(back_button)

        self.setLayout(layout)

    def gotoHelpMain(self):
        self.stack.setCurrentIndex(0)

    def download_file(self):
        url = 'https://github.com/kimvjgd/kist_pyqt_app_2/raw/main/main.exe'
        save_path, _ = QFileDialog.getSaveFileName(self, 'Save File', '', 'Executable Files (*.exe)')
        
        if save_path:
            try:
                response = requests.get(url, stream=True)
                response.raise_for_status()  # Check for request errors
                
                with open(save_path, 'wb') as file:
                    for chunk in response.iter_content(chunk_size=8192):
                        file.write(chunk)
                
                QMessageBox.information(self, 'Success', 'File downloaded successfully!', QMessageBox.StandardButton.Ok)
            except Exception as e:
                QMessageBox.critical(self, 'Error', f'Failed to download file\n\n 동현이에게 문의하세요!', QMessageBox.StandardButton.Ok)



import sys
from PyQt6.QtCore import Qt, QBasicTimer, QTime, QDate, QDateTime, QCoreApplication
from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QMenu, QCheckBox, QLabel, QPushButton, QToolTip, \
    QHBoxLayout, QVBoxLayout, QRadioButton, QLineEdit, QComboBox, QProgressBar, QSlider, QDial, QSplitter, QGroupBox, \
        QSpinBox, QDoubleSpinBox, QTabWidget, QTimeEdit, QDateTimeEdit, QDateEdit, QCalendarWidget, QTextEdit, QTextBrowser, \
        QTableWidget, QInputDialog, QMessageBox, QFontDialog, QColorDialog, QFrame, QFileDialog
from PyQt6.QtGui import QIcon, QPixmap, QFont, QColor
import urllib.request
import json
import requests
from pathlib import Path

# class translator_tab2(QWidget):
#     def __init__(self):
#         super().__init__()
#         layout = QVBoxLayout()
#         layout.addWidget(QLabel('This is Tab 2'))
#         self.setLayout(layout)

class translator_tab2(QWidget):
    def __init__(self):
        super().__init__()
        self.src_lang = 'ko'
        self.dest_lang = 'en'

        self.initUI()
    
    def initUI(self):
        self.label1 = QLabel('한국어', self)
        self.label2 = QLabel('영어', self)
        
        self.edit1 = QTextEdit(self)
        self.edit2 = QTextEdit(self)
        
        self.transBtn = QPushButton('번역하기', self)
        self.changeBtn = QPushButton('언어 바꾸기', self)

        vbox1 = QVBoxLayout()
        vbox2 = QVBoxLayout()
        vbox1.addWidget(self.label1, alignment=Qt.AlignmentFlag.AlignCenter)
        vbox1.addWidget(self.edit1)
        vbox2.addWidget(self.label2, alignment=Qt.AlignmentFlag.AlignCenter)
        vbox2.addWidget(self.edit2)

        hbox = QHBoxLayout()
        hbox.addLayout(vbox1)
        hbox.addLayout(vbox2)

        layout = QVBoxLayout()
        layout.addLayout(hbox)
        layout.addWidget(self.transBtn)
        layout.addWidget(self.changeBtn)

        self.setLayout(layout)

        self.transBtn.clicked.connect(self.translate)
        self.changeBtn.clicked.connect(self.changeLanguage)
        
        self.setWindowTitle('구글번역 프로그램(Google Translator Program)')
        # self.setGeometry(200, 200, 400, 400)
        # self.show()
    
    def translate(self):
        text = self.edit1.toPlainText()
        if not text:
            return

        url = "https://translate.googleapis.com/translate_a/single"
        params = {
            "client": "gtx",
            "sl": self.src_lang,
            "tl": self.dest_lang,
            "dt": "t",
            "q": text,
        }

        response = requests.get(url, params=params, verify=False)
        if response.status_code == 200:
            result = response.json()
            translated_text = result[0][0][0]
            self.edit2.setText(translated_text)
        else:
            self.edit2.setText("번역 실패")

    def changeLanguage(self):
        if self.label1.text() == '한국어':
            self.label1.setText('영어')
            self.label2.setText('한국어')
            self.src_lang, self.dest_lang = self.dest_lang, self.src_lang
        else:
            self.label1.setText('한국어')
            self.label2.setText('영어')
            self.src_lang, self.dest_lang = self.dest_lang, self.src_lang

        t1, t2 = self.edit1.toPlainText(), self.edit2.toPlainText()
        self.edit1.setText(t2)
        self.edit2.setText(t1)
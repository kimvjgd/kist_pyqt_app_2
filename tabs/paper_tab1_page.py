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

class paper_tab1(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        layout.addWidget(QLabel('진행 중입니다.\n\n보안 & 저널마다 포맷이 달라서.... 꽤나 걸릴 것 같은데\n\n흠... 노력중..!'))
        self.setLayout(layout)
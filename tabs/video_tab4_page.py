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
from moviepy.editor import VideoFileClip

class video_tab4(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'MOV to MP4 Converter'
        self.left = 100
        self.top = 100
        self.width = 400
        self.height = 200
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.file_loaded = False

        layout = QVBoxLayout()
        
        # Button to load MOV file
        self.button_load = QPushButton('Load MOV File', self)
        self.button_load.clicked.connect(self.load_file)
        
        # Label to show the selected file path
        self.label_file = QLabel('Select a MOV file to convert', self)
        self.label_file.setStyleSheet("font-size: 24px;")
        
        # Button to save MP4 file
        self.button_save = QPushButton('Convert and Save MP4 File', self)
        self.button_save.clicked.connect(self.save_file)



        layout.addWidget(self.label_file)
        layout.addWidget(self.button_load)
        layout.addWidget(self.button_save)
        
        self.setLayout(layout)
        self.show()

    def load_file(self):
        self.mov_file_path, _ = QFileDialog.getOpenFileName(self, "Select a MOV file", "", "MOV Files (*.mov)")
        
        if self.mov_file_path:
            self.file_loaded = True
            self.label_file.setText(f'Selected file: {self.mov_file_path}')

    def save_file(self):
        if self.mov_file_path:
            self.output_mp4_file_path, _ = QFileDialog.getSaveFileName(self, "Save as MP4", "", "MP4 Files (*.mp4)")
            if self.output_mp4_file_path:
                self.convert_avi_to_mp4(self.mov_file_path, self.output_mp4_file_path)
                self.label_file.setText(f'File converted and saved to: {self.output_mp4_file_path}')
        else:
            self.label_file.setText('No MOV file selected!')

    def convert_avi_to_mp4(self, mov_file_path, output_mp4_file_path):
        # MOV 파일 로드
        clip = VideoFileClip(mov_file_path)
        # MP4로 변환하여 저장
        clip.write_videofile(output_mp4_file_path, codec='libx264')
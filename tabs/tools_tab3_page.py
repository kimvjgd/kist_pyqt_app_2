# import sys
# from PyQt5.QtCore import Qt, QBasicTimer, QTime, QDate, QDateTime, QCoreApplication
# from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QMenu, QCheckBox, QLabel, QPushButton, QToolTip, \
#     QHBoxLayout, QVBoxLayout, QRadioButton, QLineEdit, QComboBox, QProgressBar, QSlider, QDial, QSplitter, QGroupBox, \
#         QSpinBox, QDoubleSpinBox, QTabWidget, QTimeEdit, QDateTimeEdit, QDateEdit, QCalendarWidget, QTextEdit, QTextBrowser, \
#         QTableWidget, QInputDialog, QMessageBox, QFontDialog, QColorDialog, QFrame, QFileDialog
# from PyQt5.QtGui import QIcon, QPixmap, QFont, QColor
# import urllib.request
# import json
# import requests
# from pathlib import Path

# class tools_tab3(QWidget):
#     def __init__(self):
#         super().__init__()
#         layout = QVBoxLayout()
#         layout.addWidget(QLabel('This is Tab 3'))
#         self.setLayout(layout)
import sys
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QColor, QGuiApplication, QPixmap, QScreen, QCursor
from PyQt6.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget, QToolTip

class tools_tab3(QWidget):
    def __init__(self):
        super().__init__()
        self.label = QLabel('Move the mouse to pick color (inside or outside window)\n', self)
        self.label.setStyleSheet("font-size: 20px;")
        self.current_color_label = QLabel(f'current color : {None}')
        self.current_color_label.setStyleSheet("font-size: 24px;")
        self.color_display = QLabel(self)
        self.color_display.setFixedSize(400, 200)
        self.layout = QVBoxLayout()
        self.layout.addStretch(1)
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.current_color_label)
        self.layout.addStretch(1)
        self.layout.addWidget(self.color_display)
        self.layout.addStretch(1)

        self.setLayout(self.layout)

        self.setMouseTracking(True)
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_color)
        self.timer.start(100)  # Update every 100 ms

    def update_color(self):
        screen = QGuiApplication.primaryScreen()
        pos = QCursor.pos()
        pixmap = screen.grabWindow(0, pos.x(), pos.y(), 1, 1)
        if not pixmap.isNull():
            image = pixmap.toImage()
            color = QColor(image.pixel(0, 0))
            self.color_display.setStyleSheet(f'background-color: {color.name()};')
            self.current_color_label.setText(f'current color : {color.name()}')

            # QToolTip.showText(pos, f'Color: {color.name()}')

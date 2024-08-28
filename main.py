from PyQt6.QtCore import Qt
from PyQt6.QtGui import QShortcut, QKeySequence
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QTabWidget
import tabs.paper_tab1_page as page1
import tabs.translator_tab2_page as page2
import tabs.tools_tab3_page as page3
import tabs.video_tab4_page as page4
import tabs.kibab_tab5 as page5
import tabs.help_tab6_page as page6
import tabs.osmosis_tab7_page as page7
from qt_material import apply_stylesheet
import sys

class KistApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('KIST Kwak&Kim Lab')
        self.setGeometry(300, 300, 800, 500)
        apply_stylesheet(app, theme='dark_teal.xml')
        self.uiInit()
        self.createShortcuts()
    
    def uiInit(self):
        self.paper_tab1 = page1.paper_tab1()
        self.translator_tab2 = page2.translator_tab2()
        self.tools_tab3 = page3.tools_tab3()
        self.video_tab4 = page4.video_tab4()
        self.kibab_tab5 = page5.kibab_tab5()
        self.help_tab6 = page6.help_tab6()
        self.osmosis_tab7 = page7.osmosis_tab6()

        self.tabs = QTabWidget()
        self.tabs.addTab(self.paper_tab1, '논문 검색')
        self.tabs.addTab(self.translator_tab2, '번역기')
        self.tabs.addTab(self.tools_tab3, '기타 툴')
        self.tabs.addTab(self.video_tab4, '비디오 변환')
        self.tabs.addTab(self.kibab_tab5, '오늘의 키밥')
        self.tabs.addTab(self.help_tab6, 'Help')
        self.tabs.addTab(self.osmosis_tab7, 'Osmosis_Exp')
        self.tabs.setTabPosition(QTabWidget.TabPosition.North)
        self.tabs.setTabShape(QTabWidget.TabShape.Rounded)

        vbox = QVBoxLayout()
        vbox.addWidget(self.tabs)
        
        self.setLayout(vbox)
        
    def createShortcuts(self):
        # Create shortcuts using QKeySequence
        self.shortcut1 = QShortcut(QKeySequence(Qt.KeyboardModifier.ControlModifier | Qt.Key.Key_1), self)
        self.shortcut1.activated.connect(lambda: self.tabs.setCurrentIndex(0))
        self.shortcut2 = QShortcut(QKeySequence(Qt.KeyboardModifier.ControlModifier | Qt.Key.Key_2), self)
        self.shortcut2.activated.connect(lambda: self.tabs.setCurrentIndex(1))
        self.shortcut3 = QShortcut(QKeySequence(Qt.KeyboardModifier.ControlModifier | Qt.Key.Key_3), self)
        self.shortcut3.activated.connect(lambda: self.tabs.setCurrentIndex(2))
        self.shortcut4 = QShortcut(QKeySequence(Qt.KeyboardModifier.ControlModifier | Qt.Key.Key_4), self)
        self.shortcut4.activated.connect(lambda: self.tabs.setCurrentIndex(3))
        self.shortcut5 = QShortcut(QKeySequence(Qt.KeyboardModifier.ControlModifier | Qt.Key.Key_5), self)
        self.shortcut5.activated.connect(lambda: self.tabs.setCurrentIndex(4))
        self.shortcut6 = QShortcut(QKeySequence(Qt.KeyboardModifier.ControlModifier | Qt.Key.Key_6), self)
        self.shortcut6.activated.connect(lambda: self.tabs.setCurrentIndex(5))
        self.shortcut6 = QShortcut(QKeySequence(Qt.KeyboardModifier.ControlModifier | Qt.Key.Key_7), self)
        self.shortcut6.activated.connect(lambda: self.tabs.setCurrentIndex(6))


app = QApplication(sys.argv)
exec = KistApp()
exec.show()
app.exec()

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QLineEdit
from PyQt6.QtCore import Qt

class osmosis_tab6(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # Main layout
        main_layout = QVBoxLayout()

        # Top button layout
        top_button_layout = QHBoxLayout()
        self.nulnuli_button = QPushButton('널널이 계산')
        self.kkobuli_button = QPushButton('꼬불이 계산')
        top_button_layout.addWidget(self.nulnuli_button)
        top_button_layout.addWidget(self.kkobuli_button)
        main_layout.addLayout(top_button_layout)

        # Bottom layout (split into left and right)
        bottom_layout = QHBoxLayout()

        # Nulnuli layout (left)
        nulnuli_layout = QVBoxLayout()

        # Adding the 7 rows for Nulnuli
        nulnuli_layout.addLayout(self.create_row_layout('loop', 'textedit'))
        nulnuli_layout.addLayout(self.create_row_layout('1_part', 'textedit'))
        nulnuli_layout.addLayout(self.create_row_layout('2_part', 'textedit'))
        nulnuli_layout.addLayout(self.create_row_layout('3_part', 'textedit'))
        nulnuli_layout.addLayout(self.create_row_layout('현재압력', 'text'))
        nulnuli_layout.addLayout(self.create_row_layout('del(V)', 'text'))
        nulnuli_layout.addLayout(self.create_row_layout('V_air', 'text'))

        # Kkobuli layout (right)
        kkobuli_layout = QVBoxLayout()

        # Adding the 7 rows for Kkobuli
        kkobuli_layout.addLayout(self.create_row_layout('loop', 'textedit'))
        kkobuli_layout.addLayout(self.create_row_layout('1_part', 'textedit'))
        kkobuli_layout.addLayout(self.create_row_layout('2_part', 'textedit'))
        kkobuli_layout.addLayout(self.create_row_layout('3_part', 'textedit'))
        kkobuli_layout.addLayout(self.create_row_layout('현재압력', 'text'))
        kkobuli_layout.addLayout(self.create_row_layout('del(V)', 'text'))
        kkobuli_layout.addLayout(self.create_row_layout('V_air', 'text'))

        # Add Nulnuli and Kkobuli layouts to the bottom layout
        bottom_layout.addLayout(nulnuli_layout)
        bottom_layout.addLayout(kkobuli_layout)

        # Add bottom layout to the main layout
        main_layout.addLayout(bottom_layout)

        # Set the layout for the main window
        self.setLayout(main_layout)
        self.setWindowTitle('My PyQt6 App')
        self.show()

    def create_row_layout(self, label_text, widget_type):
        """Helper function to create a row layout with a label and either a QLineEdit or QLabel."""
        row_layout = QHBoxLayout()
        row_layout.setContentsMargins(0, 0, 0, 0)  # Remove margins for precise alignment
        row_layout.setSpacing(10)  # Adjust spacing between label and textedit

        label = QLabel(label_text)
        label.setFixedWidth(80)  # Set a fixed width for labels to align them
        widget = QLineEdit() if widget_type == 'textedit' else QLabel('')

        row_layout.addWidget(label)
        row_layout.addWidget(widget)

        return row_layout

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec())

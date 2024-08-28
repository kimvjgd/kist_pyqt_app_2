import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QLineEdit, QFrame
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt

class osmosis_tab6(QWidget):
    def __init__(self):
        # nulnuli
        # kkobuli
        self.nullnuli_path1_dimension = 0.192684
        self.nullnuli_path2_dimension = 0.442
        self.nullnuli_path3_dimension = 0.180118
        self.nullnuli_loop_dimension = 1.256802
        self.nullnuli_overall_dimension = 40.12762
        
        self.kkobuli_path1_dimension = 0.046862
        self.kkobuli_path2_dimension = 0.261
        self.kkobuli_path3_dimension = 0.045029
        self.kkobuli_loop_dimension = 0.613892
        self.kkobuli_overall_dimension = 30.67206
        super().__init__()

        self.initUI()

    def initUI(self):
        # Main layout
        main_layout = QVBoxLayout()

        # Add image to the layout
        image_label = QLabel(self)
        pixmap = QPixmap("osmosis_sample.png")
        pixmap = pixmap.scaled(800, 450, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)

        image_label.setPixmap(pixmap)
        image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(image_label)

        # Adding spacing at the top of the layout
        main_layout.addSpacing(20)  # Add 20 pixels of space below the image

        # Top button layout
        top_button_layout = QHBoxLayout()
        self.nulnuli_button = QPushButton('널널이 계산')
        self.kkobuli_button = QPushButton('꼬불이 계산')
        top_button_layout.addWidget(self.nulnuli_button)
        top_button_layout.addWidget(self.kkobuli_button)
        main_layout.addLayout(top_button_layout)

        # Adding spacing between the top buttons and the bottom widgets
        main_layout.addSpacing(20)  # Add 20 pixels of space

        # Bottom layout (split into left and right)
        bottom_layout = QHBoxLayout()

        # Nulnuli layout (left)
        nulnuli_layout = QVBoxLayout()

        # Adding the 7 rows for Nulnuli
        self.nulnuli_loop_edit = QLineEdit()
        self.nulnuli_loop_edit.setStyleSheet("color: white;")  # Set text color to white
        nulnuli_layout.addLayout(self.create_row_layout('loop', 'textedit', self.nulnuli_loop_edit))
        
        self.nulnuli_1_part_edit = QLineEdit()
        self.nulnuli_1_part_edit.setStyleSheet("color: white;")  # Set text color to white
        nulnuli_layout.addLayout(self.create_row_layout('1_part', 'textedit', self.nulnuli_1_part_edit))
        
        self.nulnuli_2_part_edit = QLineEdit()
        self.nulnuli_2_part_edit.setStyleSheet("color: white;")  # Set text color to white
        nulnuli_layout.addLayout(self.create_row_layout('2_part', 'textedit', self.nulnuli_2_part_edit))
        
        self.nulnuli_3_part_edit = QLineEdit()
        self.nulnuli_3_part_edit.setStyleSheet("color: white;")  # Set text color to white
        nulnuli_layout.addLayout(self.create_row_layout('3_part', 'textedit', self.nulnuli_3_part_edit))
        
        self.nulnuli_pressure_label = QLabel('')  # Label to show current pressure
        nulnuli_layout.addLayout(self.create_row_layout('현재압력', 'text', widget=self.nulnuli_pressure_label, spacing=2))
        
        self.nulnuli_del_v_label = QLabel('')  # Label to show del(V)
        nulnuli_layout.addLayout(self.create_row_layout('del(V)', 'text', widget=self.nulnuli_del_v_label, spacing=2))
        
        self.nullnuli_v_air_label = QLabel('')  # Label to show V_air
        nulnuli_layout.addLayout(self.create_row_layout('V_air', 'text', widget=self.nullnuli_v_air_label, spacing=2))

        # Split line between Nulnuli and Kkobuli
        split_line = QFrame()
        split_line.setFrameShape(QFrame.Shape.VLine)
        split_line.setFrameShadow(QFrame.Shadow.Sunken)

        # Kkobuli layout (right)
        kkobuli_layout = QVBoxLayout()

        # Adding the 7 rows for Kkobuli
        self.kkobuli_loop_edit = QLineEdit()
        self.kkobuli_loop_edit.setStyleSheet("color: white;")  # Set text color to white
        kkobuli_layout.addLayout(self.create_row_layout('loop', 'textedit', self.kkobuli_loop_edit))
        
        self.kkobuli_1_part_edit = QLineEdit()
        self.kkobuli_1_part_edit.setStyleSheet("color: white;")  # Set text color to white
        kkobuli_layout.addLayout(self.create_row_layout('1_part', 'textedit', self.kkobuli_1_part_edit))
        
        self.kkobuli_2_part_edit = QLineEdit()
        self.kkobuli_2_part_edit.setStyleSheet("color: white;")  # Set text color to white
        kkobuli_layout.addLayout(self.create_row_layout('2_part', 'textedit', self.kkobuli_2_part_edit))
        
        self.kkobuli_3_part_edit = QLineEdit()
        self.kkobuli_3_part_edit.setStyleSheet("color: white;")  # Set text color to white
        kkobuli_layout.addLayout(self.create_row_layout('3_part', 'textedit', self.kkobuli_3_part_edit))
        
        self.kkobuli_pressure_label = QLabel('')  # Label to show current pressure
        kkobuli_layout.addLayout(self.create_row_layout('현재압력', 'text', widget=self.kkobuli_pressure_label, spacing=2))
        
        self.kkobuli_del_v_label = QLabel('')  # Label to show del(V)
        kkobuli_layout.addLayout(self.create_row_layout('del(V)', 'text', widget=self.kkobuli_del_v_label, spacing=2))
        
        self.kkobuli_v_air_label = QLabel('')  # Label to show V_air
        kkobuli_layout.addLayout(self.create_row_layout('V_air', 'text', widget=self.kkobuli_v_air_label, spacing=2))

        # Add Nulnuli and Kkobuli layouts to the bottom layout with the split line in between
        bottom_layout.addLayout(nulnuli_layout)
        bottom_layout.addWidget(split_line)  # Add the split line between the two layouts
        bottom_layout.addLayout(kkobuli_layout)

        # Add bottom layout to the main layout
        main_layout.addLayout(bottom_layout)

        # Connect button clicks to their respective functions
        self.nulnuli_button.clicked.connect(self.calculate_nulnuli_values)
        self.kkobuli_button.clicked.connect(self.calculate_kkobuli_values)

        # Set the layout for the main window
        self.setLayout(main_layout)
        self.setWindowTitle('My PyQt6 App')
        self.show()

    def create_row_layout(self, label_text, widget_type, widget=None, spacing=10):
        """Helper function to create a row layout with a label and either a QLineEdit or QLabel."""
        row_layout = QHBoxLayout()
        row_layout.setContentsMargins(0, 0, 0, 0)  # Remove margins for precise alignment
        row_layout.setSpacing(spacing)  # Adjust spacing between label and textedit

        label = QLabel(label_text)
        label.setFixedWidth(80)  # Set a fixed width for labels to align them

        if widget is None:
            widget = QLineEdit() if widget_type == 'textedit' else QLabel('')

        row_layout.addWidget(label)
        row_layout.addWidget(widget)

        return row_layout

    def calculate_nulnuli_values(self):
        """Calculate and display the current pressure and del(V) for Nulnuli."""
        # Calculate and set the current pressure
        loop_value = float(self.nulnuli_loop_edit.text())

        # Calculate and set del(V) = 1_part + 2_part + 3_part
        try:
            part1 = float(self.nulnuli_1_part_edit.text())
            part2 = float(self.nulnuli_2_part_edit.text())
            part3 = float(self.nulnuli_3_part_edit.text())
            del_v = self.nullnuli_loop_dimension * loop_value + part1 * self.nullnuli_path1_dimension + part2 * self.nullnuli_path2_dimension + part3 * self.nullnuli_path3_dimension
            v_air = self.nullnuli_overall_dimension - del_v
            current_pressure = 101325 * self.nullnuli_overall_dimension / v_air
            self.nulnuli_del_v_label.setText(f"{del_v}")
            self.nullnuli_v_air_label.setText(f"{v_air}")
            self.nulnuli_pressure_label.setText(f"{current_pressure}")
        except ValueError:
            self.nulnuli_del_v_label.setText("Invalid input")

    def calculate_kkobuli_values(self):
        """Calculate and display the current pressure and del(V) for Kkobuli."""
        # Calculate and set the current pressure
        loop_value = float(self.kkobuli_loop_edit.text())

        # Calculate and set del(V) = 1_part + 2_part + 3_part
        try:
            part1 = float(self.kkobuli_1_part_edit.text())
            part2 = float(self.kkobuli_2_part_edit.text())
            part3 = float(self.kkobuli_3_part_edit.text())
            del_v = self.kkobuli_loop_dimension * loop_value + part1 * self.kkobuli_path1_dimension + part2 * self.kkobuli_path2_dimension + part3 * self.kkobuli_path3_dimension
            v_air = self.kkobuli_overall_dimension - del_v
            current_pressure = 101325 * self.kkobuli_overall_dimension / v_air
            self.kkobuli_del_v_label.setText(f"{del_v}")
            self.kkobuli_v_air_label.setText(f"{v_air}")
            self.kkobuli_pressure_label.setText(f"{current_pressure}")
        except ValueError:
            self.kkobuli_del_v_label.setText("Invalid input")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = osmosis_tab6()
    ex.show()
    sys.exit(app.exec())

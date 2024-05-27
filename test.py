import sys
import requests
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QFileDialog, QLabel, QMessageBox
from PyQt6.QtCore import Qt

class DownloaderApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle('GitHub File Downloader')
        self.setGeometry(300, 300, 400, 200)
        
        layout = QVBoxLayout()
        
        self.infoLabel = QLabel('Click the button to download main.exe from GitHub', self)
        layout.addWidget(self.infoLabel)
        
        self.downloadButton = QPushButton('Download main.exe', self)
        self.downloadButton.clicked.connect(self.download_file)
        layout.addWidget(self.downloadButton)
        
        self.setLayout(layout)
    
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
                QMessageBox.critical(self, 'Error', f'Failed to download file: {e}', QMessageBox.StandardButton.Ok)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    downloader = DownloaderApp()
    downloader.show()
    sys.exit(app.exec())

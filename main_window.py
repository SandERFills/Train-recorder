from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QLabel, QVBoxLayout,QHBoxLayout, QMainWindow
from PyQt5.QtWidgets import QWidget
import PyQt5.QtCore
from os import path
from sys import argv
from button_panel import Button_panel
from main import VideoDisplayWidget
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Захват видео")
        self.setMinimumSize(1280,720)
        self.setStyleSheet("background-color: white;")

        home_dir=path.dirname(path.abspath(argv[0]))
        self.video_dir=path.join(home_dir,"Video")
        self._init_ui()
    def _init_ui(self):
        cental_widget=QWidget()
        self.setCentralWidget(cental_widget)
        main_layout = QHBoxLayout(cental_widget)
        main_layout.setContentsMargins(10,10,10,10)
        main_layout.setSpacing(15)

        center_widget = QWidget()
        center_layout = QVBoxLayout(center_widget)
        center_layout.setContentsMargins(0, 0, 0, 0)
        center_layout.setSpacing(10)
        self.video_widget=VideoDisplayWidget()
        center_layout.addWidget(self.video_widget,1)

        self.info_label = QLabel("Источник не выбран")
        self.info_label.setFont(QFont('Arial',9))
        self.info_label.setStyleSheet("color: #666")
        center_layout.addWidget(self.info_label)
        main_layout.addWidget(center_widget,1)
        button_frame=Button_panel()
        center_layout.addWidget(button_frame)

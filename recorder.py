import sys
import os
import datetime
import cv2
from main_window import MainWindow
from dataclasses import dataclass
from typing import Optional, List
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                             QHBoxLayout, QPushButton, QFrame, QSizePolicy,
                             QFileDialog, QLabel, QSlider, QDialog, QListWidget,
                             QListWidgetItem, QTabWidget, QMenuBar, QAction,
                             QStatusBar, QMessageBox, QProgressBar, QAbstractItemView,
                             QStyle, QStyleOptionSlider)
from PyQt5.QtCore import Qt, QTimer, QThread, pyqtSignal, QObject, QRect
from PyQt5.QtGui import QFont, QColor, QImage, QPixmap, QPainter, QPen


def main():
    app=QApplication(sys.argv)


    window=MainWindow()
    window.show()

    app.exec()

if __name__=='__main__':
    main()

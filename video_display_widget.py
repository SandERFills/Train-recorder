from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QSizePolicy, QWidget
import cv2
from PyQt5.QtGui import QPainter

class VideoDisplayWidget(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
        self.setMinimumSize(320,180)
        self.setStyleSheet("background-color: black;")
        self._pixmap = None
    def set_frame(self,frame):
        if frame is None:
            return
        rgb=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        h,w,ch=rgb.shape
        print("DEBUG h,w,ch:",h,w,ch,"/n")
        bytes_per_line=ch*w
        qimg=QImage(rgb.data,w,h,bytes_per_line,QImage.Format_RGB888)
        self._pixmap=QPixmap.fromImage(qimg)
        self.update()

    def paintEvent(self,event):
        if self._pixmap is None:
            return
        scaled=self._pixmap.scaled(
            self.size(),Qt.KeepAspectRatio, Qt.SmoothTransformation
        )
        x = (self.width() - scaled.width()) // 2
        y = (self.height() - scaled.height()) // 2
        painter = QPainter(self)
        painter.drawPixmap(x, y, scaled)
        painter.end()

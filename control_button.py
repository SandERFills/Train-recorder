from PyQt5.QtCore import QSize
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QPushButton, QSizePolicy


class Control_button(QPushButton):
    def __init__(self,text, parent=None, color=None):
        super().__init__(text,parent)
        self.setFont(QFont('Arial', 10, QFont.Bold))
        self.setMinimumHeight(45)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self._base_color = color
        self._update_style()
    def set_color(self, color):
        self._base_color = color
        self._update_style()

    def _update_style(self):
        if self._base_color:
            self.setStyleSheet(f"""
                QPushButton {{
                    background-color: {self._base_color};
                    color: white;
                    border: none;
                    border-radius: 4px;
                    padding: 8px 12px;
                    font-weight: bold;
                }}
                QPushButton:hover {{
                    background-color: {self._darken_color(self._base_color)};
                }}
                QPushButton:pressed {{
                    background-color: {self._darken_color(self._base_color, 30)};
                }}
                QPushButton:disabled {{
                    background-color: #d0d0d0;
                    color: #888;
                }}
            """)
        else:
            self.setStyleSheet("""
                QPushButton {
                    background-color: white;
                    border: 1px solid #333;
                    border-radius: 4px;
                    padding: 8px 12px;
                    font-weight: bold;
                }
                QPushButton:hover { background-color: #f0f0f0; }
                QPushButton:pressed { background-color: #e0e0e0; }
                QPushButton:disabled {
                    background-color: #d0d0d0;
                    color: #888;
                }
            """)

from PyQt5.QtWidgets import QFrame, QHBoxLayout
from control_button import Control_button

class Button_panel(QFrame):
    def __init__(self):
        super().__init__()
        self.setFrameStyle(QFrame.StyledPanel | QFrame.Raised)
        self.setStyleSheet(
            """
            QFrame {
                background-color: #f9f9f9;
                border: 1px solid #ddd;
                border-radius: 5px;
                padding: 10px;
            }
            """
        )
        self.button_layout=QHBoxLayout(self)
        self.button_layout.setContentsMargins(10, 10, 10, 10)
        self.button_layout.setSpacing(8)

        self.btn_play = Control_button("Играть")
        self.btn_play.setMinimumWidth(90)
        self.btn_play.setMaximumWidth(110)
        # self.btn_play.clicked.connect(self.play_video)
        self.button_layout.addWidget(self.btn_play)

        self.btn_play = Control_button("Стоп")
        self.btn_play.setMinimumWidth(90)
        self.btn_play.setMaximumWidth(110)
        # self.btn_play.clicked.connect(self.play_video)
        self.button_layout.addWidget(self.btn_play)

        self.btn_play = Control_button("Играть назад")
        self.btn_play.setMinimumWidth(90)
        self.btn_play.setMaximumWidth(110)
        # self.btn_play.clicked.connect(self.play_video)
        self.button_layout.addWidget(self.btn_play)

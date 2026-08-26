from PySide6.QtCore import QSize
from PySide6.QtGui import Qt
from PySide6.QtWidgets import QVBoxLayout, QWidget


class Content(QWidget):
    def __init__(self):
        super().__init__()

        self._layout = QVBoxLayout()

        self.setLayout(self._layout)
        self.setObjectName("content")
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        self.setFixedSize(QSize(800, 800 - 58))

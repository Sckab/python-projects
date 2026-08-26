from PySide6.QtGui import Qt
from PySide6.QtWidgets import QHBoxLayout, QLabel, QWidget


class Header(QWidget):
    def __init__(self):
        super().__init__()

        self._layout = QHBoxLayout()

        self._label = QLabel("NOTES")

        font = self._label.font()
        font.setPointSize(32)
        font.setBold(True)

        self._label.setFont(font)
        self._label.setObjectName("title")

        self._layout.addWidget(self._label)

        self.setLayout(self._layout)
        self.setObjectName("header")
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)

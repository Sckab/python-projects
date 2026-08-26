from PySide6.QtCore import QSize
from PySide6.QtGui import QFont, Qt
from PySide6.QtWidgets import QHBoxLayout, QLabel, QSizePolicy, QSpacerItem, QWidget

from notes.gui.custom_widgets.HeaderButton import HeaderButton


class Header(QWidget):
    def __init__(self):
        super().__init__()

        self._layout = QHBoxLayout()
        self._layout.setContentsMargins(12, 10, 12, 12)

        self._label = QLabel("NOTES")

        font = self._label.font()
        font.setPointSize(32)
        font.setFamily("Inter")
        font.setWeight(QFont.Weight(800))

        self._label.setFont(font)
        self._label.setObjectName("title")
        self._label.setAlignment(Qt.AlignmentFlag.AlignVCenter)

        self._add_btn = HeaderButton("add")
        self._remove_btn = HeaderButton("remove")
        self._delete_btn = HeaderButton("delete")

        self._layout.addWidget(self._label)
        self._layout.addItem(
            QSpacerItem(
                0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding
            )
        )
        self._layout.addWidget(self._delete_btn)
        self._layout.addWidget(self._remove_btn)
        self._layout.addWidget(self._add_btn)

        self.setLayout(self._layout)
        self.setObjectName("header")
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        self.setFixedSize(QSize(800, 58))

from PySide6.QtCore import QSize
from PySide6.QtGui import QColor, Qt
from PySide6.QtWidgets import QPushButton

from notes.gui.icons import MaterialIcon


class HeaderButton(QPushButton):
    def __init__(self, icon: str):
        super().__init__()

        self.setFlat(True)
        self.setObjectName("header_btn")
        self.setFixedSize(37, 37)
        self.setCursor(Qt.CursorShape.PointingHandCursor)

        dpr = self.devicePixelRatioF()
        pixmap = MaterialIcon(icon, size=40).pixmap(
            int(35 * dpr), color=QColor("#76946A")
        )
        pixmap.setDevicePixelRatio(dpr)

        self.setIcon(pixmap)
        self.setIconSize(QSize(35, 35))

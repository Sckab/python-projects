import os

from PySide6.QtCore import QSize
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget

from notes.gui.custom_widgets.Content import Content
from notes.gui.custom_widgets.Header import Header


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setFixedSize(QSize(800, 500))
        self.setWindowTitle("Note Taker")

        self.main_layout = QVBoxLayout()
        self.main_layout.setContentsMargins(0, 0, 0, 0)

        self.header = Header()
        self.content = Content()

        self.main_layout.addWidget(self.header)
        self.main_layout.addWidget(self.content)

        self.central = QWidget()
        self.central.setLayout(self.main_layout)

        self.setCentralWidget(self.central)


def run() -> int:
    script_dir = os.path.dirname(__file__)

    styles_dir = os.path.join(script_dir, "styles")

    app = QApplication([])

    with open(os.path.join(styles_dir, "style.qss"), "r") as f:
        app.setStyleSheet(f.read())

    window = MainWindow()
    window.show()

    return app.exec()

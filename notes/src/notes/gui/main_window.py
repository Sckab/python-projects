import os

from PySide6.QtWidgets import QApplication, QMainWindow

from notes.gui.ui.ui_main_window import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.counter = 0

        self.ui.label.setText(str(self.counter))
        self.ui.pushButton.clicked.connect(self.update_counter)

    def update_counter(self, e):
        self.counter += 1

        self.ui.label.setText(str(self.counter))


def run() -> int:
    script_dir = os.path.dirname(__file__)

    styles_dir = os.path.join(script_dir, "styles")

    app = QApplication([])

    with open(os.path.join(styles_dir, "style.qss"), "r") as f:
        app.setStyleSheet(f.read())

    window = MainWindow()
    window.show()

    return app.exec()

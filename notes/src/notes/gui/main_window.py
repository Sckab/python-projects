import os

from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine


def run() -> int:
    script_dir = os.path.dirname(__file__)

    app = QGuiApplication([])

    engine = QQmlApplicationEngine()
    engine.quit.connect(app.quit)
    engine.load(os.path.join(script_dir, "qml/main.qml"))

    return app.exec()

import QtQuick 2.15
import QtQuick.Controls 2.15

import "."

ApplicationWindow {
    id: appWin
    visible: true
    title: "Note Taker"

    minimumHeight: 500
    minimumWidth: 800

    color: Style.generalBackground

    Text {
        anchors.centerIn: parent
        text: "Hello World"
        font.pixelSize: 24
    }
}

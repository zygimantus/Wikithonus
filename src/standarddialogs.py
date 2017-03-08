#!/usr/bin/env python

import sys

from PyQt5.QtWidgets import (QApplication, QDialog,
                             QFrame, QGridLayout,
                             QInputDialog, QLabel, QPushButton)


class Dialog(QDialog):
    MESSAGE = "<p>Message boxes have a caption, a text, and up to three " \
              "buttons, each with standard or custom texts.</p>" \
              "<p>Click a button to close the message box. Pressing the Esc " \
              "button will activate the detected escape button (if any).</p>"

    def __init__(self, parent=None):
        super(Dialog, self).__init__(parent)

        frame_style = QFrame.Sunken | QFrame.Panel

        self.integerLabel = QLabel()
        self.integerLabel.setFrameStyle(frame_style)
        self.integerButton = QPushButton("QInputDialog.get&Int()")

        self.integerButton.clicked.connect(self.setInteger)

        layout = QGridLayout()
        layout.setColumnStretch(1, 1)
        layout.setColumnMinimumWidth(1, 250)
        layout.addWidget(self.integerButton, 0, 0)
        layout.addWidget(self.integerLabel, 0, 1)
        self.setLayout(layout)

        self.setWindowTitle("Standard Dialogs")

    def setInteger(self):
        i, ok = QInputDialog.getInt(self, "QInputDialog.getInt()",
                                    "Percentage:", 25, 0, 100, 1)
        if ok:
            self.integerLabel.setText("%d%%" % i)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = Dialog()
    dialog.show()
    sys.exit(app.exec_())

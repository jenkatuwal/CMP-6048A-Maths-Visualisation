from GUI.ui_interface import *


class TextInput(QLineEdit):
    def __init__(self):
        super(TextInput, self).__init__()
        self.setAlignment(Qt.AlignLeft)
        self.setStyleSheet("QLineEdit{border:2px solid;\n"
                           "border-color:rgb(214, 214, 214);\n"
                           "background-color: rgb(81, 85, 93);\n"
                           "color:rgb(214, 214, 214);}\n")

        self.setMinimumHeight(30)

        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 50, -25)

        self.setText("")

        self.setMaxLength(140)



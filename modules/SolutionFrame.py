from GUI.ui_interface import *


class SolutionFrame(QFrame):

    def __init__(self, text):
        super(SolutionFrame, self).__init__()
        # self.setAlignment(Qt.AlignLeft)
        self.setStyleSheet("QLineEdit{border:2px solid;\n"
                           "border-color:rgb(214, 214, 214);\n"
                           "background-color: rgb(255, 255, 255);\n"
                           "color:rgb(214, 214, 214);}\n"
                           "QFrame{background-color: rgb(255, 255, 255)}")

        self.layout = QVBoxLayout()
        self.setFixedSize(854, 100)

        self.text = text

        self.add_math_widget()

    def add_math_widget(self):
        from modules.symboltext import SymbolTextWidget
        self.math_widget = SymbolTextWidget(self.text, self)
        self.layout.addWidget(self.math_widget, alignment=Qt.AlignLeft)
        self.setLayout(self.layout)

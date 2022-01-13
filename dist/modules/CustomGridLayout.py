from GUI.ui_interface import *


class CustomGridLayout(QVBoxLayout):
    def __init__(self):
        super(CustomGridLayout, self).__init__()
        self.setAlignment(Qt.AlignTop)  # !!!
        self.setSpacing(10)

    def addWidget(self, widget, row, col):
        row_layout_vertical = self.count()

        if row < row_layout_vertical:
            pass
        else:
            while row >= row_layout_vertical:
                lyt = QHBoxLayout()
                lyt.setAlignment(Qt.AlignLeft)
                self.addLayout(lyt)
                row_layout_vertical = self.count()

        self.itemAt(row).insertWidget(col, widget)

    def insertRow(self, row):
        layout = QHBoxLayout()
        layout.setAlignment(Qt.AlignLeft)
        self.insertLayout(row, layout)

    def delete_row(self, row):
        for j in (range(self.itemAt(row).count())):
            self.itemAt(row).itemAt(j).widget().setParent(None)
        self.itemAt(row).setParent(None)

    def clear(self):
        for row in reversed(range(self.count())):
            for widget in reversed(range(self.itemAt(row).count())):
                self.itemAt(row).itemAt(widget).widget().setParent(None)
        for row in reversed(range(self.count())):
            self.itemAt(row).setParent(None)


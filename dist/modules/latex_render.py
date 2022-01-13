import re
from sys import argv, exit

from PyQt5 import QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class MathTextLabel(QtWidgets.QWidget):

    def __init__(self, mathText, parent=None, **kwargs):
        super(QtWidgets.QWidget, self).__init__(parent, **kwargs)
        l = QVBoxLayout(self)
        l.setContentsMargins(0, 0, 0, 0)
        r, g, b, a = self.palette().base().color().getRgbF()
        self.tex_fig = Figure(edgecolor=(r, g, b), facecolor=(r, g, b))
        self.canv = FigureCanvas(self.tex_fig)
        l.addWidget(self.canv)
        self.tex_fig.clear()
        text = self.tex_fig.suptitle(
            mathText,
            x=0.0,
            y=1.0,
            horizontalalignment='left',
            verticalalignment='top',
            size=QtGui.QFont().pointSize() * 2
        )
        self.canv.draw()
        (x0, y0), (x1, y1) = text.get_window_extent().get_points()
        w = x1 - x0
        h = y1 - y0
        self.tex_fig.set_size_inches(w / 80, h / 80)
        self.setFixedSize(int(w), int(h))


class Widget(QtWidgets.QWidget):
    def __init__(self, parent=None, **kwargs):
        super(QtWidgets.QWidget, self).__init__(parent)
        self.setWindowTitle("Max TeX")

        l = QVBoxLayout(self)
        math_text = kwargs["text"]
        math_text = rf"{math_text}"
        l.addWidget(MathTextLabel(math_text, self), alignment=Qt.AlignHCenter)


class MathText:

    def __init__(self, **kwargs):
        self.math_text_input = kwargs["text"]

    def __call__(self):
        app = QtWidgets.QApplication(argv)
        widget = Widget(text=self.math_text_input)
        widget.show()
        widget.raise_()
        exit(app.exec_())


class MathTextRegex:

    def __init__(self, _input):
        self.input = _input

    def __call__(self):
        return self.text(self.input)

    @staticmethod
    def text(_input) -> str:
        # Current implementation of this code only works on whitespace
        digits = re.split(' ', _input)
        solution = ''

        # Attempting to implement parenthesis matching
        stack = []
        for index, element in enumerate(digits):
            print(digits)
            if '(' in element:
                stack.append(element)
                digits[index] = str(element.split('(')[1])
            if ')' in element:
                if not stack:
                    print("INCORRECT PARENTHESIS")
                else:
                    stack.pop(0)
                digits[index] = str(element.split(')')[0])
        for index, element in enumerate(digits):
            if '/' in element:
                nominator = digits[index].split('/')[0]
                denominator = digits[index].split('/')[1]
                digits.pop(index)
                string = '${\\frac' + '{' + nominator + '}' + '{' + denominator + '}}$'
                digits.insert(index, string)
            if 'sin' in element:
                value = str(element.split('(')[1])
                digits[index] = '$\\sin(' + value + ')$'
            if 'cos' in element:
                value = str(element.split('(')[1])
                digits[index] = '$\\cos(' + value + ')$'
            if 'tan' in element:
                value = str(element.split('(')[1])
                digits[index] = '$\\tan(' + value + ')$'
            if 'root' in element:
                value = str(element.split('(')[1])
                digits[index] = '$\\sqrt{' + value + '}$'
            if 'diff' in element:
                value = str(element.split('(')[1])
                digits[index] = '$f\'(' + value + ')$'
            if 'int' in element:
                value = str(element.split('(')[1])
                digits[index] = '$\\int(' + value + ')$'
        for i in digits:
            solution += i

        # Checks for parenthesis, could be changed to return False and throw error
        if stack:
            print("INCORRECT PARENTHESIS")
        return solution


if __name__ == '__main__':
    input = ""

    new_string = MathTextRegex("int(diff(3x+2) + 2/5 * sin(4x^2) + 4))")()
    text_widget = MathText(text=f"{new_string}")

    text_widget()

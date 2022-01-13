import matplotlib.pyplot as plt
import numexpr as ne
import numpy as np
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from sympy import sympify, lambdify, latex
from sympy.abc import x

from GUI.ui_interface import *
from modules.stylesheetloader import StyleSheetLoader as ss_loader


class GraphFrame(QFrame):

    def __init__(self, user_input):
        super(GraphFrame, self).__init__()

        graph_input = ""

        if type(user_input) is str:
            try:

                graph_input = str(user_input).split("-graph")[1]

            except Exception as e:
                print(e)
                pass

        self.setStyleSheet(ss_loader().load(filename="graphframe.txt"))

        self.graph_layout = QGridLayout()
        self.setFixedSize(854, 400)

        self.graph_layout.addWidget(GraphWidget(graph_input), alignment=Qt.AlignCenter)

        # self.graph_layout.addWidget(GraphWidget(self, graph_input), alignment=Qt.AlignCenter)
        self.setLayout(self.graph_layout)


class GraphWidget(QWidget):

    def __init__(self, user_input, parent=None):
        super().__init__(parent)

        self.user_input = user_input

        self.figure = plt.figure()

        self.canvas = FigureCanvas(self.figure)

        self.toolbar = NavigationToolbar(self.canvas, self)

        self.toolbar.setStyleSheet(ss_loader().load(filename="matplottoolbar.txt"))

        layout = QVBoxLayout()
        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)
        self.setLayout(layout)

        if "-integrate" in self.user_input:
            self.integrate()

        if "-differentiate" in self.user_input:
            self.differentiate()

        if "-zero" in self.user_input:
            self.zero_cross()

        if "-function" in self.user_input:
            self.plot_function()

        if "-3d" in self.user_input:
            self.two_variable()

    def plot_function(self):

        user_input = self.user_input

        user_input = user_input.split("-function")[1]

        eq = sympify(user_input)
        latex_eq = str(latex(eq))

        equation = lambdify((x), eq, modules=['numpy'])

        axes = self.figure.add_subplot(111)

        print(user_input)

        axes.axhline(linewidth=2, color='black')
        axes.axvline(linewidth=2, color='black')
        axes.grid()

        t = np.linspace(-10, 10, 512, endpoint=True)

        axes.set_title(rf'Function of x')

        axes.plot(t, equation(t), label=rf'${latex_eq}$')

        axes.legend(loc='upper left')

        self.canvas.draw()

    def two_variable(self):

        user_input = self.user_input
        user_input = user_input.split("-3d")[1]

        eq = sympify(user_input)
        latex_equation = latex(eq)

        axes = self.figure.add_subplot(111, projection='3d')

        x = np.linspace(0, 2 * np.pi, 100)
        y = np.linspace(0, np.pi, 100)
        x, y = np.meshgrid(x, y)
        z = ne.evaluate(user_input)

        axes.set_title(rf'$f (x,y) = {latex_equation}$')
        axes.plot_surface(x, y, z, color='b', label=rf'${user_input}$')

        self.canvas.draw()

    @staticmethod
    def checkCrossing(y) -> bool:
        for index, element in enumerate(y):
            if (y[index - 1] < 0 and y[index] > 0 or y[index - 1] > 0 and y[index] < 0 or y[index] == 0) and index != 0:
                return True
        return False

    @staticmethod
    def findCrossings(y) -> list:
        crossings = []
        for index, element in enumerate(y):
            if (y[index - 1] < 0 and y[index] > 0 or y[index - 1] > 0 and y[index] < 0 or y[index] == 0) and index != 0:
                crossings.append(index - 1)
        return crossings

    def integrate(self):
        user_input = self.user_input

        user_input = user_input.split("-integrate")[1]

        eq = sympify(user_input)
        latex_eq = str(latex(eq))

        solution_integ = str(latex(eq.integrate(x))) + " + c"

        eval_integ = lambdify((x), eq.integrate(x), modules=['numpy'])

        axes = self.figure.add_subplot(111)

        axes.axhline(linewidth=2, color='black')
        axes.axvline(linewidth=2, color='black')

        axes.grid()

        t = np.linspace(-10, 10, 512, endpoint=True)

        axes.set_title(rf'$\int({latex_eq})dx$' + " = " + rf"${solution_integ}$")

        axes.plot(t, eval_integ(t), label=rf'$\int({latex_eq})dx$')

        axes.legend(loc='upper left')

        self.canvas.draw()

    def differentiate(self):
        user_input = self.user_input

        user_input = user_input.split("-differentiate")[1]

        eq = sympify(user_input)
        latex_eq = str(latex(eq))

        solution_deriv = str(latex(eq.diff(x)))

        eval_deriv = lambdify((x), eq.diff(x), modules=['numpy'])

        d_dx = r"$\frac{{d}}{dx}$"

        axes = self.figure.add_subplot(111)

        axes.axhline(linewidth=2, color='black')
        axes.axvline(linewidth=2, color='black')

        axes.grid()

        t = np.linspace(-10, 10, 512, endpoint=True)

        axes.set_title(rf'{d_dx}${latex_eq}$' + " = " + rf"${solution_deriv}$")

        axes.plot(t, eval_deriv(t), label=rf'{d_dx}${latex_eq}$')

        axes.legend(loc='upper left')

        self.canvas.draw()

    def zero_cross(self):

        user_input = self.user_input

        axes = self.figure.add_subplot(111)
        axes.axhline(linewidth=2, color='black')
        axes.axvline(linewidth=2, color='black')
        axes.grid()

        # Crossing Axis
        axis = (user_input.split("axis=")[1]).split("degree")[0]

        # Polynomial Degree 2/3
        degree = int((user_input.split("degree=")[1]).split("function=")[0])

        # Equation
        function = str(user_input.split("function=")[1])
        function = function.lower()
        function = function.replace("*x", "x")
        function = function.replace("**", "^")

        a: int = 0
        b: int = 0
        c: int = 0
        d: int = 0
        y: int = 0

        x = np.linspace(-10, 10, 512, endpoint=True)

        if degree == 2:

            a = int(function.split("x^2")[0])
            function = function.split("x^2+")[1]
            b = int(function.split("x")[0])
            function = function.split("x")[1]
            c = int(function)
            y = (a * (x * x)) + (b * x) + c
            axes.set_title("Zero Cross 2nd Degree")
            axes.plot(x, y, label=rf'$y = {a}x^2 + {b}x + {c}$')
            axes.legend(loc='upper left')

        elif degree == 3:

            a = int(function.split("x^3+")[0])
            function = function.split("x^3+")[1]
            b = int(function.split("x^2")[0])
            function = function.split("x^2+")[1]
            c = int(function.split("x")[0])
            function = function.split("x")[1]
            d = int(function)

            y = (a * (x * x)) + (b * x) + c
            axes.set_title("Zero Cross 3rd Degree")
            axes.plot(x, y, '-g', label=rf'$y = {a}x^3+ {b}x^2 + {c}x + {d}$')
            axes.legend(loc='upper left')

        if axis == "x":
            if self.checkCrossing(y):
                if degree == 2:
                    p = [a, b, c]
                else:
                    p = [a, b, c, d]
                roots = np.roots(p)

                axes.set_xlim([x.min(), x.max()])
                axes.set_ylim([-50, 50])

                for i in roots:
                    axes.plot(i, 0, marker='o', markersize=3, color="red")
                self.canvas.draw()

            else:
                print("No zero crossing found.")

        else:
            if self.checkCrossing(x):

                if degree == 2:
                    axes.plot(0, c, marker='o', markersize=3, color="red")

                else:
                    axes.plot(0, d, marker='o', markersize=3, color="red")

                axes.set_xlim([x.min(), x.max()])
                axes.set_ylim([-50, 50])

                self.canvas.draw()
            else:
                print("No zero crossing found.")

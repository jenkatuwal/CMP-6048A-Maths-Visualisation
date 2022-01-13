import matplotlib.pyplot as plt
import numpy as np
import RenderPlotCalc


# Console mode
class ConsoleMain:

    def __init__(self, args) -> None:
        self.window_name = "Maths Visualisation"

        # python main.py -graph -zero
        # python main.py -diff
        # python main.py -int
        # python main.py -3d

        if args[1] == "-graph":
            if "-zero" in args:
                _input = input("Intercept?(x/y): ")
                self.zeroCrossPlot(_input)
        elif args[1] == "-diff" or args[-1] == "differentiate":
            degree = int(input("Polynomial degree?: "))
            _input_list = []
            for i in range(degree + 1):
                if i != degree:
                    _input_list.append(int(input(rf'ax^{degree - i}: ')))
                else:
                    _input_list.append(int(input(rf'a: ')))

            print(self.differentiate(*_input_list))
        elif args[1] == "-int" or args[-1] == "-integrate":
            degree = int(input("Polynomial degree?: "))
            _input_list = []
            for i in range(degree + 1):
                if i != degree:
                    _input_list.append(int(input(rf'ax^{degree - i}: ')))
                else:
                    _input_list.append(int(input(rf'a: ')))

            print(self.integrate(*_input_list))
        elif args[1] == "-3d":
            self.twoVariablePlot(lambda x, y: np.sin(np.sqrt(x ** 2 + y ** 2)))
        else:
            args.pop(0)
            raw_in = ""
            for element in args:
                raw_in = raw_in + element
            answer, exception = RenderPlotCalc.math_lang_process(raw_in)
            if exception:
                print(exception.err_type)
            else:
                print(answer)

    # Code in plots for Zero crossings, differentiation and integrals. 2 or more variables.
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

    #
    # Input coefficients left-right decreasing order of polynomials.
    #
    # Example
    # 3x^2 + 4x + 2    ->   differentiate(3, 4, 2)
    #
    # Second Example
    # 5x^5 + 2x^2 - 4  ->   differentiate(5, 0, 0, 2, -4)
    #
    @staticmethod
    def differentiate(*args) -> list:
        derivative: list = []
        degree = len(args) - 1
        for i in args:
            derivative.append(degree * i)
            degree -= 1
        return derivative

    @staticmethod
    def integrate(*args) -> list:
        integral: list = []
        degree = len(args) - 1
        for i in args:
            integral.append(i / (degree + 1))
            degree -= 1
        integral.append("c")
        return integral

    @staticmethod
    def test_function(x, y):
        return np.sin(np.sqrt(x ** 2 + y ** 2))

    #
    # Input a function of x and y
    #
    # Example
    # f(x, y) = x^2 + y^2   -> twoVariablePlot(def f(x, y): return x** + y**)
    @staticmethod
    def twoVariablePlot(function) -> None:

        # Has no reference of graph size.
        x = np.linspace(-7, 7, 30)
        y = np.linspace(-7, 7, 30)
        x, y = np.meshgrid(x, y)
        z = function(x, y)
        fig = plt.figure()
        axes = plt.axes(projection='3d')
        axes.plot_surface(x, y, z, rstride=1, cstride=1, cmap='viridis', edgecolor='none')
        axes.set_xlabel('x')
        axes.set_ylabel('y')
        axes.set_zlabel('z')
        plt.show()

    def zeroCrossPlot(self, axis: str) -> None:

        degree: int = int(input("Polynomial degree?(2~3): "))

        a: int = 0
        b: int = 0
        c: int = 0
        d: int = 0
        y: int = 0

        x = np.linspace(-10, 10, 512, endpoint=True)

        if degree == 2:
            a = int(input("ax²: "))
            b = int(input(rf"{a}x² + ax: "))
            c = int(input(rf"{a}x² + {b}x + a: "))
            y = (a * (x * x)) + (b * x) + c
            plt.plot(x, y, '-g', label=rf'$y = {a}x^2 + {b}x + {c}$')
        elif degree == 3:
            a = int(input("ax³: "))
            b = int(input(rf"{a}x³+ ax²: "))
            c = int(input(rf"{a}x³+ {b}x² + ax: "))
            d = int(input(rf"{a}x³+ {b}x² + {c}x + a: "))
            y = (a * (x * x * x)) + (b * (x * x)) + (c * x) + d
            plt.plot(x, y, '-g', label=rf'$y = {a}x³+ {b}x² + {c}x + {d}$')
        else:
            print("error :/")

        if axis == "x":
            if self.checkCrossing(y):
                if degree == 2:
                    p = [a, b, c]
                else:
                    p = [a, b, c, d]
                roots = np.roots(p)
                float_array = roots.astype(float)
                axes = plt.gca()
                axes.set_xlim([x.min(), x.max()])
                axes.set_ylim([-50, 50])
                axes.axhline(linewidth=2, color='black')
                axes.axvline(linewidth=2, color='black')

                for i in float_array:
                    plt.plot(i, 0, marker='o', markersize=3, color="red")
                plt.grid()
                plt.xlabel('x')
                plt.ylabel('y')
                plt.title('Zero crossing')
                plt.legend(loc='upper left')
                plt.show()
            else:
                print("No zero crossing found.")
        else:
            if self.checkCrossing(x):

                axes = plt.gca()
                axes.set_xlim([x.min(), x.max()])
                axes.set_ylim([y.min() - (y.max() / 2), y.max()])
                axes.axhline(linewidth=2, color='black')
                axes.axvline(linewidth=2, color='black')
                if degree == 2:
                    plt.plot(0, c, marker='o', markersize=3, color="red")
                else:
                    plt.plot(0, d, marker='o', markersize=3, color="red")
                plt.grid()
                plt.xlabel('x')
                plt.ylabel('y')
                plt.title('Zero crossing')
                plt.legend(loc='upper left')
                plt.show()
            else:
                print("No zero crossing found.")


if __name__ == "__main__":
    pass

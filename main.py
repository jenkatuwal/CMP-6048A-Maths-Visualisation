# This needs to be imported first.
from sys import path

path.append('GUI/')
path.append('modules/')
from PySide2 import QtCore
from PySide2.QtGui import QIcon
from modules.stylesheetloader import StyleSheetLoader as ssl_loader
from modules.help import Help
from modules.splashscreen import SplashScreen
from modules.symboltext import SymbolTextWidget
from modules.console import ConsoleMain
from GUI.ui_interface import *
from modules.CustomGridLayout import CustomGridLayout
from modules.TextInput import TextInput
from modules.SolutionFrame import SolutionFrame
from modules.RenderPlotCalc import math_lang_process
from modules.GraphFrame import GraphFrame
from sympy import sympify, latex
from sympy.abc import x
from sympy.solvers import solve


class MainWindow(QMainWindow):
    text_input_dict = {}

    def __init__(self) -> None:
        # Initialise MainWindow and setup UI
        QMainWindow.__init__(self, None)
        self.effect = None
        self.current_text_input = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.math_layout = QVBoxLayout()
        # For showing and hiding
        self.math_widget = False

        # For when the menu is expanded
        self.menu_open: bool = False

        # Window Properties
        self.setWindowTitle("Maths Visualisation")
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # Show lambda: function, executes the function when the button is clicked.
        # can also be written as self.ui.minBtn.clicked.connect(self.showMinimized)
        # This applies to all the scenarios
        self.ui.minBtn.clicked.connect(lambda: self.showMinimized())

        # Attributes that will be set in runtime
        self.clickPosition = None
        self.splash = None
        self.animation = None
        self.menu = None

        # Show Window
        self.setWindowIcon(QIcon("images/icon.png"))

        # Set the icon image of the help button
        self.ui.help_btn.setIcon(QIcon("images/outline_help_white_48dp"))

        self.ui.add_text_input_btn.setIcon(QIcon("images/new.png"))
        self.ui.add_text_input_btn.clicked.connect(lambda: self.add_text_input(1))

        # Add keyboard shortcut
        self.add_text_input_shortcut = QShortcut(QKeySequence('Ctrl+N'), self)
        self.add_text_input_shortcut.activated.connect(lambda: self.add_text_input(1))
        self.open_help_shortcut = QShortcut(QKeySequence('Ctrl+H'), self)
        self.open_help_shortcut.activated.connect(lambda: self.show_help())
        self.ui.add_text_input_btn.setToolTip("New Cells")

        self.ui.delete_all_btn.setIcon(QIcon("images/baseline_delete_white_36dp.png"))

        self.ui.delete_all_btn.clicked.connect(lambda: self.outputlayout.clear())

        self.ui.delete_all_btn.setToolTip("Delete all cells")

        self.ui.tooltip_label.setText("Add a cell to get started (CTRL+ N) or CTRL+ H to show commands.")

        # Show raise the main window when called
        self.show()
        self.raise_()
        self.activateWindow()

        # Open slide menu
        self.ui.math_symbol_button.clicked.connect(lambda: self.slideTopMenu())
        self.ui.math_symbol_button.clicked.connect(lambda: self.is_math_checked())
        self.ui.math_symbol_button.setToolTip("Math input dropdown")

        # Window icon clicked go back to splashscreen
        self.ui.window_icon.clicked.connect(lambda: self.show_splash())

        self.ui.window_icon.setIcon(QIcon("images/icon.png"))

        # For testing - Math input testing
        symbol_text = r'Latex Example String: $\int(3 x^{3} - x^{2} + 6) dx = \frac{3 x^{4}}{4} - \frac{x^{3}}{3} + 6 ' \
                      r'x + c$ '

        # Text box for math_text input
        self.ui.input_edit.setText(symbol_text)
        self.ui.input_edit.setMaxLength(117)
        self.ui.input_edit.textChanged.connect(lambda: self.addMath())

        # Get mouse position and move the window around when holding on the tob bar, since we have used
        # Qt frameless window
        def moveWindow(e) -> None:
            if not self.isMaximized():
                if e.buttons() == Qt.LeftButton:
                    self.move(self.pos() + e.globalPos() - self.clickPosition)
                    self.clickPosition = e.globalPos()
                    e.accept()

        self.ui.headerFrame.mouseMoveEvent = moveWindow

        self.ui.closeBtn.clicked.connect(lambda: self.close())
        self.ui.help_btn.clicked.connect(lambda: self.show_help())

        self.ss_loader = ssl_loader()

        # ssl_loader is a custom-made class that loads stylesheets in the correct formatting from text files.
        self.setStyleSheet(self.ss_loader.load(filename="mainwindow.txt"))

        # This is the latex rendering widget, text input is passed into the class init method. Then it is rendered.
        self.math_widget = SymbolTextWidget(r"Type Latex inside '\$$' to render here.", self)
        self.math_layout.addWidget(self.math_widget, alignment=Qt.AlignCenter)
        self.ui.math_text_frame.setLayout(self.math_layout)

        # QT uses box layouts for widget placement
        self.outputlayout = CustomGridLayout()
        self.ui.output_frame.setLayout(self.outputlayout)

        # Gui style sheets
        self.text_input_error_ss = self.ss_loader.load(filename="redtextbot.txt")
        self.default_text_input_ss = self.ss_loader.load(filename="defaulttextinput.txt")

        # This is for getting which widget the user is focused on.
        self.focused_widget = None

        def add_text_box(e):
            if e.key() == QtCore.Qt.Key_Return:

                self.focused_widget = self.focusWidget()
                user_input = self.focused_widget.text()

                # math_lang_process() is the method we use to evaluate user input to our lexer/parser.
                result, error = math_lang_process(user_input)
                if error:

                    self.focused_widget.setStyleSheet(self.text_input_error_ss)

                    self.ui.tooltip_label.setText(f"Error: {error.err_type}")
                    pass

                else:
                    self.focused_widget.setStyleSheet(self.default_text_input_ss)
                    self.ui.tooltip_label.setText(f"")
                    self.add_text_input(1)
                    self.add_solution_frame(str(result))

                if "-graph" in user_input and user_input != "-graph":
                    self.focused_widget.setStyleSheet(self.default_text_input_ss)
                    self.ui.tooltip_label.setText(f"")
                    user_input = user_input.lower()
                    user_input = user_input.replace(" ", "")

                    try:
                        self.add_text_input(1)
                        self.outputlayout.insertRow(2)
                        self.outputlayout.addWidget(GraphFrame(user_input), 2, 0)

                    except Exception:

                        self.focused_widget.setStyleSheet(self.text_input_error_ss)

                        self.ui.tooltip_label.setText(f"Error: Incorrect Syntax")

                        self.outputlayout.delete_row(3)

                if "-differentiate" in user_input and "-graph" not in user_input and len(user_input) != len(
                        "-differentiate"):
                    self.focused_widget.setStyleSheet(self.default_text_input_ss)

                    self.add_text_input(1)
                    self.outputlayout.insertRow(2)
                    self.add_solution_frame(self.differentiate(user_input))
                    self.ui.tooltip_label.setText(f"")

                if "-integrate" in user_input and "-graph" not in user_input and len(user_input) != len("-integrate"):
                    self.focused_widget.setStyleSheet(self.default_text_input_ss)

                    self.add_text_input(1)
                    self.outputlayout.insertRow(2)
                    self.add_solution_frame(self.integrate(user_input))
                    self.ui.tooltip_label.setText(f"")

                if "-solve" in user_input and "-graph" not in user_input and len(user_input) != len(
                        "-solve"):
                    self.focused_widget.setStyleSheet(self.default_text_input_ss)

                    self.add_text_input(1)
                    self.outputlayout.insertRow(2)
                    self.add_solution_frame(self.solve(user_input))
                    self.ui.tooltip_label.setText(f"")

                if user_input == "-clear":
                    self.outputlayout.clear()
                    self.ui.tooltip_label.setText(f"")

                if user_input == "-help":
                    self.show_help()

        # Listen for 'return' pressed by the user to add a new text and calculate users input.
        self.ui.output_frame.keyPressEvent = add_text_box

    # Using the sympy differentiate module to take in user input and return the derivative in a latex format.
    @staticmethod
    def differentiate(user_input):

        user_input = user_input.split("-differentiate")[1]
        eq = sympify(user_input)
        latex_eq = str(latex(eq))

        solution_deriv = eq.diff(x)
        latex_solution_deriv = str(latex(solution_deriv))

        return r"$ \frac{d}{dx} (" + latex_eq + ")  = " + latex_solution_deriv + "$"

    # Using the sympy integrate module to take in user input and return the derivative in a latex format.#
    @staticmethod
    def integrate(user_input):

        user_input = user_input.split("-integrate")[1]
        eq = sympify(user_input)
        latex_eq = str(latex(eq))
        solution_integ = str(latex(eq.integrate(x))) + " + c"
        solution_integ = rf'$\int({latex_eq}) dx = {solution_integ}$'

        return solution_integ

    # Quadratic Equation Solver
    @staticmethod
    def solve(user_input):

        user_input = user_input.split("-solve")[1]
        eq = sympify(user_input)
        latex_eq = str(latex(eq))

        answer = solve(user_input, x)

        latex_answer = rf'${latex(sympify(answer))}$'
        return latex_answer

    # Method for getting the position of the users text input in the main window
    @classmethod
    def text_index(cls):
        return cls.text_input_dict

    # Check if the main window dropdown menu is open.
    def is_math_checked(self):
        if self.ui.math_symbol_button.isChecked():
            self.ui.math_symbol_button.setStyleSheet(self.ss_loader.load(filename="mathsymbolcheck.txt"))

    # Add glow effect to widget
    @staticmethod
    def add_glow_effect(widget, toggle):
        effect = QGraphicsDropShadowEffect(widget)
        if toggle:
            effect.setOffset(0, 0)
            effect.setBlurRadius(5)
            effect.setColor(QColor(10, 255, 10))
            widget.setGraphicsEffect(effect)
        else:
            effect.setEnabled(False)

    # Display the glow effect
    def manage_glow(self):
        if len(self.ui.output_frame.findChildren(TextInput)) == 0:
            self.add_glow_effect(self.ui.add_text_input_btn, True)
        else:
            self.add_glow_effect(self.ui.add_text_input_btn, False)

    # Add the user input text box
    def add_text_input(self, row):
        text_input = TextInput()
        self.current_text_input = text_input
        text_list = self.ui.output_frame.findChildren(TextInput)
        if len(text_list) != 0:
            for i in text_list:
                i.setReadOnly(True)
        self.outputlayout.insertRow(row)
        self.outputlayout.addWidget(text_input, row, 0)
        text_input.setFocus()

    # Add the output of a users calculation
    def add_solution_frame(self, text):
        self.outputlayout.insertRow(2)
        self.outputlayout.addWidget(SolutionFrame(text), 2, 0)

    # Add the graph frame
    def add_graph_frame(self, text):
        self.outputlayout.insertRow(2)

        try:
            self.outputlayout.addWidget(GraphFrame(text), 2, 0)

        except Exception:
            pass

    def addMath(self) -> None:

        self.refresh_math()
        symbol_text = self.ui.input_edit.text()
        self.math_widget = SymbolTextWidget(symbol_text, self)
        self.math_layout.addWidget(self.math_widget, alignment=Qt.AlignCenter)
        self.ui.math_text_frame.setLayout(self.math_layout)

    def fade(self, widget):

        self.effect = QGraphicsOpacityEffect()
        widget.setGraphicsEffect(self.effect)

        self.animation = QtCore.QPropertyAnimation(self.effect, b"opacity")
        self.animation.setDuration(1)
        self.animation.setStartValue(1)
        self.animation.setEndValue(0)
        self.animation.start()

    def un_fade(self, widget):

        self.effect = QGraphicsOpacityEffect()
        widget.setGraphicsEffect(self.effect)

        self.animation = QtCore.QPropertyAnimation(self.effect, b"opacity")
        self.animation.setDuration(500)
        self.animation.setStartValue(0)
        self.animation.setEndValue(1)
        self.animation.start()

    # Deletes and redraws the latex render of the text entered.
    def refresh_math(self):
        for i in reversed(range(self.math_layout.count())):
            layout_item = self.math_layout.itemAt(i)
            if layout_item.widget() is not None:
                self.math_layout.removeWidget(self.math_widget)
                self.math_widget.deleteLater()
                self.math_widget = None

    def mousePressEvent(self, event: QEvent) -> None:
        self.clickPosition = event.globalPos()

    # Show splash screen
    def show_splash(self) -> None:
        self.splash = SplashScreen()
        self.un_fade(self.splash)
        # self.splash.show()
        self.close()

    # Show help screen
    def show_help(self) -> None:
        _help = Help()
        _help.show()
        self.close()

    # Open the top sliding menu
    def slideTopMenu(self) -> None:

        height = self.ui.top_menu_frame.height()
        self.ui.math_symbol_button.setStyleSheet(self.ss_loader.load(filename='topmenuhoverclosed.txt'))

        if height == 50:

            self.ui.math_symbol_button.setStyleSheet(self.ss_loader.load(filename='topmenubuttonline.txt'))
            self.menu_open = True
            new_height = 150
            self.ui.math_text_frame.setStyleSheet(self.ss_loader.load(filename='opentopframe.txt'))

            # Checks if a math widget is there first.
            if not self.math_widget:
                pass

            else:
                self.math_widget.show()

        else:

            self.menu_open = False
            new_height = 50

            if not self.math_widget:
                pass

            else:
                self.math_widget.hide()
                pass

        self.ui.math_symbol_button.setStyleSheet(self.ss_loader.load(filename='mathsymbolbuttonhover.txt'))

        # Animate minimumHeight
        self.animation = QPropertyAnimation(self.ui.top_menu_frame, b"minimumHeight")
        self.animation.setDuration(250)

        # Start value is the current menu width
        self.animation.setStartValue(height)

        # end value is the new menu width
        self.animation.setEndValue(new_height)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()


if __name__ == "__main__":
    from sys import exit, argv

    args = argv

    if len(args) > 1:
        app = ConsoleMain(args)
        # app.run()
        exit()
    else:
        app = QApplication()
        # window = MainWindow()
        window = SplashScreen()
        exit(app.exec_())

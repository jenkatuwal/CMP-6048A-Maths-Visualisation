from GUI.ui_interface import *


class SplashScreen(QMainWindow):

    def __init__(self):

        QMainWindow.__init__(self, None)
        from PySide2 import QtCore
        from PySide2.QtGui import QIcon
        from GUI.ui_splashscreen import Ui_SplashScreen

        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon("images/icon.png"))
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.clickPosition = None
        self.main = None
        self.filePath = ""
        self.shadow = None
        self.animation_started = False

        def moveWindow(e: QEvent) -> None:
            if not self.isMaximized():
                if e.buttons() == Qt.LeftButton:
                    self.move(self.pos() + e.globalPos() - self.clickPosition)
                    self.clickPosition = e.globalPos()
                    e.accept()

        self.ui.centralwidget.mouseMoveEvent = moveWindow
        self.show()

        self.ui.new_button.clicked.connect(lambda: self.showMain())
        self.ui.exit_button.clicked.connect(lambda: self.close())

        self.ui.new_button.setToolTip('New')
        self.ui.exit_button.setToolTip('Exit')

        self.ui.new_button.enterEvent = lambda event: self.ui.tooltip.setText(
            'New')

        self.ui.exit_button.enterEvent = lambda event: self.ui.tooltip.setText(
            'Exit')
        self.ui.centralwidget.enterEvent = lambda event: self.ui.tooltip.setText(
            '')
        self.ui.footer_frame.enterEvent = lambda event: self.ui.tooltip.setText(
            '')
        self.ui.buttons_frame.enterEvent = lambda event: self.ui.tooltip.setText(
            '')
        self.ui.icon_frame.enterEvent = lambda event: self.ui.tooltip.setText(
            '')

    def showMain(self) -> None:
        from main import MainWindow

        self.close()
        self.main = MainWindow()
        self.un_fade(self.main)

    def mousePressEvent(self, event: QEvent) -> None:
        self.clickPosition = event.globalPos()

    def set_drop_shadow(self) -> QGraphicsDropShadowEffect:
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(5)
        return self.shadow

    def fade(self, widget):
        self.effect = QGraphicsOpacityEffect()
        widget.setGraphicsEffect(self.effect)

        self.animation = QPropertyAnimation(self.effect, b"opacity")
        self.animation.setDuration(1)
        self.animation.setStartValue(1)
        self.animation.setEndValue(0)
        self.animation.start()

    def un_fade(self, widget):
        self.effect = QGraphicsOpacityEffect()
        widget.setGraphicsEffect(self.effect)

        self.animation = QPropertyAnimation(self.effect, b"opacity")
        self.animation.setDuration(500)
        self.animation.setStartValue(0)
        self.animation.setEndValue(1)
        self.animation.start()

    def openFile(self) -> Exception:

        options = QFileDialog.Options()

        self.filePath, _ = QFileDialog.getOpenFileName(
            None,
            "Open",
            "",
            "All Files (*)",
            options=options,
        )

        try:
            with open(self.filePath, 'r') as file:
                # Open File Logic here
                print(file)
                pass

        except Exception as e:
            return e

from GUI.ui_interface import *

# Max -----


class Help(QMainWindow):

    def __init__(self) -> None:
        from PySide2 import QtCore
        from PySide2.QtGui import QIcon
        from GUI.ui_help import Ui_Help

        QMainWindow.__init__(self, None)

        self.ui = Ui_Help()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon("images/icon.png"))
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.clickPosition = None

        self.ui.return_button.setIcon(QIcon('images/undo.png'))

        self.ui.closeBtn.clicked.connect(lambda: self.close())
        self.ui.return_button.clicked.connect(lambda: self.showMain())

        def moveWindow(e: QEvent) -> None:
            if not self.isMaximized():
                if e.buttons() == Qt.LeftButton:
                    self.move(self.pos() + e.globalPos() - self.clickPosition)
                    self.clickPosition = e.globalPos()
                    e.accept()

        self.ui.centralwidget.mouseMoveEvent = moveWindow
        self.show()

    def mousePressEvent(self, event: QEvent) -> None:
        self.clickPosition = event.globalPos()

    def un_fade(self, widget):
        self.effect = QGraphicsOpacityEffect()
        widget.setGraphicsEffect(self.effect)

        self.animation = QPropertyAnimation(self.effect, b"opacity")
        self.animation.setDuration(500)
        self.animation.setStartValue(0)
        self.animation.setEndValue(1)
        self.animation.start()

    def showMain(self) -> None:
        from main import MainWindow
        _main = MainWindow()
        self.un_fade(_main)
        _main.show()
        self.close()

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'splashscreenwGikUp.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_SplashScreen(object):
    def setupUi(self, SplashScreen):
        if not SplashScreen.objectName():
            SplashScreen.setObjectName(u"SplashScreen")
        SplashScreen.resize(472, 554)
        SplashScreen.setMaximumSize(QSize(500, 554))
        SplashScreen.setStyleSheet(u"border-radius: 10px;")
        self.centralwidget = QWidget(SplashScreen)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"border-style: solid;\n"
"border-width: 2px;\n"
"border-color:rgb(61, 64, 70);\n"
"background-color: rgb(32, 33, 36);\n"
"border-radius: 10px;\n"
"background-color: rgb(32, 33, 36);\n"
"border-radius: 10px;")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.icon_frame = QFrame(self.centralwidget)
        self.icon_frame.setObjectName(u"icon_frame")
        self.icon_frame.setStyleSheet(u"background-color: rgb(32, 33, 36);\n"
"border-radius: 10px;\n"
"\n"
"border-width: 0px;")
        self.icon_frame.setFrameShape(QFrame.StyledPanel)
        self.icon_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.icon_frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.icon_frame)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setFamily(u"Microsoft PhagsPa")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"color:rgb(214, 214, 214);")
        self.label_2.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout_2.addWidget(self.label_2)

        self.frame_3 = QFrame(self.icon_frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(300, 300))
        self.label.setStyleSheet(u"border-radius:10px;\n"
"padding-right: 20px;")
        self.label.setPixmap(QPixmap(u"images/icon.png"))
        self.label.setScaledContents(True)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setMargin(0)
        self.label.setIndent(0)

        self.horizontalLayout.addWidget(self.label)


        self.verticalLayout_2.addWidget(self.frame_3)


        self.verticalLayout.addWidget(self.icon_frame)

        self.buttons_frame = QFrame(self.centralwidget)
        self.buttons_frame.setObjectName(u"buttons_frame")
        self.buttons_frame.setMinimumSize(QSize(450, 100))
        self.buttons_frame.setMaximumSize(QSize(450, 100))
        self.buttons_frame.setStyleSheet(u"QFrame{\n"
"border-top:    1px solid  rgb(61, 64, 70);\n"
"border-right:  0px solid;\n"
"border-bottom: 1px solid  rgb(61, 64, 70);\n"
"border-left:  0px solid;\n"
"background-color: rgb(32, 33, 36);\n"
"border-radius:0px\n"
"}\n"
"\n"
"")
        self.buttons_frame.setFrameShape(QFrame.StyledPanel)
        self.buttons_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.buttons_frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.new_button = QPushButton(self.buttons_frame)
        self.new_button.setObjectName(u"new_button")
        self.new_button.setMaximumSize(QSize(75, 75))
        self.new_button.setMouseTracking(True)
        self.new_button.setToolTipDuration(2)
        self.new_button.setStyleSheet(u"QPushButton:hover {\n"
"	background-color: rgb(56, 57, 61);\n"
"}\n"
"QPushButton{\n"
"border-width: 0px;}")
        icon = QIcon()
        icon.addFile(u"images/new image.png", QSize(), QIcon.Normal, QIcon.Off)
        self.new_button.setIcon(icon)
        self.new_button.setIconSize(QSize(85, 100))
        self.new_button.setFlat(True)

        self.horizontalLayout_2.addWidget(self.new_button)

        self.exit_button = QPushButton(self.buttons_frame)
        self.exit_button.setObjectName(u"exit_button")
        self.exit_button.setMaximumSize(QSize(75, 75))
        self.exit_button.setMouseTracking(True)
        self.exit_button.setToolTipDuration(2)
        self.exit_button.setStyleSheet(u"QPushButton:hover {\n"
"	background-color: rgb(56, 57, 61);\n"
"border-width: 0px;\n"
"}\n"
"QPushButton{\n"
"border-width: 0px;}")
        icon1 = QIcon()
        icon1.addFile(u"images/outline_exit_to_app_white_48dp.png", QSize(), QIcon.Normal, QIcon.Off)
        self.exit_button.setIcon(icon1)
        self.exit_button.setIconSize(QSize(85, 100))
        self.exit_button.setFlat(True)

        self.horizontalLayout_2.addWidget(self.exit_button)

        self.exit_button.raise_()
        self.new_button.raise_()

        self.verticalLayout.addWidget(self.buttons_frame)

        self.footer_frame = QFrame(self.centralwidget)
        self.footer_frame.setObjectName(u"footer_frame")
        font1 = QFont()
        font1.setPointSize(9)
        self.footer_frame.setFont(font1)
        self.footer_frame.setStyleSheet(u"\n"
"border-width: 0px;")
        self.footer_frame.setFrameShape(QFrame.StyledPanel)
        self.footer_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.footer_frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.version_label = QLabel(self.footer_frame)
        self.version_label.setObjectName(u"version_label")
        font2 = QFont()
        font2.setFamily(u"Microsoft PhagsPa")
        font2.setPointSize(9)
        font2.setItalic(False)
        self.version_label.setFont(font2)
        self.version_label.setStyleSheet(u"color:rgb(214, 214, 214);")

        self.horizontalLayout_3.addWidget(self.version_label)

        self.tooltip = QLabel(self.footer_frame)
        self.tooltip.setObjectName(u"tooltip")
        self.tooltip.setLayoutDirection(Qt.LeftToRight)
        self.tooltip.setStyleSheet(u"color:rgb(214, 214, 214);")
        self.tooltip.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.tooltip)


        self.verticalLayout.addWidget(self.footer_frame)

        SplashScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(SplashScreen)

        QMetaObject.connectSlotsByName(SplashScreen)
    # setupUi

    def retranslateUi(self, SplashScreen):
        SplashScreen.setWindowTitle(QCoreApplication.translate("SplashScreen", u"Splash Screen", None))
        self.label_2.setText(QCoreApplication.translate("SplashScreen", u"Maths Visualisation", None))
        self.label.setText("")
#if QT_CONFIG(tooltip)
        self.new_button.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.new_button.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.new_button.setText("")
#if QT_CONFIG(tooltip)
        self.exit_button.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.exit_button.setStatusTip("")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.exit_button.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.exit_button.setText("")
        self.version_label.setText(QCoreApplication.translate("SplashScreen", u"Maths Visualisation 1.0", None))
        self.tooltip.setText("")
    # retranslateUi


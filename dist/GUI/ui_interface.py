# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfaceIVWKkV.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(900, 900)
        MainWindow.setMinimumSize(QSize(900, 900))
        MainWindow.setMaximumSize(QSize(900, 900))
        MainWindow.setStyleSheet(u"QMainWindow{\n"
"	background-color: rgb(32, 36, 38);\n"
"}")
        self.actionNew = QAction(MainWindow)
        self.actionNew.setObjectName(u"actionNew")
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        self.actionClose = QAction(MainWindow)
        self.actionClose.setObjectName(u"actionClose")
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        self.actionSave_As = QAction(MainWindow)
        self.actionSave_As.setObjectName(u"actionSave_As")
        self.actionSave_Images = QAction(MainWindow)
        self.actionSave_Images.setObjectName(u"actionSave_Images")
        self.actionQuit = QAction(MainWindow)
        self.actionQuit.setObjectName(u"actionQuit")
        self.actionUndo = QAction(MainWindow)
        self.actionUndo.setObjectName(u"actionUndo")
        self.actionRedo = QAction(MainWindow)
        self.actionRedo.setObjectName(u"actionRedo")
        self.actionCut = QAction(MainWindow)
        self.actionCut.setObjectName(u"actionCut")
        self.actionCopy = QAction(MainWindow)
        self.actionCopy.setObjectName(u"actionCopy")
        self.actionpaste = QAction(MainWindow)
        self.actionpaste.setObjectName(u"actionpaste")
        self.actionDelete = QAction(MainWindow)
        self.actionDelete.setObjectName(u"actionDelete")
        self.actionSelect_All = QAction(MainWindow)
        self.actionSelect_All.setObjectName(u"actionSelect_All")
        self.actionEdit = QAction(MainWindow)
        self.actionEdit.setObjectName(u"actionEdit")
        self.actionblah_blah = QAction(MainWindow)
        self.actionblah_blah.setObjectName(u"actionblah_blah")
        self.actionstuff = QAction(MainWindow)
        self.actionstuff.setObjectName(u"actionstuff")
        self.actionstuff_2 = QAction(MainWindow)
        self.actionstuff_2.setObjectName(u"actionstuff_2")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"border-bottom-left-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"\n"
"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.headerFrame = QFrame(self.centralwidget)
        self.headerFrame.setObjectName(u"headerFrame")
        self.headerFrame.setMinimumSize(QSize(0, 40))
        self.headerFrame.setMaximumSize(QSize(10000, 40))
        self.headerFrame.setLayoutDirection(Qt.LeftToRight)
        self.headerFrame.setStyleSheet(u"\n"
"QFrame{\n"
"border-top-left-radius: 10px;\n"
"border-top-right-radius:10px;\n"
"border-bottom-left-radius: 0px;\n"
"border-bottom-right-radius:0px;\n"
"background-color: rgb(61, 64, 70);\n"
"}\n"
"\n"
"\n"
"")
        self.headerFrame.setFrameShape(QFrame.StyledPanel)
        self.headerFrame.setFrameShadow(QFrame.Raised)
        self.minBtn = QPushButton(self.headerFrame)
        self.minBtn.setObjectName(u"minBtn")
        self.minBtn.setGeometry(QRect(830, 11, 34, 20))
        self.minBtn.setMaximumSize(QSize(35, 16777215))
        self.minBtn.setStyleSheet(u"QPushButton:hover {\n"
"	background-color: rgb(56, 57, 61);\n"
"}\n"
"QPushButton{\n"
"	border-radius:10px;\n"
"}")
        icon = QIcon()
        icon.addFile(u"images/min ver 2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minBtn.setIcon(icon)
        self.minBtn.setIconSize(QSize(30, 30))
        self.closeBtn = QPushButton(self.headerFrame)
        self.closeBtn.setObjectName(u"closeBtn")
        self.closeBtn.setGeometry(QRect(864, 11, 28, 20))
        self.closeBtn.setMinimumSize(QSize(10, 0))
        self.closeBtn.setMaximumSize(QSize(35, 16777215))
        self.closeBtn.setStyleSheet(u"QPushButton:hover {\n"
"	background-color: rgb(56, 57, 61);\n"
"}\n"
"QPushButton{\n"
"	border-radius:10px;\n"
"}\n"
"")
        icon1 = QIcon()
        icon1.addFile(u"images/outline_close_white_48dp.png", QSize(), QIcon.Normal, QIcon.Off)
        self.closeBtn.setIcon(icon1)
        self.closeBtn.setIconSize(QSize(30, 30))
        self.title_label = QLabel(self.headerFrame)
        self.title_label.setObjectName(u"title_label")
        self.title_label.setGeometry(QRect(330, 7, 241, 31))
        font = QFont()
        font.setFamily(u"Microsoft PhagsPa")
        font.setPointSize(10)
        self.title_label.setFont(font)
        self.title_label.setStyleSheet(u"color:rgb(214, 214, 214);")
        self.title_label.setAlignment(Qt.AlignCenter)
        self.window_icon = QPushButton(self.headerFrame)
        self.window_icon.setObjectName(u"window_icon")
        self.window_icon.setGeometry(QRect(12, 7, 31, 31))
        self.window_icon.setStyleSheet(u"QPushButton:hover {\n"
"	background-color: rgb(56, 57, 61);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u"../images/icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.window_icon.setIcon(icon2)
        self.window_icon.setIconSize(QSize(28, 28))

        self.verticalLayout.addWidget(self.headerFrame)

        self.main_frame = QFrame(self.centralwidget)
        self.main_frame.setObjectName(u"main_frame")
        self.main_frame.setEnabled(True)
        self.main_frame.setStyleSheet(u"border-style: solid;\n"
"border-width: 3px;\n"
"border-color:rgb(61, 64, 70);\n"
"background-color: rgb(32, 33, 36);\n"
"QFrame{\n"
"	border-bottom-left-radius: 10px;\n"
"	border-bottom-right-radius: 10px;\n"
"	\n"
"}")
        self.main_frame.setFrameShape(QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.main_frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, -1)
        self.top_menu_frame = QFrame(self.main_frame)
        self.top_menu_frame.setObjectName(u"top_menu_frame")
        self.top_menu_frame.setMinimumSize(QSize(0, 50))
        self.top_menu_frame.setMaximumSize(QSize(1000, 150))
        self.top_menu_frame.setStyleSheet(u"border-bottom:0px solid;\n"
"border-radius:10px;\n"
"\n"
"background-color: rgb(81, 85, 93);\n"
"border-top:0px solid;\n"
"border-left:0px solid;\n"
"border-right:0px solid;\n"
"border-color: rgb(91, 91, 91);\n"
"border-radius:0px;\n"
"")
        self.top_menu_frame.setFrameShape(QFrame.StyledPanel)
        self.top_menu_frame.setFrameShadow(QFrame.Raised)
        self.math_text_frame = QFrame(self.top_menu_frame)
        self.math_text_frame.setObjectName(u"math_text_frame")
        self.math_text_frame.setGeometry(QRect(9, 50, 871, 70))
        self.math_text_frame.setMinimumSize(QSize(700, 0))
        self.math_text_frame.setMaximumSize(QSize(1000, 16777215))
        self.math_text_frame.setStyleSheet(u"")
        self.math_text_frame.setFrameShape(QFrame.StyledPanel)
        self.math_text_frame.setFrameShadow(QFrame.Raised)
        self.menu_buttons_frame = QFrame(self.top_menu_frame)
        self.menu_buttons_frame.setObjectName(u"menu_buttons_frame")
        self.menu_buttons_frame.setGeometry(QRect(0, 0, 891, 43))
        self.menu_buttons_frame.setStyleSheet(u"QFrame{\n"
"border-bottom: 1px solid #dadada;\n"
"}")
        self.menu_buttons_frame.setFrameShape(QFrame.StyledPanel)
        self.menu_buttons_frame.setFrameShadow(QFrame.Raised)
        self.math_symbol_button = QPushButton(self.menu_buttons_frame)
        self.math_symbol_button.setObjectName(u"math_symbol_button")
        self.math_symbol_button.setGeometry(QRect(5, 0, 41, 41))
        self.math_symbol_button.setMaximumSize(QSize(50, 16777215))
        self.math_symbol_button.setFont(font)
        self.math_symbol_button.setStyleSheet(u"QPushButton:hover {\n"
"	background-color: rgb(56, 57, 61);\n"
"}\n"
"QToolTip{color: white;}\n"
"")
        icon3 = QIcon()
        icon3.addFile(u"images/calculate.png", QSize(), QIcon.Normal, QIcon.Off)
        icon3.addFile(u"../images/calculate.png", QSize(), QIcon.Normal, QIcon.On)
        self.math_symbol_button.setIcon(icon3)
        self.math_symbol_button.setIconSize(QSize(40, 40))
        self.math_symbol_button.setCheckable(True)
        self.math_symbol_button.setChecked(False)
        self.tooltip_label = QLabel(self.menu_buttons_frame)
        self.tooltip_label.setObjectName(u"tooltip_label")
        self.tooltip_label.setGeometry(QRect(550, 0, 331, 41))
        self.tooltip_label.setLayoutDirection(Qt.LeftToRight)
        self.tooltip_label.setStyleSheet(u"QLabel{\n"
"\n"
"border-bottom: 0px;\n"
"\n"
"color:rgb(214, 214, 214);\n"
"\n"
"}")
        self.tooltip_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.add_text_input_btn = QPushButton(self.menu_buttons_frame)
        self.add_text_input_btn.setObjectName(u"add_text_input_btn")
        self.add_text_input_btn.setGeometry(QRect(50, 0, 41, 41))
        self.add_text_input_btn.setStyleSheet(u"QPushButton:hover{background-color:rgb(56, 57, 61);}\n"
"QToolTip{color: white;}\n"
"QPushButton{border-radius: 10px;}")
        icon4 = QIcon()
        icon4.addFile(u"../images/new.png", QSize(), QIcon.Normal, QIcon.Off)
        self.add_text_input_btn.setIcon(icon4)
        self.add_text_input_btn.setIconSize(QSize(41, 41))
        self.delete_all_btn = QPushButton(self.menu_buttons_frame)
        self.delete_all_btn.setObjectName(u"delete_all_btn")
        self.delete_all_btn.setGeometry(QRect(95, 0, 41, 41))
        self.delete_all_btn.setStyleSheet(u"QPushButton:hover{background-color:rgb(56, 57, 61);}\n"
"QToolTip{color: white;}\n"
"QPushButton{border-radius: 10px;}")
        icon5 = QIcon()
        icon5.addFile(u"../images/baseline_delete_white_36dp.png", QSize(), QIcon.Normal, QIcon.Off)
        icon5.addFile(u"../images/outline_close_white_48dp.png", QSize(), QIcon.Normal, QIcon.On)
        self.delete_all_btn.setIcon(icon5)
        self.delete_all_btn.setIconSize(QSize(41, 41))
        self.help_btn = QPushButton(self.menu_buttons_frame)
        self.help_btn.setObjectName(u"help_btn")
        self.help_btn.setGeometry(QRect(138, 0, 41, 41))
        self.help_btn.setStyleSheet(u"QPushButton:hover{background-color:rgb(56, 57, 61);}\n"
"QToolTip{color: white;}\n"
"QPushButton{border-radius: 10px;}")
        icon6 = QIcon()
        icon6.addFile(u"../images/outline_help_white_48dp.png", QSize(), QIcon.Normal, QIcon.Off)
        self.help_btn.setIcon(icon6)
        self.help_btn.setIconSize(QSize(38, 38))
        self.input_edit = QLineEdit(self.top_menu_frame)
        self.input_edit.setObjectName(u"input_edit")
        self.input_edit.setGeometry(QRect(10, 124, 871, 25))
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.input_edit.sizePolicy().hasHeightForWidth())
        self.input_edit.setSizePolicy(sizePolicy)
        self.input_edit.setMinimumSize(QSize(871, 25))
        self.input_edit.setMaximumSize(QSize(871, 25))
        self.input_edit.setStyleSheet(u"QLineEdit{border:2px solid;\n"
"\n"
"border-color:rgb(214, 214, 214);\n"
"background-color: rgb(81, 85, 93);\n"
"color:rgb(214, 214, 214);}")
        self.input_edit.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_2.addWidget(self.top_menu_frame)

        self.input_scroll = QScrollArea(self.main_frame)
        self.input_scroll.setObjectName(u"input_scroll")
        self.input_scroll.setStyleSheet(u"border-width: 0px;")
        self.input_scroll.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 894, 795))
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(9, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.scrollAreaWidgetContents)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"border-radius: 0px;")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.horizontalLayout = QHBoxLayout(self.page)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, -1, -1, -1)
        self.output_frame = QFrame(self.page)
        self.output_frame.setObjectName(u"output_frame")
        self.output_frame.setMinimumSize(QSize(700, 0))
        self.output_frame.setStyleSheet(u"QFrame{border:2px solid;\n"
"\n"
"border-color:rgb(214, 214, 214);\n"
"background-color: rgb(81, 85, 93);\n"
"color:rgb(214, 214, 214);}")
        self.output_frame.setFrameShape(QFrame.StyledPanel)
        self.output_frame.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.output_frame)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.stackedWidget.addWidget(self.page_2)

        self.verticalLayout_3.addWidget(self.stackedWidget)

        self.input_scroll.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.input_scroll)


        self.verticalLayout.addWidget(self.main_frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionNew.setText(QCoreApplication.translate("MainWindow", u"New...", None))
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"Open...", None))
        self.actionClose.setText(QCoreApplication.translate("MainWindow", u"Close", None))
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.actionSave_As.setText(QCoreApplication.translate("MainWindow", u"Save As..", None))
        self.actionSave_Images.setText(QCoreApplication.translate("MainWindow", u"Save Plots..", None))
        self.actionQuit.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.actionUndo.setText(QCoreApplication.translate("MainWindow", u"Undo", None))
        self.actionRedo.setText(QCoreApplication.translate("MainWindow", u"Redo", None))
        self.actionCut.setText(QCoreApplication.translate("MainWindow", u"Cut", None))
        self.actionCopy.setText(QCoreApplication.translate("MainWindow", u"Copy", None))
        self.actionpaste.setText(QCoreApplication.translate("MainWindow", u"Paste", None))
        self.actionDelete.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.actionSelect_All.setText(QCoreApplication.translate("MainWindow", u"Select All", None))
        self.actionEdit.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.actionblah_blah.setText(QCoreApplication.translate("MainWindow", u"blah blah", None))
        self.actionstuff.setText(QCoreApplication.translate("MainWindow", u"stuff", None))
        self.actionstuff_2.setText(QCoreApplication.translate("MainWindow", u"stuff", None))
        self.minBtn.setText("")
        self.closeBtn.setText("")
        self.title_label.setText(QCoreApplication.translate("MainWindow", u"Math Visualisation", None))
        self.window_icon.setText("")
        self.math_symbol_button.setText("")
        self.tooltip_label.setText("")
        self.add_text_input_btn.setText("")
        self.delete_all_btn.setText("")
        self.help_btn.setText("")
    # retranslateUi


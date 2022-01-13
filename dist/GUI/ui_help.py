# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'helpiGbpGv.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import image_rsc_rc

class Ui_Help(object):
    def setupUi(self, Help):
        if not Help.objectName():
            Help.setObjectName(u"Help")
        Help.resize(900, 900)
        Help.setMinimumSize(QSize(900, 900))
        Help.setMaximumSize(QSize(900, 900))
        Help.setStyleSheet(u"QMainWindow{\n"
"	background-color: rgb(32, 36, 38);\n"
"}")
        self.actionNew = QAction(Help)
        self.actionNew.setObjectName(u"actionNew")
        self.actionOpen = QAction(Help)
        self.actionOpen.setObjectName(u"actionOpen")
        self.actionClose = QAction(Help)
        self.actionClose.setObjectName(u"actionClose")
        self.actionSave = QAction(Help)
        self.actionSave.setObjectName(u"actionSave")
        self.actionSave_As = QAction(Help)
        self.actionSave_As.setObjectName(u"actionSave_As")
        self.actionSave_Images = QAction(Help)
        self.actionSave_Images.setObjectName(u"actionSave_Images")
        self.actionQuit = QAction(Help)
        self.actionQuit.setObjectName(u"actionQuit")
        self.actionUndo = QAction(Help)
        self.actionUndo.setObjectName(u"actionUndo")
        self.actionRedo = QAction(Help)
        self.actionRedo.setObjectName(u"actionRedo")
        self.actionCut = QAction(Help)
        self.actionCut.setObjectName(u"actionCut")
        self.actionCopy = QAction(Help)
        self.actionCopy.setObjectName(u"actionCopy")
        self.actionpaste = QAction(Help)
        self.actionpaste.setObjectName(u"actionpaste")
        self.actionDelete = QAction(Help)
        self.actionDelete.setObjectName(u"actionDelete")
        self.actionSelect_All = QAction(Help)
        self.actionSelect_All.setObjectName(u"actionSelect_All")
        self.centralwidget = QWidget(Help)
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
        self.title_label.setGeometry(QRect(402, 7, 91, 31))
        font = QFont()
        font.setFamily(u"Microsoft PhagsPa")
        font.setPointSize(10)
        self.title_label.setFont(font)
        self.title_label.setStyleSheet(u"color:rgb(214, 214, 214);")
        self.title_label.setAlignment(Qt.AlignCenter)
        self.return_button = QPushButton(self.headerFrame)
        self.return_button.setObjectName(u"return_button")
        self.return_button.setGeometry(QRect(12, 7, 31, 31))
        self.return_button.setStyleSheet(u"QPushButton:hover {\n"
"	background-color: rgb(56, 57, 61);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u"../images/undo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.return_button.setIcon(icon2)
        self.return_button.setIconSize(QSize(28, 28))

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
        self.input_scroll = QScrollArea(self.main_frame)
        self.input_scroll.setObjectName(u"input_scroll")
        self.input_scroll.setStyleSheet(u"border-width: 0px;")
        self.input_scroll.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 894, 845))
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
        self.help_main_frame = QFrame(self.page)
        self.help_main_frame.setObjectName(u"help_main_frame")
        self.help_main_frame.setStyleSheet(u"QFrame{border:2px solid;\n"
"\n"
"border-color:rgb(214, 214, 214);\n"
"background-color: rgb(81, 85, 93);\n"
"color:rgb(214, 214, 214);}")
        self.help_main_frame.setFrameShape(QFrame.StyledPanel)
        self.help_main_frame.setFrameShadow(QFrame.Raised)
        self.textEdit = QTextEdit(self.help_main_frame)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(10, 10, 856, 808))
        self.textEdit.setReadOnly(True)

        self.horizontalLayout.addWidget(self.help_main_frame)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.stackedWidget.addWidget(self.page_2)

        self.verticalLayout_3.addWidget(self.stackedWidget)

        self.input_scroll.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.input_scroll)


        self.verticalLayout.addWidget(self.main_frame)

        Help.setCentralWidget(self.centralwidget)

        self.retranslateUi(Help)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Help)
    # setupUi

    def retranslateUi(self, Help):
        Help.setWindowTitle(QCoreApplication.translate("Help", u"MainWindow", None))
        self.actionNew.setText(QCoreApplication.translate("Help", u"New...", None))
        self.actionOpen.setText(QCoreApplication.translate("Help", u"Open...", None))
        self.actionClose.setText(QCoreApplication.translate("Help", u"Close", None))
        self.actionSave.setText(QCoreApplication.translate("Help", u"Save", None))
        self.actionSave_As.setText(QCoreApplication.translate("Help", u"Save As..", None))
        self.actionSave_Images.setText(QCoreApplication.translate("Help", u"Save Plots..", None))
        self.actionQuit.setText(QCoreApplication.translate("Help", u"Quit", None))
        self.actionUndo.setText(QCoreApplication.translate("Help", u"Undo", None))
        self.actionRedo.setText(QCoreApplication.translate("Help", u"Redo", None))
        self.actionCut.setText(QCoreApplication.translate("Help", u"Cut", None))
        self.actionCopy.setText(QCoreApplication.translate("Help", u"Copy", None))
        self.actionpaste.setText(QCoreApplication.translate("Help", u"Paste", None))
        self.actionDelete.setText(QCoreApplication.translate("Help", u"Delete", None))
        self.actionSelect_All.setText(QCoreApplication.translate("Help", u"Select All", None))
        self.minBtn.setText("")
        self.closeBtn.setText("")
        self.title_label.setText(QCoreApplication.translate("Help", u"Help", None))
        self.return_button.setText("")
        self.textEdit.setHtml(QCoreApplication.translate("Help", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:600; text-decoration: underline;\">User Interface Navigation</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600;\">- Commands</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0p"
                        "x; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">-help</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">-clear</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">-graph</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">-solve</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">-integrate</span></p>\n"
""
                        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">-differentiate</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">-zero</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">-function *</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">-3d *</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style="
                        "\" font-size:11pt;\">* - has to be prefixed by '-graph '</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">You can just copy/paste these functions into the text inputs if you wish.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">All graphs can be saved as images by clicking the save icon inside the graph widget.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:"
                        "0px; -qt-block-indent:0; text-indent:0px; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">Example Graphed Function of 2 variables (x, y):</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">3D graphs can be rotated in any plane by clicking and dragging on the graph.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">- Supported functions: log() sin() cos() tan() sqrt()</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600;\">' </span><a name=\"chat-messages-930047956051169292\"></a><span style=\" font-family:'Consola"
                        "s','Andale Mono WT','Andale Mono','Lucida Console','Lucida Sans Typewriter','DejaVu Sans Mono','Bitstream Vera Sans Mono','Liberation Mono','Nimbus Mono L','Monaco','Courier New','Courier','monospace'; font-size:8pt; font-weight:600; color:#000000;\">-</span><span style=\" font-family:'Consolas','Andale Mono WT','Andale Mono','Lucida Console','Lucida Sans Typewriter','DejaVu Sans Mono','Bitstream Vera Sans Mono','Liberation Mono','Nimbus Mono L','Monaco','Courier New','Courier','monospace'; font-size:8pt; font-weight:600; color:#000000;\">graph -3d sin(x) * sin(y)</span><span style=\" font-size:11pt; font-weight:600;\">'</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600;\">' </span><a name=\"chat-messages-930047956051169292\"></a><span style=\" font-family:'Consolas','Andale Mono WT','Andale Mono','Lucida Console','Lucida Sans Typewriter','DejaVu Sans Mono','Bitstream Vera Sans M"
                        "ono','Liberation Mono','Nimbus Mono L','Monaco','Courier New','Courier','monospace'; font-size:8pt; font-weight:600; color:#000000;\">-</span><span style=\" font-family:'Consolas','Andale Mono WT','Andale Mono','Lucida Console','Lucida Sans Typewriter','DejaVu Sans Mono','Bitstream Vera Sans Mono','Liberation Mono','Nimbus Mono L','Monaco','Courier New','Courier','monospace'; font-size:8pt; font-weight:600; color:#000000;\">graph -3d log(y) * sin(x) - 2*x</span><span style=\" font-size:11pt; font-weight:600;\">'</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">Example Graphed Functions of x:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-inden"
                        "t:0; text-indent:0px;\"><span style=\" font-size:11pt;\">- Supported functions of x: log() ln() sin() cos() tan() sqrt()</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600;\">' </span><a name=\"chat-messages-930047956051169292\"></a><span style=\" font-family:'Consolas','Andale Mono WT','Andale Mono','Lucida Console','Lucida Sans Typewriter','DejaVu Sans Mono','Bitstream Vera Sans Mono','Liberation Mono','Nimbus Mono L','Monaco','Courier New','Courier','monospace'; font-size:8pt; font-weight:600; color:#000000;\">-</span><span style=\" font-family:'Consolas','Andale Mono WT','Andale Mono','Lucida Console','Lucida Sans Typewriter','DejaVu Sans Mono','Bitstream Vera Sans Mono','Liberation Mono','Nimbus Mono L','Monaco','Courier New','Courier','monospace'; font-size:8pt; font-weight:600; color:#000000;\">graph -function log(x)</span><span style=\" font-size:11pt; font-weight:600;\">'"
                        "</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600;\">' </span><a name=\"chat-messages-930047956051169292\"></a><span style=\" font-family:'Consolas','Andale Mono WT','Andale Mono','Lucida Console','Lucida Sans Typewriter','DejaVu Sans Mono','Bitstream Vera Sans Mono','Liberation Mono','Nimbus Mono L','Monaco','Courier New','Courier','monospace'; font-size:8pt; font-weight:600; color:#000000;\">-</span><span style=\" font-family:'Consolas','Andale Mono WT','Andale Mono','Lucida Console','Lucida Sans Typewriter','DejaVu Sans Mono','Bitstream Vera Sans Mono','Liberation Mono','Nimbus Mono L','Monaco','Courier New','Courier','monospace'; font-size:8pt; font-weight:600; color:#000000;\">graph -function x**3</span><span style=\" font-size:11pt; font-weight:600;\">'</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text"
                        "-indent:0px;\"><span style=\" font-size:11pt; font-weight:600;\">' </span><a name=\"chat-messages-930047956051169292\"></a><span style=\" font-family:'Consolas','Andale Mono WT','Andale Mono','Lucida Console','Lucida Sans Typewriter','DejaVu Sans Mono','Bitstream Vera Sans Mono','Liberation Mono','Nimbus Mono L','Monaco','Courier New','Courier','monospace'; font-size:8pt; font-weight:600; color:#000000;\">-</span><span style=\" font-family:'Consolas','Andale Mono WT','Andale Mono','Lucida Console','Lucida Sans Typewriter','DejaVu Sans Mono','Bitstream Vera Sans Mono','Liberation Mono','Nimbus Mono L','Monaco','Courier New','Courier','monospace'; font-size:8pt; font-weight:600; color:#000000;\">graph -function 2*x+1</span><span style=\" font-size:11pt; font-weight:600;\">'</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Consolas','Andale Mono WT','Andale Mono','Lucida Console','Lucida Sans"
                        " Typewriter','DejaVu Sans Mono','Bitstream Vera Sans Mono','Liberation Mono','Nimbus Mono L','Monaco','Courier New','Courier','monospace'; font-size:8pt; font-weight:600; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">Example Solve Quadratic Equation of x (returns positive and negative solution for x):</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600;\">'</span><span style=\" font-family:'Consolas','Andale Mono WT','Andale Mono','Lucida Console','Lucida Sans Typewriter','DejaVu Sans Mono','Bitstream Vera Sans Mono','Liberation Mono','Nimbus Mono L','Monaco','Courier New','Courier','monospace'; font-size:8pt; font-weight:600; color:#000000;\">-solve 5*x**2 + 6*x + 10</span><span style=\" font-size:11pt; font-weight:600;\">'</span></p>\n"
"<p s"
                        "tyle=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Consolas','Andale Mono WT','Andale Mono','Lucida Console','Lucida Sans Typewriter','DejaVu Sans Mono','Bitstream Vera Sans Mono','Liberation Mono','Nimbus Mono L','Monaco','Courier New','Courier','monospace'; font-size:8pt; font-weight:600; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">Example Zero Cross Polynomial:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600;\">'</span><a name=\"chat-messages-930047956051169292\"></a><span style=\" font-family:'Consolas','Andale Mono WT','Andale Mono','Lucida Console','Lucida Sans Typewriter','DejaVu Sans Mono','Bitstream Vera Sans Mono','Liberation Mo"
                        "no','Nimbus Mono L','Monaco','Courier New','Courier','monospace'; font-size:8pt; font-weight:600; color:#000000;\">-</span><span style=\" font-family:'Consolas','Andale Mono WT','Andale Mono','Lucida Console','Lucida Sans Typewriter','DejaVu Sans Mono','Bitstream Vera Sans Mono','Liberation Mono','Nimbus Mono L','Monaco','Courier New','Courier','monospace'; font-size:8pt; font-weight:600; color:#000000;\">graph -zero axis=x degree=2 function=10*x**2+10*x-10</span><span style=\" font-size:11pt; font-weight:600;\">'</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600;\">'</span><a name=\"chat-messages-930047956051169292\"></a><span style=\" font-family:'Consolas','Andale Mono WT','Andale Mono','Lucida Console','Lucida Sans Typewriter','DejaVu Sans Mono','Bitstream Vera Sans Mono','Liberation Mono','Nimbus Mono L','Monaco','Courier New','Courier','monospace'; font-size:8pt; font-weigh"
                        "t:600; color:#000000;\">-</span><span style=\" font-family:'Consolas','Andale Mono WT','Andale Mono','Lucida Console','Lucida Sans Typewriter','DejaVu Sans Mono','Bitstream Vera Sans Mono','Liberation Mono','Nimbus Mono L','Monaco','Courier New','Courier','monospace'; font-size:8pt; font-weight:600; color:#000000;\">graph -zero axis=y degree=2 function=10*x**2+10*x-10</span><span style=\" font-size:11pt; font-weight:600;\">'</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">Example Differentiate:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600;\">'</span><a name=\"chat-messages-930047741"
                        "298622464\"></a><span style=\" font-family:'Consolas','Andale Mono WT','Andale Mono','Lucida Console','Lucida Sans Typewriter','DejaVu Sans Mono','Bitstream Vera Sans Mono','Liberation Mono','Nimbus Mono L','Monaco','Courier New','Courier','monospace'; font-size:8pt; font-weight:600; color:#000000;\">-</span><span style=\" font-family:'Consolas','Andale Mono WT','Andale Mono','Lucida Console','Lucida Sans Typewriter','DejaVu Sans Mono','Bitstream Vera Sans Mono','Liberation Mono','Nimbus Mono L','Monaco','Courier New','Courier','monospace'; font-size:8pt; font-weight:600; color:#000000;\">differentiate 3*x**3-1*x**2+6</span><span style=\" font-size:11pt; font-weight:600;\">'</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11p"
                        "t;\">Example Graphed Differentiate:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600;\">'</span><a name=\"chat-messages-930047849796890654\"></a><span style=\" font-family:'Consolas','Andale Mono WT','Andale Mono','Lucida Console','Lucida Sans Typewriter','DejaVu Sans Mono','Bitstream Vera Sans Mono','Liberation Mono','Nimbus Mono L','Monaco','Courier New','Courier','monospace'; font-size:8pt; font-weight:600; color:#000000;\">-</span><span style=\" font-family:'Consolas','Andale Mono WT','Andale Mono','Lucida Console','Lucida Sans Typewriter','DejaVu Sans Mono','Bitstream Vera Sans Mono','Liberation Mono','Nimbus Mono L','Monaco','Courier New','Courier','monospace'; font-size:8pt; font-weight:600; color:#000000;\">graph </span><a name=\"chat-messages-930047741298622464\"></a><span style=\" font-family:'Consolas','Andale Mono WT','Andale Mono','Lucida Console','Lucida Sans Typew"
                        "riter','DejaVu Sans Mono','Bitstream Vera Sans Mono','Liberation Mono','Nimbus Mono L','Monaco','Courier New','Courier','monospace'; font-size:8pt; font-weight:600; color:#000000;\">-</span><span style=\" font-family:'Consolas','Andale Mono WT','Andale Mono','Lucida Console','Lucida Sans Typewriter','DejaVu Sans Mono','Bitstream Vera Sans Mono','Liberation Mono','Nimbus Mono L','Monaco','Courier New','Courier','monospace'; font-size:8pt; font-weight:600; color:#000000;\">differentiate 3*x**3-1*x**2+6</span><span style=\" font-size:11pt; font-weight:600;\">'</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">Example Integration:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px"
                        "; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600;\">'</span><a name=\"chat-messages-930045998976364555\"></a><span style=\" font-family:'Consolas','Andale Mono WT','Andale Mono','Lucida Console','Lucida Sans Typewriter','DejaVu Sans Mono','Bitstream Vera Sans Mono','Liberation Mono','Nimbus Mono L','Monaco','Courier New','Courier','monospace'; font-size:8pt; font-weight:600; color:#000000;\">-</span><span style=\" font-family:'Consolas','Andale Mono WT','Andale Mono','Lucida Console','Lucida Sans Typewriter','DejaVu Sans Mono','Bitstream Vera Sans Mono','Liberation Mono','Nimbus Mono L','Monaco','Courier New','Courier','monospace'; font-size:8pt; font-weight:600; color:#000000;\">integrate 3*x**3-1*x**2+6</span><span style=\" font-size:11pt; font-weight:600;\">'</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt;\"><br /></p>\n"
"<p "
                        "style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">Example Graphed Integration:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600;\">'</span><a name=\"chat-messages-930047849796890654\"></a><span style=\" font-family:'Consolas','Andale Mono WT','Andale Mono','Lucida Console','Lucida Sans Typewriter','DejaVu Sans Mono','Bitstream Vera Sans Mono','Liberation Mono','Nimbus Mono L','Monaco','Courier New','Courier','monospace'; font-size:8pt; font-weight:600; color:#000000;\">-</span><span style=\" font-family:'Consolas','Andale Mono WT','Andale Mono','Lucida Console','Lucida Sans Typewriter','DejaVu Sans Mono','Bitstream Vera Sans Mono','Liberation Mono','Nimbus Mono L','Monaco','Courier New','Courier','monospace'; font-size:8pt; font-weight:600; color:#000000;\">graph -integrate 3*x**"
                        "3-1*x**2+6 '</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600;\">- Shortcuts</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">CTRL + N - New Input Cell</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">CTRL + H - Open Help Menu</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-to"
                        "p:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600;\">Splash Window</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">Clicking on '</span><span style=\" font-size:11pt; font-style:italic;\">new </span><span style=\" font-size:11pt;\">' will alllow you to create a new instance of the notebook, clicking '</span><span style=\" font-size:11pt; font-style:italic;\">exit </span><span style=\" font-size:11pt;\">' will exit the program.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt;\"><br />"
                        "</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600;\">-----------</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/images/stylesheets/images/splashScreen.png\" /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px;"
                        " margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600;\">-----------</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600;\">Main Window</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-i"
                        "ndent:0px;\"><span style=\" font-size:11pt; font-weight:600;\">-----------</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/images/stylesheets/images/menuBar.png\" /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600;\">-----------</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt; font-weight:600;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt; font-weight:600;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-"
                        "left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">The menu bar on the top contains three key buttons.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600;\">Renderer</span><span style=\" font-size:11pt;\">: Clicking it once will expand and reveal a textbox that you can input text into a latex renderer, clicking it again will close it</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span sty"
                        "le=\" font-size:11pt; font-weight:600;\">Add</span><span style=\" font-size:11pt;\"> </span><span style=\" font-size:11pt; font-weight:600;\">Cell</span><span style=\" font-size:11pt;\">: Add a cell to your current notebook</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600;\">Remove</span><span style=\" font-size:11pt;\"> </span><span style=\" font-size:11pt; font-weight:600;\">Cell</span><span style=\" font-size:11pt;\">: Clear the contents of the notebook</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">The tooltip on the far left of the menu bar gives helpful tips that can help whilst "
                        "using the navigation. This consists of what to do next and any errors that might be present in the cells that you are working on.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600;\">Error Types</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">When you encounter an error, the tool tip will change and the cell with an error will be highlighted in red.</span></p>\n"
"<p style=\"-qt-paragraph-type:emp"
                        "ty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600;\">-----------</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/images/stylesheets/images/menuBar_error.png\" /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-b"
                        "lock-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600;\">-----------</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt; font-weight:600;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt; font-weight:600;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">There are multiple errors you can encounter when typing in the cells, here are some of them.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px"
                        "; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600;\">Invalid Syntax</span><span style=\" font-size:11pt;\">: The syntax that you have entered in the cell does not meet the language requirements of the program</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600;\">Invalid Operation</span><span style=\" font-size:11pt;\">: You have tried to do a mathematical operation that is not possible</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600;\">Invalid Character</span><span style=\" font-size:11pt;\">: The character you have entered doe"
                        "s not match the logical flow of the syntax</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:600; text-decoration: underline;\">Syntax</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:18pt; font-weight:600; text-decoration: underline;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">Within each 'cell' of the program there are cert"
                        "ian rules that must be followed. These are the syntactical rules of the program. The renderer is seperated from this as this must follow the rules of latex in order to render your equation.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">The syntax is straight forward and will accept any basic mathematical input that would be allowed on a calculator. This includes the usage of brackets. </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-siz"
                        "e:11pt;\">Here is a basic syntax list:</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">+ Addition/Plus/Positive</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">- Substraction/Minus/Negative</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">* Multiplication</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">/ Division</span></p>\n"
"<p style=\"-qt-paragraph-type:empty"
                        "; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600;\">-----------</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/images/stylesheets/images/exampleBasicCalc.png\" /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-"
                        "block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600;\">-----------</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt; font-weight:600;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt; font-weight:600;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">Example Calculation:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-"
                        "size:11pt;\">' </span><span style=\" font-family:'Consolas','Andale Mono WT','Andale Mono','Lucida Console','Lucida Sans Typewriter','DejaVu Sans Mono','Bitstream Vera Sans Mono','Liberation Mono','Nimbus Mono L','Monaco','Courier New','Courier','monospace'; font-size:8pt; font-weight:600; color:#000000;\">(100+20)*200+1-9231.1</span><span style=\" font-size:11pt;\"> '</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600;\">Advanced Syntax</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; m"
                        "argin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">Whilst you can run calculations on the program that are fairly basic, you also are able to run commands to plot graphs and help differentiate, intergrate as well as plot the zero crossing of a polynomial. You are also able to graph the commands buy adding ' -graph' infront of the command as shown below.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; marg"
                        "in-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600;\">-----------</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/images/stylesheets/images/exampleAdvCalc.png\" /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600;\">-----------</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt; font-weight:600;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt; font-weight:600;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom"
                        ":0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">Example Zero Cross Polynomial:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600;\">' </span><a name=\"chat-messages-930047956051169292\"></a><span style=\" font-family:'Consolas','Andale Mono WT','Andale Mono','Lucida Console','Lucida Sans Typewriter','DejaVu Sans Mono','Bitstream Vera Sans Mono','Liberation Mono','Nimbus Mono L','Monaco','Courier New','Courier','monospace'; font-size:8pt; font-weight:600; color:#000000;\">-</span><span style=\" font-family:'Consolas','Andale Mono WT','Andale Mono','Lucida Console','Lucida Sans Typewriter','DejaVu Sans Mono','Bitstream Vera Sans Mono','Liberation Mono'"
                        ",'Nimbus Mono L','Monaco','Courier New','Courier','monospace'; font-size:8pt; font-weight:600; color:#000000;\">graph -zero axis=x degree=2 function=10*x**2+10*x-10'</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">Example Differentiate:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600;\">' </span><a name=\"chat-messages-930047741298622464\"></a><span style=\" font-family:'Consolas','Andale Mono WT','Andale Mono','Lucida Console','Lucida Sans Typewriter','DejaVu Sans Mono','Bitstream Vera Sans Mono','Liberation Mono','Nimbus Mono L','Monaco','Courier New','Courier','monospace'; font-size"
                        ":8pt; font-weight:600; color:#000000;\">-</span><span style=\" font-family:'Consolas','Andale Mono WT','Andale Mono','Lucida Console','Lucida Sans Typewriter','DejaVu Sans Mono','Bitstream Vera Sans Mono','Liberation Mono','Nimbus Mono L','Monaco','Courier New','Courier','monospace'; font-size:8pt; font-weight:600; color:#000000;\">differentiate 3*x**3-1*x**2+6 '</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">Example Integration:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600;\">' </span><a name=\"chat-messages-930045998976364555\"></a><span style=\" font-family:'Consolas','Andale Mo"
                        "no WT','Andale Mono','Lucida Console','Lucida Sans Typewriter','DejaVu Sans Mono','Bitstream Vera Sans Mono','Liberation Mono','Nimbus Mono L','Monaco','Courier New','Courier','monospace'; font-size:8pt; font-weight:600; color:#000000;\">-</span><span style=\" font-family:'Consolas','Andale Mono WT','Andale Mono','Lucida Console','Lucida Sans Typewriter','DejaVu Sans Mono','Bitstream Vera Sans Mono','Liberation Mono','Nimbus Mono L','Monaco','Courier New','Courier','monospace'; font-size:8pt; font-weight:600; color:#000000;\">integrate 3*x**3-1*x**2+6 '</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">Once again, you are able to insert the ' -graph ' command to plot the outcomes.</span></p>\n"
"<p style=\"-qt-paragraph"
                        "-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">Example Graphed Integration:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600;\">' </span><a name=\"chat-messages-930047849796890654\"></a><span style=\" font-family:'Consolas','Andale Mono WT','Andale Mono','Lucida Console','Lucida Sans Typewriter','DejaVu Sans Mono','Bitstream Vera Sans Mono','Liberation Mono','Nimbus Mono L','Monaco','Courier New','Courier','monospace'; font-size:8pt; font-weight:600; color:#000000;\">-</span><span style=\" font-family:'Consolas','Andale Mono WT','Andale Mono','Lucida Console','Lucida Sans Typewriter','DejaVu Sans Mono','Bitstream Vera Sans "
                        "Mono','Liberation Mono','Nimbus Mono L','Monaco','Courier New','Courier','monospace'; font-size:8pt; font-weight:600; color:#000000;\">graph -integrate 3*x**3-1*x**2+6 '</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600;\">Utility Syntax</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-"
                        "indent:0px;\"><span style=\" font-size:11pt;\">Whilst you can use the GUI to help you access key areas, you are also able to use the cells to quickly navigate to where you need to go to. There are commands avaliable like so:</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">' </span><a name=\"chat-messages-930047956051169292\"></a><span style=\" font-family:'Consolas','Andale Mono WT','Andale Mono','Lucida Console','Lucida Sans Typewriter','DejaVu Sans Mono','Bitstream Vera Sans Mono','Liberation Mono','Nimbus Mono L','Monaco','Courier New','Courier','monospace'; font-size:8pt; font-weight:600; color:#000000;\">-</span><span style=\" font-family:'Consolas','Andale Mono WT','Andale Mono','Lucida Console','Lucida Sans Typ"
                        "ewriter','DejaVu Sans Mono','Bitstream Vera Sans Mono','Liberation Mono','Nimbus Mono L','Monaco','Courier New','Courier','monospace'; font-size:8pt; font-weight:600; color:#000000;\">clear</span><span style=\" font-size:11pt;\"> ' : Clears the cells currently on the program</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">' </span><a name=\"chat-messages-930047956051169292\"></a><span style=\" font-family:'Consolas','Andale Mono WT','Andale Mono','Lucida Console','Lucida Sans Typewriter','DejaVu Sans Mono','Bitstream Vera Sans Mono','Liberation Mono','Nimbus Mono L','Monaco','Courier New','Courier','monospace'; font-size:8pt; font-weight:600; color:#000000;\">-</span><span style=\" font-family:'Consolas','Andale Mono WT','Andale Mono','Lucida Console','Lucida Sans Typewriter','DejaVu Sans Mono','Bitstream Vera Sans Mono','Liberation Mono','Nimbus Mono L','Monaco','Courier New','Courier','mon"
                        "ospace'; font-size:8pt; font-weight:600; color:#000000;\">help</span><span style=\" font-size:11pt;\"> ' : Bring up the help menu</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600;\">Keyboard Shortcuts</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">' </span><span style=\" font-family:'Consolas','Andale Mono WT','Andale Mono','Lucida Console','Lucida Sans Typewriter','DejaVu Sans Mono','Bitstream "
                        "Vera Sans Mono','Liberation Mono','Nimbus Mono L','Monaco','Courier New','Courier','monospace'; font-size:8pt; font-weight:600; color:#000000;\">CTRL+N</span><span style=\" font-size:11pt;\"> ' : Create a new cell</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:600; text-decoration: underline;\">Console Mode</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">The program is designed to be run via console as well for qu"
                        "ick usage and application for those who are more fimiliar with the command-line.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600;\">-----------</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/images/stylesheets/images/exampleConsoleBasicCalc.png\" /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><spa"
                        "n style=\" font-size:11pt; font-weight:600;\">-----------</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt; font-weight:600;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600;\">Usage</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">Console mode works via d"
                        "ifferent arguments passed onto it. The prefix being the program name with the arguments being the following (excluding the quotation marks):</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">' </span><span style=\" font-family:'Consolas','Andale Mono WT','Andale Mono','Lucida Console','Lucida Sans Typewriter','DejaVu Sans Mono','Bitstream Vera Sans Mono','Liberation Mono','Nimbus Mono L','Monaco','Courier New','Courier','monospace'; font-size:8pt; font-weight:600; color:#000000;\">(100+20)*200+1-9231.1</span><span style=\" font-size:11pt;\"> ' : Run normal calculations</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" fo"
                        "nt-size:11pt;\">' </span><a name=\"chat-messages-930047956051169292\"></a><span style=\" font-family:'Consolas','Andale Mono WT','Andale Mono','Lucida Console','Lucida Sans Typewriter','DejaVu Sans Mono','Bitstream Vera Sans Mono','Liberation Mono','Nimbus Mono L','Monaco','Courier New','Courier','monospace'; font-size:8pt; font-weight:600; color:#000000;\">-</span><span style=\" font-family:'Consolas','Andale Mono WT','Andale Mono','Lucida Console','Lucida Sans Typewriter','DejaVu Sans Mono','Bitstream Vera Sans Mono','Liberation Mono','Nimbus Mono L','Monaco','Courier New','Courier','monospace'; font-size:8pt; font-weight:600; color:#000000;\">graph -zero</span><span style=\" font-size:11pt;\"> ' : Calculate the zero-crossing of a polynomial</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">' </span><a name=\"chat-messages-930047741298622464\"></a><span style=\" font-family:'Consolas','Andal"
                        "e Mono WT','Andale Mono','Lucida Console','Lucida Sans Typewriter','DejaVu Sans Mono','Bitstream Vera Sans Mono','Liberation Mono','Nimbus Mono L','Monaco','Courier New','Courier','monospace'; font-size:8pt; font-weight:600; color:#000000;\">-</span><span style=\" font-family:'Consolas','Andale Mono WT','Andale Mono','Lucida Console','Lucida Sans Typewriter','DejaVu Sans Mono','Bitstream Vera Sans Mono','Liberation Mono','Nimbus Mono L','Monaco','Courier New','Courier','monospace'; font-size:8pt; font-weight:600; color:#000000;\">diff</span><span style=\" font-size:11pt;\"> ' : Differentiate</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">' </span><a name=\"chat-messages-930045998976364555\"></a><span style=\" font-family:'Consolas','Andale Mono WT','Andale Mono','Lucida Console','Lucida Sans Typewriter','DejaVu Sans Mono','Bitstream Vera Sans Mono','Liberation Mono','Nimbus Mono L','Monaco'"
                        ",'Courier New','Courier','monospace'; font-size:8pt; font-weight:600; color:#000000;\">-</span><span style=\" font-family:'Consolas','Andale Mono WT','Andale Mono','Lucida Console','Lucida Sans Typewriter','DejaVu Sans Mono','Bitstream Vera Sans Mono','Liberation Mono','Nimbus Mono L','Monaco','Courier New','Courier','monospace'; font-size:8pt; font-weight:600; color:#000000;\">int</span><span style=\" font-size:11pt;\"> ' : Integrate</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">' </span><span style=\" font-family:'Consolas','Andale Mono WT','Andale Mono','Lucida Console','Lucida Sans Typewriter','DejaVu Sans Mono','Bitstream Vera Sans Mono','Liberation Mono','Nimbus Mono L','Monaco','Courier New','Courier','monospace'; font-size:8pt; font-weight:600; color:#000000;\">-3d</span><span style=\" font-size:11pt;\"> ' : Plot a function of two given variables</span></p>\n"
"<p style=\"-qt-parag"
                        "raph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">Then you are going to have to pass arguements to the questions that are asked for the appropriate output</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px;"
                        " margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600;\">-----------</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/images/stylesheets/images/exampleGraphZeroCalc.png\" /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600;\">-----------</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt; font-weight:600;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt; font-weight:600;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; ma"
                        "rgin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt; font-weight:600;\"><br /></p></body></html>", None))
    # retranslateUi


# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QMainWindow, QMenu,
    QMenuBar, QPlainTextEdit, QSizePolicy, QStatusBar,
    QTreeView, QVBoxLayout, QWidget)

from mplwidget import MplWidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1024, 662)
        MainWindow.setLayoutDirection(Qt.LeftToRight)
        MainWindow.setAutoFillBackground(False)
        self.actionOpen_Workfolder = QAction(MainWindow)
        self.actionOpen_Workfolder.setObjectName(u"actionOpen_Workfolder")
        self.actionProcessingMenu = QAction(MainWindow)
        self.actionProcessingMenu.setObjectName(u"actionProcessingMenu")
        self.actionSignalNavigation = QAction(MainWindow)
        self.actionSignalNavigation.setObjectName(u"actionSignalNavigation")
        self.actionDictionary_indexing = QAction(MainWindow)
        self.actionDictionary_indexing.setObjectName(u"actionDictionary_indexing")
        self.actionPattern_Center = QAction(MainWindow)
        self.actionPattern_Center.setObjectName(u"actionPattern_Center")
        self.actionROI = QAction(MainWindow)
        self.actionROI.setObjectName(u"actionROI")
        self.actionHough_indexing = QAction(MainWindow)
        self.actionHough_indexing.setObjectName(u"actionHough_indexing")
        self.actionPre_indexing_maps = QAction(MainWindow)
        self.actionPre_indexing_maps.setObjectName(u"actionPre_indexing_maps")
        self.actionSettings = QAction(MainWindow)
        self.actionSettings.setObjectName(u"actionSettings")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.systemViewerLayout = QVBoxLayout()
        self.systemViewerLayout.setObjectName(u"systemViewerLayout")
        self.folderLabel = QLabel(self.centralwidget)
        self.folderLabel.setObjectName(u"folderLabel")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.folderLabel.sizePolicy().hasHeightForWidth())
        self.folderLabel.setSizePolicy(sizePolicy)

        self.systemViewerLayout.addWidget(self.folderLabel)

        self.systemViewer = QTreeView(self.centralwidget)
        self.systemViewer.setObjectName(u"systemViewer")
        sizePolicy.setHeightForWidth(self.systemViewer.sizePolicy().hasHeightForWidth())
        self.systemViewer.setSizePolicy(sizePolicy)
        self.systemViewer.setMinimumSize(QSize(320, 320))
        self.systemViewer.setMouseTracking(False)
        self.systemViewer.setTabletTracking(True)
        self.systemViewer.setStyleSheet(u"")
        self.systemViewer.setEditTriggers(QAbstractItemView.AnyKeyPressed|QAbstractItemView.CurrentChanged|QAbstractItemView.DoubleClicked|QAbstractItemView.SelectedClicked)
        self.systemViewer.setTabKeyNavigation(True)
        self.systemViewer.setDragEnabled(False)
        self.systemViewer.setDragDropOverwriteMode(False)
        self.systemViewer.setAlternatingRowColors(False)
        self.systemViewer.setAnimated(True)
        self.systemViewer.header().setStretchLastSection(True)

        self.systemViewerLayout.addWidget(self.systemViewer)

        self.systemViewerLayout.setStretch(1, 1)

        self.horizontalLayout.addLayout(self.systemViewerLayout)

        self.MplWidget = MplWidget(self.centralwidget)
        self.MplWidget.setObjectName(u"MplWidget")
        sizePolicy.setHeightForWidth(self.MplWidget.sizePolicy().hasHeightForWidth())
        self.MplWidget.setSizePolicy(sizePolicy)
        self.MplWidget.setMinimumSize(QSize(320, 320))
        self.MplWidget.setAutoFillBackground(False)
        self.MplWidget.setStyleSheet(u"background-color: transparent")

        self.horizontalLayout.addWidget(self.MplWidget)

        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 3)

        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.consoleLog = QPlainTextEdit(self.centralwidget)
        self.consoleLog.setObjectName(u"consoleLog")
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.consoleLog.sizePolicy().hasHeightForWidth())
        self.consoleLog.setSizePolicy(sizePolicy1)

        self.verticalLayout_3.addWidget(self.consoleLog)

        self.inputLayout = QHBoxLayout()
        self.inputLayout.setObjectName(u"inputLayout")
        self.consolePrompt = QLabel(self.centralwidget)
        self.consolePrompt.setObjectName(u"consolePrompt")

        self.inputLayout.addWidget(self.consolePrompt)


        self.verticalLayout_3.addLayout(self.inputLayout)

        self.verticalLayout_3.setStretch(0, 1)

        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        self.verticalLayout_4.setStretch(0, 3)
        self.verticalLayout_4.setStretch(1, 1)

        self.gridLayout.addLayout(self.verticalLayout_4, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1024, 21))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuProcessing = QMenu(self.menubar)
        self.menuProcessing.setObjectName(u"menuProcessing")
        self.menuPlot = QMenu(self.menubar)
        self.menuPlot.setObjectName(u"menuPlot")
        self.menuDictionary_indexing = QMenu(self.menubar)
        self.menuDictionary_indexing.setObjectName(u"menuDictionary_indexing")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuProcessing.menuAction())
        self.menubar.addAction(self.menuPlot.menuAction())
        self.menubar.addAction(self.menuDictionary_indexing.menuAction())
        self.menuFile.addAction(self.actionOpen_Workfolder)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSettings)
        self.menuProcessing.addAction(self.actionProcessingMenu)
        self.menuProcessing.addAction(self.actionROI)
        self.menuProcessing.addAction(self.actionPattern_Center)
        self.menuPlot.addAction(self.actionSignalNavigation)
        self.menuPlot.addAction(self.actionPre_indexing_maps)
        self.menuDictionary_indexing.addAction(self.actionDictionary_indexing)
        self.menuDictionary_indexing.addAction(self.actionHough_indexing)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"EBSD-GUI", None))
        self.actionOpen_Workfolder.setText(QCoreApplication.translate("MainWindow", u"Open Workfolder...", None))
#if QT_CONFIG(statustip)
        self.actionOpen_Workfolder.setStatusTip(QCoreApplication.translate("MainWindow", u"Select a folder containing patterns", u"LOL"))
#endif // QT_CONFIG(statustip)
        self.actionProcessingMenu.setText(QCoreApplication.translate("MainWindow", u"Noise-to-signal improvement", None))
#if QT_CONFIG(statustip)
        self.actionProcessingMenu.setStatusTip(QCoreApplication.translate("MainWindow", u"Perform processing on a pattern", None))
#endif // QT_CONFIG(statustip)
        self.actionSignalNavigation.setText(QCoreApplication.translate("MainWindow", u"Signal navigation", None))
        self.actionDictionary_indexing.setText(QCoreApplication.translate("MainWindow", u"Dictionary indexing", None))
        self.actionPattern_Center.setText(QCoreApplication.translate("MainWindow", u"Refine pattern center", None))
        self.actionROI.setText(QCoreApplication.translate("MainWindow", u"Choose region of interest", None))
        self.actionHough_indexing.setText(QCoreApplication.translate("MainWindow", u"Hough indexing", None))
        self.actionPre_indexing_maps.setText(QCoreApplication.translate("MainWindow", u"Generate pre-indexing maps", None))
        self.actionSettings.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
#if QT_CONFIG(statustip)
        self.actionSettings.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.folderLabel.setText(QCoreApplication.translate("MainWindow", u"NO FOLDER OPENED", None))
        self.consolePrompt.setText(QCoreApplication.translate("MainWindow", u">>>", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuProcessing.setTitle(QCoreApplication.translate("MainWindow", u"Processing", None))
        self.menuPlot.setTitle(QCoreApplication.translate("MainWindow", u"Pattern inspection", None))
        self.menuDictionary_indexing.setTitle(QCoreApplication.translate("MainWindow", u"Indexing", None))
    # retranslateUi


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bubbleChart.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_BubbleChartTab(object):
    def setupUi(self, BubbleChartTab):
        BubbleChartTab.setObjectName("BubbleChartTab")
        BubbleChartTab.resize(1150, 830)
        BubbleChartTab.setMinimumSize(QtCore.QSize(1150, 830))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        BubbleChartTab.setFont(font)
        BubbleChartTab.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.gridLayout = QtWidgets.QGridLayout(BubbleChartTab)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(BubbleChartTab)
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.bubbleChartView = QtWebEngineWidgets.QWebEngineView(BubbleChartTab)
        self.bubbleChartView.setStyleSheet("color: rgb(0, 0, 0);")
        self.bubbleChartView.setUrl(QtCore.QUrl("about:blank"))
        self.bubbleChartView.setObjectName("bubbleChartView")
        self.gridLayout.addWidget(self.bubbleChartView, 1, 0, 1, 2)
        self.extractBubbleBtn = QtWidgets.QPushButton(BubbleChartTab)
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.extractBubbleBtn.setFont(font)
        self.extractBubbleBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.extractBubbleBtn.setMouseTracking(True)
        self.extractBubbleBtn.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.extractBubbleBtn.setObjectName("extractBubbleBtn")
        self.gridLayout.addWidget(self.extractBubbleBtn, 2, 0, 1, 1)

        self.retranslateUi(BubbleChartTab)
        QtCore.QMetaObject.connectSlotsByName(BubbleChartTab)

    def retranslateUi(self, BubbleChartTab):
        _translate = QtCore.QCoreApplication.translate
        BubbleChartTab.setWindowTitle(_translate("BubbleChartTab", "Bubble Chart"))
        self.label.setText(_translate("BubbleChartTab", "Bubble Chart "))
        self.extractBubbleBtn.setText(_translate("BubbleChartTab", "Extract Video"))

from PyQt5 import QtWebEngineWidgets

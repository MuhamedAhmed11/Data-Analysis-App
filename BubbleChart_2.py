# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'BubbleChart_2.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_BubbleChart_2(object):
    def setupUi(self, BubbleChart_2):
        BubbleChart_2.setObjectName("BubbleChart_2")
        BubbleChart_2.resize(1150, 830)
        BubbleChart_2.setMinimumSize(QtCore.QSize(1150, 830))
        BubbleChart_2.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.gridLayout = QtWidgets.QGridLayout(BubbleChart_2)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(BubbleChart_2)
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.bubbleChartView2 = QtWebEngineWidgets.QWebEngineView(BubbleChart_2)
        self.bubbleChartView2.setUrl(QtCore.QUrl("about:blank"))
        self.bubbleChartView2.setObjectName("bubbleChartView2")
        self.gridLayout.addWidget(self.bubbleChartView2, 1, 0, 1, 2)
        self.extractBubbleChartBtn_2 = QtWidgets.QPushButton(BubbleChart_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.extractBubbleChartBtn_2.setFont(font)
        self.extractBubbleChartBtn_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.extractBubbleChartBtn_2.setObjectName("extractBubbleChartBtn_2")
        self.gridLayout.addWidget(self.extractBubbleChartBtn_2, 2, 0, 1, 1)

        self.retranslateUi(BubbleChart_2)
        QtCore.QMetaObject.connectSlotsByName(BubbleChart_2)

    def retranslateUi(self, BubbleChart_2):
        _translate = QtCore.QCoreApplication.translate
        BubbleChart_2.setWindowTitle(_translate("BubbleChart_2", "BubbleChart"))
        self.label.setText(_translate("BubbleChart_2", "Bubble Chart"))
        self.extractBubbleChartBtn_2.setText(_translate("BubbleChart_2", "Extract as Video"))

from PyQt5 import QtWebEngineWidgets

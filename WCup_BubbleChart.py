# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WCup_BubbleChart.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_worldCupBubbleChart(object):
    def setupUi(self, worldCupBubbleChart):
        worldCupBubbleChart.setObjectName("worldCupBubbleChart")
        worldCupBubbleChart.resize(1027, 596)
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        worldCupBubbleChart.setFont(font)
        worldCupBubbleChart.setStyleSheet("background-color: rgb(125, 171, 255);")
        self.gridLayout = QtWidgets.QGridLayout(worldCupBubbleChart)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(worldCupBubbleChart)
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.worldCupBubbleChartView = QtWebEngineWidgets.QWebEngineView(worldCupBubbleChart)
        self.worldCupBubbleChartView.setUrl(QtCore.QUrl("about:blank"))
        self.worldCupBubbleChartView.setObjectName("worldCupBubbleChartView")
        self.gridLayout.addWidget(self.worldCupBubbleChartView, 1, 0, 1, 1)

        self.retranslateUi(worldCupBubbleChart)
        QtCore.QMetaObject.connectSlotsByName(worldCupBubbleChart)

    def retranslateUi(self, worldCupBubbleChart):
        _translate = QtCore.QCoreApplication.translate
        worldCupBubbleChart.setWindowTitle(_translate("worldCupBubbleChart", "Bubble Chart"))
        self.label.setText(_translate("worldCupBubbleChart", "Bubble Chart"))

from PyQt5 import QtWebEngineWidgets

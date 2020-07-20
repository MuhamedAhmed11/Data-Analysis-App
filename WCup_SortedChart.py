# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WCup_SortedChart.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_worldCupSortedChart(object):
    def setupUi(self, worldCupSortedChart):
        worldCupSortedChart.setObjectName("worldCupSortedChart")
        worldCupSortedChart.resize(985, 613)
        worldCupSortedChart.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.gridLayout = QtWidgets.QGridLayout(worldCupSortedChart)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(worldCupSortedChart)
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.worldCupSortedChartView = QtWebEngineWidgets.QWebEngineView(worldCupSortedChart)
        self.worldCupSortedChartView.setUrl(QtCore.QUrl("about:blank"))
        self.worldCupSortedChartView.setObjectName("worldCupSortedChartView")
        self.gridLayout.addWidget(self.worldCupSortedChartView, 1, 0, 1, 1)

        self.retranslateUi(worldCupSortedChart)
        QtCore.QMetaObject.connectSlotsByName(worldCupSortedChart)

    def retranslateUi(self, worldCupSortedChart):
        _translate = QtCore.QCoreApplication.translate
        worldCupSortedChart.setWindowTitle(_translate("worldCupSortedChart", "Sorted Chart"))
        self.label.setText(_translate("worldCupSortedChart", "Sorted Chart"))

from PyQt5 import QtWebEngineWidgets

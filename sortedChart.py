# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sortedChart.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SortedChartTab(object):
    def setupUi(self, SortedChartTab):
        SortedChartTab.setObjectName("SortedChartTab")
        SortedChartTab.resize(1150, 830)
        SortedChartTab.setMinimumSize(QtCore.QSize(1150, 830))
        SortedChartTab.setStyleSheet("background-color: rgb(170, 85, 255);\n"
"background-color: rgb(170, 170, 255);")
        self.gridLayout = QtWidgets.QGridLayout(SortedChartTab)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(SortedChartTab)
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.SortChartView = QtWebEngineWidgets.QWebEngineView(SortedChartTab)
        self.SortChartView.setUrl(QtCore.QUrl("about:blank"))
        self.SortChartView.setObjectName("SortChartView")
        self.gridLayout.addWidget(self.SortChartView, 1, 0, 1, 2)
        self.extractSortChartBtn = QtWidgets.QPushButton(SortedChartTab)
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.extractSortChartBtn.setFont(font)
        self.extractSortChartBtn.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.extractSortChartBtn.setObjectName("extractSortChartBtn")
        self.gridLayout.addWidget(self.extractSortChartBtn, 2, 0, 1, 1)

        self.retranslateUi(SortedChartTab)
        QtCore.QMetaObject.connectSlotsByName(SortedChartTab)

    def retranslateUi(self, SortedChartTab):
        _translate = QtCore.QCoreApplication.translate
        SortedChartTab.setWindowTitle(_translate("SortedChartTab", "Sorted Chart"))
        self.label.setText(_translate("SortedChartTab", "Sorted Chart"))
        self.extractSortChartBtn.setText(_translate("SortedChartTab", "Extract Video"))

from PyQt5 import QtWebEngineWidgets

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mapGraph.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MapGraphTab(object):
    def setupUi(self, MapGraphTab):
        MapGraphTab.setObjectName("MapGraphTab")
        MapGraphTab.resize(1150, 831)
        MapGraphTab.setMinimumSize(QtCore.QSize(1150, 830))
        MapGraphTab.setStyleSheet("background-color: rgb(255, 96, 117);")
        self.gridLayout = QtWidgets.QGridLayout(MapGraphTab)
        self.gridLayout.setObjectName("gridLayout")
        self.mapView = QtWebEngineWidgets.QWebEngineView(MapGraphTab)
        self.mapView.setUrl(QtCore.QUrl("about:blank"))
        self.mapView.setObjectName("mapView")
        self.gridLayout.addWidget(self.mapView, 1, 0, 1, 2)
        self.label = QtWidgets.QLabel(MapGraphTab)
        self.label.setMinimumSize(QtCore.QSize(1050, 0))
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        self.extractrMapBtn = QtWidgets.QPushButton(MapGraphTab)
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.extractrMapBtn.setFont(font)
        self.extractrMapBtn.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.extractrMapBtn.setObjectName("extractrMapBtn")
        self.gridLayout.addWidget(self.extractrMapBtn, 2, 0, 1, 1)

        self.retranslateUi(MapGraphTab)
        QtCore.QMetaObject.connectSlotsByName(MapGraphTab)

    def retranslateUi(self, MapGraphTab):
        _translate = QtCore.QCoreApplication.translate
        MapGraphTab.setWindowTitle(_translate("MapGraphTab", "Map Graph"))
        self.label.setText(_translate("MapGraphTab", "Map Graph"))
        self.extractrMapBtn.setText(_translate("MapGraphTab", "Extract Video"))

from PyQt5 import QtWebEngineWidgets

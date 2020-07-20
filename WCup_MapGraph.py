# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WCup_MapGraph.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_worldCupMapGraph(object):
    def setupUi(self, worldCupMapGraph):
        worldCupMapGraph.setObjectName("worldCupMapGraph")
        worldCupMapGraph.resize(851, 538)
        worldCupMapGraph.setStyleSheet("background-color: rgb(255, 180, 249);")
        self.gridLayout = QtWidgets.QGridLayout(worldCupMapGraph)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(worldCupMapGraph)
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.worldCupMapGraphView = QtWebEngineWidgets.QWebEngineView(worldCupMapGraph)
        self.worldCupMapGraphView.setUrl(QtCore.QUrl("about:blank"))
        self.worldCupMapGraphView.setObjectName("worldCupMapGraphView")
        self.gridLayout.addWidget(self.worldCupMapGraphView, 1, 0, 1, 1)

        self.retranslateUi(worldCupMapGraph)
        QtCore.QMetaObject.connectSlotsByName(worldCupMapGraph)

    def retranslateUi(self, worldCupMapGraph):
        _translate = QtCore.QCoreApplication.translate
        worldCupMapGraph.setWindowTitle(_translate("worldCupMapGraph", "Map Graph"))
        self.label.setText(_translate("worldCupMapGraph", "Map Graph"))

from PyQt5 import QtWebEngineWidgets

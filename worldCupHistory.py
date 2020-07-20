# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'worldCupHistory.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_worldCupHistory(object):
    def setupUi(self, worldCupHistory):
        worldCupHistory.setObjectName("worldCupHistory")
        worldCupHistory.resize(1262, 733)
        worldCupHistory.setMinimumSize(QtCore.QSize(1150, 710))
        worldCupHistory.setStyleSheet("background-image: url(:/images/nomwumvkxilildca8wuf.jpg);\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);\n"
"background-repeat: no-repeat;")
        self.gridLayout_2 = QtWidgets.QGridLayout(worldCupHistory)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 135, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 0, 0, 1, 1)
        self.label = QtWidgets.QLabel(worldCupHistory)
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("")
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(844, 70, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 1, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 135, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem2, 2, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        spacerItem3 = QtWidgets.QSpacerItem(138, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 0, 0, 1, 1)
        self.BubbleChartButton = QtWidgets.QPushButton(worldCupHistory)
        self.BubbleChartButton.setMinimumSize(QtCore.QSize(400, 300))
        self.BubbleChartButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.BubbleChartButton.setStyleSheet("background-image: url(:/images/bubble.JPG);\n"
"background-color: rgb(255, 255, 255);")
        self.BubbleChartButton.setText("")
        self.BubbleChartButton.setObjectName("BubbleChartButton")
        self.gridLayout.addWidget(self.BubbleChartButton, 0, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(168, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 0, 2, 1, 1)
        self.SortedChartButton = QtWidgets.QPushButton(worldCupHistory)
        self.SortedChartButton.setMinimumSize(QtCore.QSize(400, 300))
        self.SortedChartButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.SortedChartButton.setStyleSheet("background-image: url(:/images/Ranks.JPG);\n"
"background-color: rgb(255, 255, 255);")
        self.SortedChartButton.setText("")
        self.SortedChartButton.setObjectName("SortedChartButton")
        self.gridLayout.addWidget(self.SortedChartButton, 0, 3, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(148, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 0, 4, 1, 1)
        self.label_10 = QtWidgets.QLabel(worldCupHistory)
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 1, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(worldCupHistory)
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 1, 3, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 3, 0, 1, 2)

        self.retranslateUi(worldCupHistory)
        QtCore.QMetaObject.connectSlotsByName(worldCupHistory)

    def retranslateUi(self, worldCupHistory):
        _translate = QtCore.QCoreApplication.translate
        worldCupHistory.setWindowTitle(_translate("worldCupHistory", "World Cup History"))
        self.label.setText(_translate("worldCupHistory", "Data Analysis"))
        self.label_10.setText(_translate("worldCupHistory", "                Bubble Chart"))
        self.label_9.setText(_translate("worldCupHistory", "                Sorted Chart"))

import sourcc_rc

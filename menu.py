# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menu.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1034, 828)
        MainWindow.setStyleSheet("background-image: url(:/images/best-business-intelligence-and-data-visualization-tools-for-2019-featured-1200x900.jpg);\n"
"background-repeat: no-repeat;\n"
"background-color: rgb(22, 26, 53);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 81, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 0, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(594, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 1, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 238, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem2, 2, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.covid19DataButton = QtWidgets.QPushButton(self.centralwidget)
        self.covid19DataButton.setMinimumSize(QtCore.QSize(400, 300))
        self.covid19DataButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.covid19DataButton.setStyleSheet("background-image: url(:/images/covid19-2-400x300.jpg);\n"
"background-color: rgb(255, 255, 255);")
        self.covid19DataButton.setText("")
        self.covid19DataButton.setObjectName("covid19DataButton")
        self.gridLayout.addWidget(self.covid19DataButton, 0, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 0, 1, 1, 1)
        self.worldCupDataButton = QtWidgets.QPushButton(self.centralwidget)
        self.worldCupDataButton.setMinimumSize(QtCore.QSize(400, 300))
        self.worldCupDataButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.worldCupDataButton.setStyleSheet("background-image: url(:/images/512066_v2.jpg);\n"
"background-color: rgb(255, 255, 255);")
        self.worldCupDataButton.setText("")
        self.worldCupDataButton.setObjectName("worldCupDataButton")
        self.gridLayout.addWidget(self.worldCupDataButton, 0, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 2, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 3, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Data Analysis Application"))
        self.label.setText(_translate("MainWindow", "Data Analysis"))
        self.label_2.setText(_translate("MainWindow", "COVID-19 Data Analysis"))
        self.label_3.setText(_translate("MainWindow", "World Cup Data Analysis"))

import sourcc_rc

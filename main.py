from PyQt5 import QtWidgets, QtGui
from menu import Ui_MainWindow
from bubbleChart import Ui_BubbleChartTab
from mapGraph import Ui_MapGraphTab
from covid19 import Ui_Form
from sortedChart import Ui_SortedChartTab
from BubbleChart_2 import Ui_BubbleChart_2
from WCup_BubbleChart import Ui_worldCupBubbleChart
from WCup_SortedChart import Ui_worldCupSortedChart
from worldCupHistory import Ui_worldCupHistory
import plotly.express as px
import pandas as pd
import plotly.offline as plt
import sys
import os
import cv2
import numpy as np
import pyautogui
import matplotlib.animation as animation
import matplotlib.pyplot as plot


class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(ApplicationWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        data = os.getcwd() + '\Datasets\world_data.csv'
        self.dataFrame = pd.read_csv(data)

        worldCupData = os.getcwd() + '\Datasets\world_cup.csv'
        self.worldCupDataFrame = pd.read_csv(worldCupData)

        self.ui.covid19DataButton.clicked.connect(
            lambda: self.OpenWindow('COVID-19'))
        self.ui.worldCupDataButton.clicked.connect(
            lambda: self.OpenWindow('WorldCup'))

    def htmlConverter(self, fig):
        raw_html = '<html><head><meta charset="utf-8" />'
        raw_html += '<script src="https://cdn.plot.ly/plotly-latest.min.js"></script></head>'
        raw_html += '<body>'
        raw_html += plt.plot(fig, include_plotlyjs=False, output_type='div')
        raw_html += '</body></html>'
        return raw_html

    def OpenWindow(self, value):
        if value == 'BubbleGraph1':
            self.Form = QtWidgets.QWidget()
            self.ui = Ui_BubbleChartTab()
            self.ui.setupUi(self.Form)
            self.Form.show()
            self.bubbleChartPlot()
            self.ui.extractBubbleBtn.clicked.connect(
                lambda: self.checkClickedBtn('bubble1'))
        if value == 'MapGraph':
            self.Form = QtWidgets.QWidget()
            self.ui = Ui_MapGraphTab()
            self.ui.setupUi(self.Form)
            self.Form.show()
            self.mapGraphPlot()
            self.ui.extractrMapBtn.clicked.connect(
                lambda: self.checkClickedBtn('map'))
        if value == 'SortedList':
            self.Form = QtWidgets.QWidget()
            self.ui = Ui_SortedChartTab()
            self.ui.setupUi(self.Form)
            self.Form.show()
            self.sortChartPlot()
            self.ui.extractSortChartBtn.clicked.connect(
                lambda: self.checkClickedBtn('list'))
        if value == 'BubbleGraph2':
            self.Form = QtWidgets.QWidget()
            self.ui = Ui_BubbleChart_2()
            self.ui.setupUi(self.Form)
            self.Form.show()
            self.bubbleChartPlot_2()
            self.ui.extractBubbleChartBtn_2.clicked.connect(
                lambda: self.checkClickedBtn('bubble2'))

        if value == 'COVID-19':
            self.Form2 = QtWidgets.QWidget()
            self.ui = Ui_Form()
            self.ui.setupUi(self.Form2)
            self.Form2.show()
            self.ui.BubbleChartButton.clicked.connect(
                lambda: self.OpenWindow('BubbleGraph1'))
            self.ui.MapGraphButton.clicked.connect(
                lambda: self.OpenWindow('MapGraph'))
            self.ui.SortedChartButton.clicked.connect(
                lambda: self.OpenWindow('SortedList'))
            self.ui.BubbleChartButton_2.clicked.connect(
                lambda: self.OpenWindow('BubbleGraph2'))
        ############################################### WORLD CUP TABS ###############################################
        if value == 'WorldCup':
            self.Form2 = QtWidgets.QWidget()
            self.ui = Ui_worldCupHistory()
            self.ui.setupUi(self.Form2)
            self.Form2.show()
            self.ui.BubbleChartButton.clicked.connect(
                lambda: self.OpenWindow(6))
            self.ui.SortedChartButton.clicked.connect(
                lambda: self.OpenWindow(7))
        if value == 6:
            self.Form = QtWidgets.QWidget()
            self.ui = Ui_worldCupBubbleChart()
            self.ui.setupUi(self.Form)
            self.Form.show()
            self.worldCupBubbleChartPlot()
        if value == 7:
            self.Form = QtWidgets.QWidget()
            self.ui = Ui_worldCupSortedChart()
            self.ui.setupUi(self.Form)
            self.Form.show()
            self.worldCupSotedChartPlot()

    ############################################### COVID-19 Datasets ###############################################
    def checkClickedBtn(self, value):
        if value == 'bubble1':
            path = os.getcwd() + '/BubbleGraph Screenshots'
            self.extractVideo(path, 'BubbleChart_1.avi')
        if value == 'bubble2':
            path = os.getcwd() + '/BubbleGraph_2 Screenshots'
            self.extractVideo(path, 'BubbleChart_2.avi')
        if value == 'map':
            path = os.getcwd() + '/mapGraph Screenshots'
            self.extractVideo(path, 'mapGraph.avi')
        if value == 'list':
            path = os.getcwd() + '/sortedChart Screenshots'
            self.extractVideo(path, 'SortedChart.avi')

    def bubbleChartPlot(self):
        fig = px.scatter(self.dataFrame, x='Deaths', y='Recovered', animation_frame="Date", animation_group="Country", size="Confirmed", color="continent",
                         hover_name="Country", log_x=True, size_max=65, range_x=[10, 4000000], range_y=[10, 300000], title="COVID-19")
        raw_html = self.htmlConverter(fig)
        self.ui.bubbleChartView.setHtml(raw_html)

    def mapGraphPlot(self):
        fig = px.choropleth(self.dataFrame, locations="iso_alpha", color="Confirmed",
                            hover_name="Country", title="COVID-19",
                            animation_frame="Date",
                            color_continuous_scale=px.colors.sequential.YlOrRd)
        raw_html = self.htmlConverter(fig)
        self.ui.mapView.setHtml(raw_html)

    def sortChartPlot(self):
        fig = px.bar(self.dataFrame, x="Confirmed", y="Country",
                     orientation='h', animation_frame="Date", color="continent", title="COVID-19")
        raw_html = self.htmlConverter(fig)
        self.ui.SortChartView.setHtml(raw_html)

    def bubbleChartPlot_2(self):
        fig = px.scatter(self.dataFrame, x='Recovered', y='Deaths', animation_frame="Date", animation_group="Country", size="Confirmed", color="continent",
                         hover_name="Country", log_x=True, size_max=65, range_x=[10, 4000000], range_y=[10, 300000], title="COVID-19")
        raw_html = self.htmlConverter(fig)
        self.ui.bubbleChartView2.setHtml(raw_html)

    def extractVideo(self, folderPath, videoName):
        image_folder = folderPath
        video_name = videoName
        # images = [img for img in os.listdir(
        #     image_folder) if img.endswith(".JPG")]
        images = ['Capture0.JPG', 'Capture1.JPG', 'Capture2.JPG', 'Capture3.JPG', 'Capture4.JPG', 'Capture5.JPG', 'Capture6.JPG', 'Capture7.JPG', 'Capture8.JPG',
                  'Capture9.JPG', 'Capture10.JPG', 'Capture11.JPG', 'Capture12.JPG', 'Capture13.JPG', 'Capture14.JPG', 'Capture15.JPG', 'Capture16.JPG', 'Capture17.JPG', 'Capture18.JPG']
        frame = cv2.imread(os.path.join(image_folder, images[0]))
        height, width, layers = frame.shape

        video = cv2.VideoWriter(video_name, 0, 1, (width, height))

        for image in images:
            video.write(cv2.imread(os.path.join(image_folder, image)))

        cv2.destroyAllWindows()
        video.release()

    ################################################## World Cup Datasets ##################################################

    def worldCupBubbleChartPlot(self):
        fig = px.scatter(self.worldCupDataFrame, x="Won", y="Lost", animation_frame="Year",
                         size="Goals for", hover_name="Team", color="Team",
                         log_x=True, size_max=65)
        raw_html = self.htmlConverter(fig)
        self.ui.worldCupBubbleChartView.setHtml(raw_html)

    def worldCupSotedChartPlot(self):
        fig = px.bar(self.worldCupDataFrame, x="Goals for", y="Team",
                     orientation='h', animation_frame="Year", color="Team")
        raw_html = self.htmlConverter(fig)
        self.ui.worldCupSortedChartView.setHtml(raw_html)


def main():
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    app.exec_()


if __name__ == "__main__":
    main()

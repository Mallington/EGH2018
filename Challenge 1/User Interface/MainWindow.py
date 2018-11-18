# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
# Matplotlib libraries
import matplotlib
matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt
# Matplot in PyQt5 Libraries
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
# Numpy Library
import numpy as np



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1650,1080)
        self.mainWidget = QtWidgets.QWidget(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.mainWidget.setFont(font)
        self.mainWidget.setStyleSheet("background-color: rgb(40, 43, 48);\n"
"color: rgb(255,255,255);\n"
"font: 15pt \"Trebuchet MS\";")
        self.mainWidget.setObjectName("mainWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.mainWidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lbl3 = QtWidgets.QLabel(self.mainWidget)
        self.lbl3.setStyleSheet("color: rgb(40, 43, 48);")
        self.lbl3.setObjectName("lbl3")
        self.gridLayout_2.addWidget(self.lbl3, 0, 10, 1, 1)
        self.lbl2 = QtWidgets.QLabel(self.mainWidget)
        self.lbl2.setStyleSheet("color: rgb(40, 43, 48);")
        self.lbl2.setObjectName("lbl2")
        self.gridLayout_2.addWidget(self.lbl2, 0, 9, 1, 1)
        self.lbl9 = QtWidgets.QLabel(self.mainWidget)
        self.lbl9.setStyleSheet("color: rgb(40, 43, 48);")
        self.lbl9.setObjectName("lbl9")
        self.gridLayout_2.addWidget(self.lbl9, 0, 16, 1, 1)
        self.lbl6 = QtWidgets.QLabel(self.mainWidget)
        self.lbl6.setStyleSheet("color: rgb(40, 43, 48);")
        self.lbl6.setObjectName("lbl6")
        self.gridLayout_2.addWidget(self.lbl6, 0, 13, 1, 1)
        self.lbl5 = QtWidgets.QLabel(self.mainWidget)
        self.lbl5.setStyleSheet("color: rgb(40, 43, 48);")
        self.lbl5.setObjectName("lbl5")
        self.gridLayout_2.addWidget(self.lbl5, 0, 12, 1, 1)
        self.lbl4 = QtWidgets.QLabel(self.mainWidget)
        self.lbl4.setStyleSheet("color: rgb(40, 43, 48);")
        self.lbl4.setObjectName("lbl4")
        self.gridLayout_2.addWidget(self.lbl4, 0, 11, 1, 1)
        self.companyList = QtWidgets.QListWidget(self.mainWidget)
        self.companyList.setStyleSheet("background-color: rgb(54,57,63); \n"
"")
        self.companyList.setObjectName("companyList")
        companies = ["A","B","B","B","B","B","B","B","B","B"]
        for company in companies:
            item = QtWidgets.QListWidgetItem()
            self.companyList.addItem(item)


        self.gridLayout_2.addWidget(self.companyList, 1, 0, 1, 5)
        self.searchbar = QtWidgets.QLineEdit(self.mainWidget)
        self.searchbar.setStyleSheet("background-color: rgb(255,255,255);\n"
"color: rgb(0,0,0);")
        self.searchbar.setObjectName("searchbar")
        self.gridLayout_2.addWidget(self.searchbar, 0, 0, 1, 1)
        self.searchButton = QtWidgets.QPushButton(self.mainWidget)
        self.searchButton.setStyleSheet("background-color: rgb(54,57,63); \n"
"")
        self.searchButton.setObjectName("searchButton")
        self.gridLayout_2.addWidget(self.searchButton, 0, 1, 1, 1)
        self.lbl7 = QtWidgets.QLabel(self.mainWidget)
        self.lbl7.setStyleSheet("color: rgb(40, 43, 48);")
        self.lbl7.setObjectName("lbl7")
        self.gridLayout_2.addWidget(self.lbl7, 0, 14, 1, 1)
        self.lbl8 = QtWidgets.QLabel(self.mainWidget)
        self.lbl8.setStyleSheet("color: rgb(40, 43, 48);")
        self.lbl8.setObjectName("lbl8")
        self.gridLayout_2.addWidget(self.lbl8, 0, 15, 1, 1)
        self.canvas = QtWidgets.QGridLayout()
        self.canvas.setObjectName("canvas")
        self.graph = MplCanvas(self.mainWidget)
        self.canvas.addWidget(self.graph)
        self.gridLayout_2.addLayout(self.canvas, 1, 7, 1, 11)
        MainWindow.setCentralWidget(self.mainWidget)
        self.companyList.itemSelectionChanged.connect(self.selectionChanged)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lbl3.setText(_translate("MainWindow", "TextLabel"))
        self.lbl2.setText(_translate("MainWindow", "TextLabel"))
        self.lbl9.setText(_translate("MainWindow", "TextLabel"))
        self.lbl6.setText(_translate("MainWindow", "TextLabel"))
        self.lbl5.setText(_translate("MainWindow", "TextLabel"))
        self.lbl4.setText(_translate("MainWindow", "TextLabel"))
        __sortingEnabled = self.companyList.isSortingEnabled()
        self.companyList.setSortingEnabled(False)
        item = self.companyList.item(0)
        item.setText(_translate("MainWindow", "Company 0"))
        item = self.companyList.item(1)
        item.setText(_translate("MainWindow", "Company 1"))
        item = self.companyList.item(2)
        item.setText(_translate("MainWindow", "Company 2"))
        item = self.companyList.item(3)
        item.setText(_translate("MainWindow", "Company 3"))
        item = self.companyList.item(4)
        item.setText(_translate("MainWindow", "Company 4"))
        item = self.companyList.item(5)
        item.setText(_translate("MainWindow", "Company 5"))
        self.companyList.setSortingEnabled(__sortingEnabled)
        self.searchbar.setPlaceholderText(_translate("MainWindow", "Type Here to Search..."))
        self.searchButton.setText(_translate("MainWindow", "Search"))
        self.lbl7.setText(_translate("MainWindow", "TextLabel"))
        self.lbl8.setText(_translate("MainWindow", "TextLabel"))

    def selectionChanged(self):
        print("Selected items: ", self.companyList.currentRow())

class MplCanvas(FigureCanvas):
    """Canvas object for the graph to be plotted within"""
    def __init__(self, parent=None):
        """Instantiates the subplots"""
        fig = Figure()
        FigureCanvas.__init__(self, fig)
        self.axes = fig.add_subplot(111)
        self.setupAxis()
        self.timer = QtCore.QTimer(self)
        fig.set_facecolor("#282B30")
        self.epochs = []
        self.prices = []
        self.simpleMA = [0]
        self.expMA = [0]
        # Need vars for sds too
        
        self.startProjectile()


    def setupAxis(self):
        """Sets up the axis to stop them from skewing"""
        self.axes.set_autoscale_on(False)  # Stops the graph from changing in size, skewing the projectile's motion
        self.axes.set_xlim(0, 100)  # Sets the range for the plot to work on
        self.axes.set_ylim(0, 100)
        self.axes.set_xlabel("Epoch")
        self.axes.set_ylabel("Price")
        self.axes.yaxis.label.set_color("white")
        self.axes.xaxis.label.set_color("white")
        self.axes.tick_params(axis="y", colors="white")
        self.axes.tick_params(axis="x", colors="white")
        self.axes.title.set_color("white")
        self.axes.set_facecolor("#282B30")
        self.axes.spines["left"].set_color("white")
        self.axes.spines["bottom"].set_color("white")
        self.axes.spines["right"].set_color("#282B30")
        self.axes.spines["top"].set_color("#282B30")
        
        
    def startProjectile(self):
        """Starts the projectile off, once the button has been pressed"""
        self.__plots = np.zeros(shape=(130, 2))  # Clears the array again
        self.__plotCounter = 0
        self._GPEarray = []
        self._KEarray = []
        self.timer.timeout.connect(self.PlotNextPoint)
        self.timer.start(1000)  # Needs to only start when the button pressed

    def PlotNextPoint(self):
        """Plots the new location for the projectile each second"""
        self.epochs.append(self.__plotCounter)
        self.prices.append(np.random.randint(100))
        #Get the epochs from your code
        #get the prices from your code
        self.axes.plot(self.epochs,self.prices, "white") # Plots the points so far
        self.draw()  # Redraws the graph
        self.__plotCounter += 1


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


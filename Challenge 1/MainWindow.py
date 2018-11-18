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
# In House library
import DataStream
import functions

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.resize(1650,1080)
        self.mainWidget = QtWidgets.QWidget(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.mainWidget.setFont(font)
        self.mainWidget.setObjectName("mainWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.mainWidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lbl3 = QtWidgets.QLabel(self.mainWidget)
        self.lbl3.setObjectName("lbl3")
        self.gridLayout_2.addWidget(self.lbl3, 0, 10, 1, 1)
        self.comboBox2 = QtWidgets.QComboBox(self.mainWidget)
        self.comboBox2.setObjectName("comboBox2")
        self.gridLayout_2.addWidget(self.comboBox2, 0, 9, 1, 1)
        self.button9 = QtWidgets.QPushButton(self.mainWidget)
        self.button9.setObjectName("button9")
        self.button9.clicked.connect(self.themeButton)
        self.gridLayout_2.addWidget(self.button9, 0, 16, 1, 1)
        self.lbl6 = QtWidgets.QLabel(self.mainWidget)
        self.lbl6.setObjectName("lbl6")
        self.gridLayout_2.addWidget(self.lbl6, 0, 11, 1, 1)
        self.lineBox4 = QtWidgets.QLineEdit(self.mainWidget)
        self.lineBox4.setObjectName("lineBox4")
        self.gridLayout_2.addWidget(self.lineBox4, 0, 12, 1, 1)
        self.lineBox5 = QtWidgets.QLineEdit(self.mainWidget)
        self.lineBox5.setObjectName("lineBox5")
        self.gridLayout_2.addWidget(self.lineBox5, 0, 13, 1, 1)
        self.companyList = QtWidgets.QListWidget(self.mainWidget)
        self.companyList.setObjectName("companyList")
        self.data = DataStream.DataStream()

        self.comboBox2.addItem("   0  ")
        self.comboBox2.addItem("  10  ")
        self.comboBox2.addItem("  30  ")
        self.comboBox2.addItem("  60  ")
        self.comboBox2.activated[str].connect(self.changeEpoch)


        self.companies = self.data.MARKET.Companies

        self.DEFAULT_N = 20
        self.HALF_LIFE = 0


        self.recalculateSim(self.DEFAULT_N)
        self.recalculateExp(self.HALF_LIFE)

        i = 0
        for company in self.companies:
            #print(company.COMPANY_NAME)
            item = QtWidgets.QListWidgetItem()
            self.companyList.addItem(item)
            item = self.companyList.item(i)
            _translate = QtCore.QCoreApplication.translate
            item.setText(_translate("MainWindow", company.COMPANY_NAME+" ["+company.SYMBOL+"]"))
            i += 1




        self.gridLayout_2.addWidget(self.companyList, 1, 0, 1, 5)
        self.searchbar = QtWidgets.QLineEdit(self.mainWidget)
        self.searchbar.setObjectName("searchbar")
        self.gridLayout_2.addWidget(self.searchbar, 0, 0, 1, 1)
        self.searchButton = QtWidgets.QPushButton(self.mainWidget)
        self.searchButton.setObjectName("searchButton")
        self.gridLayout_2.addWidget(self.searchButton, 0, 1, 1, 1)
        self.lbl7 = QtWidgets.QLabel(self.mainWidget)
        self.lbl7.setObjectName("lbl7")
        self.gridLayout_2.addWidget(self.lbl7, 0, 14, 1, 1)
        self.lbl8 = QtWidgets.QLabel(self.mainWidget)
        self.lbl8.setObjectName("lbl8")
        self.gridLayout_2.addWidget(self.lbl8, 0, 15, 1, 1)
        self.canvas = QtWidgets.QGridLayout()
        self.canvas.setObjectName("canvas")
        halfLifeText = self.lineBox5.text()
        if halfLifeText == "":
            halfLife = 0
        else:
            halfLife = int(halfLifeText)

        windowText = self.lineBox4.text()
        if  windowText == "":
            window = 0.5
        else:
            window = float(windowText)
        self.graph = MplCanvas(self.data,self.companyList,self.mainWidget,halfLife, self)
        self.canvas.addWidget(self.graph)
        self.gridLayout_2.addLayout(self.canvas, 1, 7, 1, 11)
        MainWindow.setCentralWidget(self.mainWidget)
        self.companyList.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.companyList.itemSelectionChanged.connect(self.selectionChanged)

        self.themeMode = 0
        self.changeTheme(self.themeMode)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def setAllListsHidden(self, value):
        for i in range(self.companyList.count()):
            self.companyList.item(i).setHidden(value)

    def searchKeyWord(self):
        self.setAllListsHidden(True)



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Challenge 1: Charting"))
        self.lbl3.setText(_translate("MainWindow", "MA Window"))
        #self.comboBox2.setText(_translate("MainWindow", "TextLabel"))
        self.button9.setText(_translate("MainWindow", "Change Theme"))
        self.lbl6.setText(_translate("MainWindow", "TextLabel"))
        self.lineBox4.setPlaceholderText(_translate("MainWindow", "Window"))
        self.lineBox5.setPlaceholderText(_translate("MainWindow", "Half-Life Ex"))
        __sortingEnabled = self.companyList.isSortingEnabled()
        self.companyList.setSortingEnabled(False)
        self.companyList.setSortingEnabled(__sortingEnabled)
        self.searchbar.setPlaceholderText(_translate("MainWindow", "Type Here to Search..."))
        self.searchButton.setText(_translate("MainWindow", "Search"))
        self.lbl7.setText(_translate("MainWindow", "TextLabel"))
        self.lbl8.setText(_translate("MainWindow", "TextLabel"))
        self.searchbar.setStyleSheet("background-color: rgb(255,255,255);\n color: rgb(0,0,0);")
        self.lineBox5.setStyleSheet("background-color: rgb(255, 255, 255); \n color: rgb(0, 0, 0);") # 215, 212, 207
        self.lineBox4.setStyleSheet("background-color: rgb(255, 255, 255); \n color: rgb(0, 0, 0);")


    def selectionChanged(self):
        print("Selected items: ", self.companies[self.companyList.currentRow()].COMPANY_NAME)

        self.graph.drawCompany(self.companies[self.companyList.currentRow()])

    def changeEpoch(self, text):
        n = int(text)
        self.recalculateSim(self.DEFAULT_N)
        #self.graph.
        print(n)

    def recalculateSim(self,n):
        if n!=0:
            for company in self.companies:
                for i in range(len(company.EPOCH_DATA)):
                    if company.EPOCH_DATA[i].TRADING:
                        company.EPOCH_DATA[i].SIMPLE_MOV_AVG =0
                        company.EPOCH_DATA[i].MOV_SD =0
                        if i!=0:
                            pric=[x.PRICE for x in company.EPOCH_DATA[:i+1]]
                            company.EPOCH_DATA[i].SIMPLE_MOV_AVG = functions.simMovAvg(pric,company.EPOCH_DATA[i-1].SIMPLE_MOV_AVG,n)



                            if(i<10) :
                                print("pric: ", pric)
                            company.EPOCH_DATA[i].MOV_SD = functions.movStandDev(pric,company.EPOCH_DATA[i-1].SIMPLE_MOV_AVG,company.EPOCH_DATA[i].SIMPLE_MOV_AVG,n)
                        else:
                            company.EPOCH_DATA[i].SIMPLE_MOV_AVG = functions.simMovAvg([company.EPOCH_DATA[0].PRICE],company.EPOCH_DATA[0].SIMPLE_MOV_AVG,n)
                            company.EPOCH_DATA[i].MOV_SD = functions.movStandDev([company.EPOCH_DATA[0].PRICE],company.EPOCH_DATA[0].SIMPLE_MOV_AVG,company.EPOCH_DATA[0].SIMPLE_MOV_AVG,n)


    def recalculateExp(self,halfLife):
        if halfLife!=0:
            for company in self.companies:
                for i in range(len(company.EPOCH_DATA)):
                    company.EPOCH_DATA[i].EXP_MOV_AVG = 0
                    company.EPOCH_DATA[i].EXP_MOV_SD = 0
                    if i!=0:
                        company.EPOCH_DATA[i].EXP_MOV_AVG = functions.expMovAvg(company.EPOCH_DATA[i-1].PRICE,company.EPOCH_DATA[i-1].EXP_MOV_AVG,halfLife)
                        company.EPOCH_DATA[i].EX_VAR = functions.expVar(company.EPOCH_DATA[i-1].PRICE,company.EPOCH_DATA[i-1].EXP_MOV_AVG,company.EPOCH_DATA[i-1].EX_VAR,halfLife)
                        company.EPOCH_DATA[i].EXP_MOV_SD = functions.expMovStandDev(company.EPOCH_DATA[i].EX_VAR)
                    else:
                        company.EPOCH_DATA[0].EXP_MOV_AVG = functions.expMovAvg(company.EPOCH_DATA[0].PRICE,company.EPOCH_DATA[0],halfLife)
                        company.EPOCH_DATA[0].EX_VAR = functions.expVar(company.EPOCH_DATA[0].PRICE,company.EPOCH_DATA[0].EXP_MOV_AVG,company.EPOCH_DATA[0].EX_VAR,halfLife)
                        company.EPOCH_DATA[0].EXP_MOV_SD = functions.expMovStandDev(company.EPOCH_DATA[0].EX_VAR)

    def refresh(self,n,halfLife):
        if n!=0:
            for company in self.companies:
                pric = [x.PRICE for x in company.EPOCH_DATA]
                company.EPOCH_DATA[-1].SIMPLE_MOV_AVG = functions.simMovAvg(pric,company.EPOCH_DATA[-2].SIMPLE_MOV_AVG,n)
                company.EPOCH_DATA[-1].MOV_SD = functions.movStandDev(pric,company.EPOCH_DATA[-2].SIMPLE_MOV_AVG,company.EPOCH_DATA[-1].SIMPLE_MOV_AVG,n)
        if halfLife!=0:
            for company in self.companies:
                company.EPOCH_DATA[-1].EXP_MOV_AVG = functions.expMovAvg(company.EPOCH_DATA.PRICE[-1],company.EPOCH_DATA[-2].EXP_MOV_AVG,halfLife)
                company.EPOCH_DATA[-1].EX_VAR = functions.expVar(company.EPOCH_DATA.PRICE[-1],company.EPOCH_DATA[-2].EXP_MOV_AVG,company.EPOCH_DATA[-2].EX_VAR,halfLife)
                company.EPOCH_DATA[-1].EXP_MOV_SD = functions.expMovStandDev(company.EPOCH_DATA[-1].EX_VAR)



    def changeTheme(self,mode):
        if mode == 0:
            self.lbl7.setStyleSheet("color: rgb(40, 43, 48);")
            self.lbl8.setStyleSheet("color: rgb(40, 43, 48);")
            self.searchButton.setStyleSheet("background-color: rgb(54,57,63); \n")
            self.companyList.setStyleSheet("background-color: rgb(54,57,63); \n")
            self.lbl6.setStyleSheet("color: rgb(40, 43, 48);")
            self.comboBox2.setStyleSheet("background-color: rgb(54, 57, 63); \n color: rgb(255, 255, 255);")
            self.button9.setStyleSheet("background-color: rgb(54,57,63);")
            self.lbl3.setStyleSheet("color: rgb(255, 255, 255);")
            self.mainWidget.setStyleSheet("background-color: rgb(40, 43, 48);\n color: rgb(255,255,255);\n font: 15pt \"Trebuchet MS\";")
        else:
            self.lbl7.setStyleSheet("color: rgb(215, 212, 207);")
            self.lbl8.setStyleSheet("color: rgb(215, 212, 207);")
            self.searchButton.setStyleSheet("background-color: rgb(201,198,192); \n")
            self.companyList.setStyleSheet("background-color: rgb(201,198,192); \n")
            self.lbl6.setStyleSheet("color: rgb(215, 212, 207);")
            self.comboBox2.setStyleSheet("background-color: rgb(201,198,192); \n color: rgb(255, 255, 255);")
            self.button9.setStyleSheet("background-color: rgb(201,198,192);")
            self.lbl3.setStyleSheet("color: rgb(0, 0, 0);")
            self.mainWidget.setStyleSheet("background-color: rgb(215, 212, 207);\n color: rgb(0,0,0);\n font: 15pt \"Trebuchet MS\";")

        self.graph.changeTheme(mode)

    def themeButton(self):
        #print("Theme changed")
        if self.themeMode == 1:
            self.themeMode = 0
        else:
            self.themeMode = 1
        self.changeTheme(self.themeMode)


class MplCanvas(FigureCanvas):
    """Canvas object for the graph to be plotted within"""
    

    def __init__(self, dataPointer,listView,halfLife, mainWindow, parent=None):

        """Instantiates the subplots"""
        self.MAIN_WINDOW = mainWindow
        
        self.halfLife = halfLife
        #self.window = window
        self.DATA_POINTER = dataPointer
        self.LIST_VIEW = listView
        self.fig = Figure()
        FigureCanvas.__init__(self, self.fig)
        self.axes = self.fig.add_subplot(111)
        self.setupAxis()
        self.timer = QtCore.QTimer(self)
        self.epochs = []
        self.prices = []
        self.simpleMA = [0]
        self.expMA = [0]
        # Need vars for sds too

        self.changeAnimationElapsed =0

        self.startProjectile()

    def setupAxis(self):
        """Sets up the axis to stop them from skewing"""
        self.axes.set_xlabel("Epoch", fontsize=50)
        self.axes.set_ylabel("Price", fontsize=50)
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
        self.__plotCounter = 0
        self.timer.timeout.connect(self.updateData)
        self.timer.start(100)  # Needs to only start when the button pressed

    def forceUpdate(self):
        self.drawCompany(self.DATA_POINTER.MARKET.Companies[self.LIST_VIEW.currentRow()])

    def updateData(self):
        
        self.DATA_POINTER.update()

        if self.DATA_POINTER.isUpdateAvailable():
            self.changeAnimationElapsed =0

            
            self.MAIN_WINDOW.refresh(self.MAIN_WINDOW.DEFAULT_N ,self.MAIN_WINDOW.HALF_LIFE)

            self.drawCompany(self.DATA_POINTER.MARKET.Companies[self.LIST_VIEW.currentRow()])
        else:
            if self.changeAnimationElapsed <=10:
                self.drawCompany(self.DATA_POINTER.MARKET.Companies[self.LIST_VIEW.currentRow()])



    def drawCompany(self,comp):
        xAxis = []
        yAxis = []
        color = "white"
            #print("Time: ",e.TIMESTAMP, "Price: ",e.PREV_PRICE )
        self.axes.clear()
        self.axes.set_xlabel("Epoch", fontsize=50)
        self.axes.set_ylabel("Price", fontsize=50)

        for e in comp.EPOCH_DATA:
           xAxis.append(e.TIMESTAMP)
           yAxis.append(e.PRICE)
        self.plotGraph(xAxis,yAxis,color, "-")

        xAxis = []
        yAxis = []
        for e in comp.EPOCH_DATA:
            #if i>wind:
                if(e.SIMPLE_MOV_AVG !=0):

                    xAxis.append(e.TIMESTAMP)
                    yAxis.append(e.SIMPLE_MOV_AVG)
            #i+=1
        self.plotGraph(xAxis,yAxis,color, "--")

        self.draw()
        self.changeAnimationElapsed+=1

    def plotGraph(self, xAxis,yAxis, defaultColor, line):
        if self.changeAnimationElapsed <10:
            self.axes.plot(xAxis,yAxis, "red")
        else:
            self.axes.plot(xAxis,yAxis, defaultColor, linestyle =line)

    def PlotNextPoint(self):
        """Plots the new location for the projectile each second"""
        self.epochs.append(self.__plotCounter)
        self.prices.append(np.random.randint(100))
        self.axes.plot(self.epochs,self.prices, "white") # Plots the points so far
        self.draw()  # Redraws the graph
        self.__plotCounter += 1

    def changeTheme(self, mode):
        if mode == 0:
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
            self.fig.set_facecolor("#282B30")

        else:
            self.axes.yaxis.label.set_color("black")
            self.axes.xaxis.label.set_color("black")
            self.axes.tick_params(axis="y", colors="black")
            self.axes.tick_params(axis="x", colors="black")
            self.axes.title.set_color("black")
            self.axes.set_facecolor("#D7D4CF")
            self.axes.spines["left"].set_color("black")
            self.axes.spines["bottom"].set_color("black")
            self.axes.spines["right"].set_color("#D7D4CF")
            self.axes.spines["top"].set_color("#D7D4CF")
            self.fig.set_facecolor("#D7D4CF")
        self.draw()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

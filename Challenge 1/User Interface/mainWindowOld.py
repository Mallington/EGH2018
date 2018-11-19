# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
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
        MainWindow.resize(1920, 1080)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.centralwidget.setFont(font)
        self.centralwidget.setStyleSheet("background-color: rgb(40, 43, 48);\n"
"color: rgb(255,255,255);\n"
"font: 15pt \"Trebuchet MS\";")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setStyleSheet("background-color: rgb(54,57,63); \n"
"")
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        self.gridLayout_2.addWidget(self.listWidget, 1, 0, 1, 3)
        #Added
        self.canvas = QtWidgets.QVBoxLayout(self.centralwidget)
        self.graph = MplCanvas(self.centralwidget)
        self.canvas.addWidget(self.graph)
        #self.gridLayout_2.addWidget(self.graph, 0, 3, 2, 1)
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setObjectName("graphicsView")
        self.gridLayout_2.addWidget(self.graph, 0, 3, 2, 1)
        
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setStyleSheet("background-color: rgb(54,57,63); \n"
"")
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_2.addWidget(self.pushButton, 0, 2, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setStyleSheet("background-color: rgb(255,255,255);\n"
"color: rgb(0,0,0);")
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_2.addWidget(self.lineEdit, 0, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("MainWindow", "Company 0"))
        item = self.listWidget.item(1)
        item.setText(_translate("MainWindow", "Company 1"))
        item = self.listWidget.item(2)
        item.setText(_translate("MainWindow", "Company 2"))
        item = self.listWidget.item(3)
        item.setText(_translate("MainWindow", "Company 3"))
        item = self.listWidget.item(4)
        item.setText(_translate("MainWindow", "Company 4"))
        item = self.listWidget.item(5)
        item.setText(_translate("MainWindow", "Company 5"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.pushButton.setText(_translate("MainWindow", "Search"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Type Here to Search..."))

        """self.__canvas = QtWidgets.QVBoxLayout()
        self.__graph = MplCanvas(self)
        self.__canvas.addWidget(self.__graph)"""


class MplCanvas(FigureCanvas):
    """Canvas object for the graph to be plotted within"""
    def __init__(self, parent=None):
        """Instantiates the subplots"""
        fig = Figure()
        FigureCanvas.__init__(self, fig)
        self.axes = fig.add_subplot(111)
        self.setupAxis()
        self.timer = QtCore.QTimer(self)
        
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
        self.axes.plot(self.epochs,self.prices, "black") # Plots the points so far
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


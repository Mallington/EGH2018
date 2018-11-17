# PyQt 5 Libraries
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
# Matplotlib libraries
import matplotlib
matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt
# Matplot in PyQt5 Libraries
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
# Numpy Library
import numpy as np




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
        self.axes.set_xlim(0, 1000)  # Sets the range for the plot to work on
        self.axes.set_ylim(0, 1000)
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




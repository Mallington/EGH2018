#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 15:09:43 2018

@author: mathew
"""

import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style


import numpy as np
import time as t


style.use("fivethirtyeight")


fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)



xs = []
ys = []
movingAverage = [0]
def animate(i):
    xs.append(i)
    ys.append(np.random.randint(100))
    ax1.clear()
    ax1.plot(xs,ys)

    

ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()

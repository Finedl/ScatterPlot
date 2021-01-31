# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 14:37:55 2020

@author: dongdong
"""

import numpy as np
import matplotlib.pyplot as plt
library_lng = 120.425947
library_lat = 36.078474
longitude=[]
latitude=[]
for i in range(1,7):#The initial value is 6, every iteration, the number is increased by 6
    longitude=[]
    latitude=[]
    for j in range(i*6):
        n= (np.random.randint(2, 7))* 100
        longitude.append(library_lng + (np.random.rand(1) - 0.5) * 2 / n);
        latitude.append(library_lat + (np.random.rand(1) - 0.5) * 2 / n); 
    figure = plt.figure(figsize = [16, 10])
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    ax = figure.add_subplot()
    ax.set_title('Number of durians:' + str(6 * i), fontproperties = 'SimHei', fontsize = 35)
    ax.scatter(longitude, latitude, s=280, alpha=0.9, marker='v', color ='#ffd700')
    ax.plot(library_lng, library_lat, '.', color = 'r', markersize = 33)
    ax.set_xlabel('Longitude', fontproperties = 'SimHei', fontsize = 30)
    ax.set_ylabel('Latitude', fontproperties = 'SimHei', fontsize = 30)
    ax.ticklabel_format(useOffset=False)
    ax.axis([120.42004, 120.437593, 36.071997, 36.082411])#
    ax.grid()
    plt.savefig('D:/Durian/Durians Distribution' + str(i))
    #plt.show()
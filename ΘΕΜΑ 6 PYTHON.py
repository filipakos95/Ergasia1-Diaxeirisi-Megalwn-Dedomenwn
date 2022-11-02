from statistics import *
import math
import numpy as np
from scipy.spatial import distance
from numpy.linalg import norm

def nominaldistance(v1,v2):
    if len(v1)==len(v2):
        zipped_vector=zip(v1,v2)
        my_sum=0
        for each in zipped_vector:
            my_sum+=pow(each[0]-each[1],2)
        return math.sqrt(my_sum)

#DIANYSMATA
x1=("Green", "Potato", "Ford") 
y1=("Tyrian purple", "Pasta", "Opel")

x2=("Eagle", "Ronaldo", "Real madrid", "Prussian blue", "Michael Bay")
y2=("Eagle", "Ronaldo", "Real madrid", "Prussian blue", "Michael Bay")

x3=("Werner Herzog", "Aquirre, the wrath of God", "Audi", "Spanish red")
y3=("Martin Scorsese", "Taxi driver", "Toyota", "Spanish red")


#ORIZW TA NEA DIANYSMATA POY PROKYPTOYN WS ARITHMOI
#vector 1
x11=(1,0,1,0,1,0)
y11=(0,1,0,1,0,1)
print(nominaldistance(x11,y11))
#vector 2
x22=(4,5,6,7,8)
y22=(4,5,6,7,8)
print(nominaldistance(x22,y22))
#vector 3
x33=(9,10,11,12)
y33=(13,14,15,12)
print(nominaldistance(x33,y33))

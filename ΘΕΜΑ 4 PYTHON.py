from statistics import *
import math
import numpy as np
from scipy.spatial import distance

def euclideandistance(v1,v2):
    if len(v1)==len(v2):
        zipped_vector=zip(v1,v2)
        my_sum=0
        for each in zipped_vector:
            my_sum+=pow(each[0]-each[1],2)
        return math.sqrt(my_sum)


#THEMA 4 ERWTHMA I  
#FTIAXNW TA DIANYSMATA THS ASKHSHS

#vector1
x1=(1,2,3,4,5,6)
y1= (1,2,3,4,5,6)
print(euclideandistance(x1,y1))
#vector2
x2=(-0.5, 1, 7.3, 7, 9.4, -8.2, 9, -6, -6.3)
y2=(0.5, -1, -7.3, -7, -9.4, 8.2, -9, 6, 6.3)
print(euclideandistance(x2,y2))
#vector3
x3=(-0.5, 1, 7.3, 7, 9.4, -8.2)
y3=(1.25, 9.02, -7.3, -7, 5, 1.3)
print(euclideandistance(x3,y3))
#vector4
x4=(0, 0, 0.2)
y4=(0.2, 0.2, 0)
print(euclideandistance(x4,y4))

#ERWTHMA 2

#FTIAXNW TA DIANYSMATA TOY PINAKA
A1=(25000,14,7)
A2=(42000,17,9)
A3=(55000,22,5)
A4=(27000,13,11)
A5=(58000,21,13)

#EUCLIDEANDISTANCE
print(euclideandistance(A1,A5))
print(euclideandistance(A2,A5))
print(euclideandistance(A3,A5))
print(euclideandistance(A4,A5))

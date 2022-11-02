from statistics import *
import math
import numpy as np
from scipy.spatial import distance


#euclideanDistance = sqrt((ax-bx)^2 + (ay-by)^2 + (az-bz)^2)
#euclideandistance=(sqrt(sum( (x - y)**2 for x, y in zip(x, y))))



#THEMA 4 ERWTHMA I


##################################   
#FTIAXNW TA DIANYSMATA THS ASKHSHS

    #vector1
x1=(1,2,3,4,5,6)
y1= (1,2,3,4,5,6)
vector1=np.array(x1)
vector2=np.array(y1)
print(vector1)
print(vector2)

    #vector2
x2=(-0.5, 1, 7.3, 7, 9.4, -8.2, 9, -6, -6.3)
y2=(0.5, -1, -7.3, -7, -9.4, 8.2, -9, 6, 6.3)
vector3=np.array(x2)
vector4=np.array(y2)
print(vector3)
print(vector4)

     #vector3
x3=(-0.5, 1, 7.3, 7, 9.4, -8.2)
y3=(1.25, 9.02, -7.3, -7, 5, 1.3)
vector5=np.array(x3)
vector6=np.array(y3)
print(vector5)
print(vector6)

    #vector4
x4=(0, 0, 0.2)
y4=(0.2, 0.2, 0)
vector7=np.array(x4)
vector8=np.array(y4)
print(vector7)
print(vector8)

##################

#EUCLIDEANDISTANCE

#euclideandistance vector1
from math import sqrt
x1=(1,2,3,4,5,6)
y1= (1,2,3,4,5,6)
print (sqrt(sum( (x1 - y1)**2 for x1, y1 in zip(x1, y1))))

#euclideandistance vector2
from math import sqrt
x2=(-0.5, 1, 7.3, 7, 9.4, -8.2, 9, -6, -6.3)
y2=(0.5, -1, -7.3, -7, -9.4, 8.2, -9, 6, 6.3)
print (sqrt(sum( (x2 - y2)**2 for x2, y2 in zip(x2, y2))))

#euclideandistance vector3
from math import sqrt
x3=(-0.5, 1, 7.3, 7, 9.4, -8.2)
y3=(1.25, 9.02, -7.3, -7, 5, 1.3)
print (sqrt(sum( (x3 - y3)**2 for x3, y3 in zip(x3, y3))))


#euclideandistance vector4
from math import sqrt
x4=(0, 0, 0.2)
y4=(0.2, 0.2, 0)
print (sqrt(sum( (x4 - y4)**2 for x4, y4 in zip(x4, y4))))



#################################################################

#THEMA 2

#################################

#FTIAXNW TA DIANYSMATA TOY PINAKA

A1=(25000,14,7)
A2=(42000,17,9)
A3=(55000,22,5)
A4=(27000,13,11)
A5=(58000,21,13)

vectorA1=np.array(A1)
print(vectorA1)

vectorA2=np.array(A2)
print(vectorA2)

vectorA3=np.array(A3)
print(vectorA3)

vectorA4=np.array(A4)
print(vectorA4)

vectorA5=np.array(A5)
print(vectorA5)

##################

#EUCLIDEANDISTANCE


#EUCLIDEANDISTANCE VECTORA1.5
from math import sqrt
A5=(58000,21,13)
A1=(25000,14,7)
apostasi1=print (sqrt(sum( (A1 - A5)**2 for A1, A5 in zip(A1, A5))))

#EUCLIDEANDISTANCE VECTORA2.5
from math import sqrt
A5=(58000,21,13)
A2=(42000,17,9)
apostasi2=print (sqrt(sum( (A2 - A5)**2 for A2, A5 in zip(A2, A5))))

#EUCLIDEANDISTANCE VECTORA3.5
from math import sqrt
A5=(58000,21,13)
A3=(55000,22,5)
apostasi3=print (sqrt(sum( (A3 - A5)**2 for A3, A5 in zip(A3, A5))))

#EUCLIDEANDISTANCE VECTORA14.5
from math import sqrt
A5=(58000,21,13)
A4=(27000,13,11)
apostasi4=print (sqrt(sum( (A4 - A5)**2 for A4, A5 in zip(A4, A5))))


#if apostasi1<apostasi2 and apostasi1<apostasi3 and apostasi1<apostasi4:
          # print("Ο ΧΡΗΣΤΗΣ Α1 ΤΑΙΡΙΑΖΕΙ ΠΕΡΙΣΣΟΤΕΡΟ ΣΤΟΝ ΧΡΗΣΤΗ 5")



#if apostasi2<apostasi1 and apostasi2<apostasi3 and apostasi2<apostasi4 :
          # print("Ο ΧΡΗΣΤΗΣ Α2 ΤΑΙΡΙΑΖΕΙ ΠΕΡΙΣΣΟΤΕΡΟ ΣΤΟΝ ΧΡΗΣΤΗ 5")



#if apostasi3<apostasi1 and apostasi3<apostasi2 and apostasi3<apostasi4:
          # print("Ο ΧΡΗΣΤΗΣ Α3 ΤΑΙΡΙΑΖΕΙ ΠΕΡΙΣΣΟΤΕΡΟ ΣΤΟΝ ΧΡΗΣΤΗ 5")



#if apostasi4<apostasi1 and apostasi4<apostasi2 and apostasi4<apostasi3:
           #print("Ο ΧΡΗΣΤΗΣ Α4 ΤΑΙΡΙΑΖΕΙ ΠΕΡΙΣΣΟΤΕΡΟ ΣΤΟΝ ΧΡΗΣΤΗ 5")



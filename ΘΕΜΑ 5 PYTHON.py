
from statistics import *
import math
import numpy as np
from scipy.spatial import distance
from numpy.linalg import norm


#SYNARTHSH SYNHMITONOY

####cosine = np.dot(x,y)/(norm(x)*norm(y))


##################################################################




#ORISMOS DIANYSMATWN

#1
x1=(9.32, -8.3, 0.2) 
y1= (-5.3, 8.2, 7)

#2
x2=(6.5, 1.3, 0.3, 16, 2.4, -5.2, 2, -6, -6.3)
y2=(0.5, -1, -7.3, -7, -9.4, 8.2, -9, 6, 6.3)

#3
x3=(-0.5, 1, 7.3, 7, 9.4, -8.2)
y3=(1.25, 9.02, -7.3, -7, 15, 12.3)

#4
x4=(2, 8, 5.2)
y4=(2, 8, 5.2)

##################################################################


#EMFANISH DIANYSMATWN


####1
x1=(9.32, -8.3, 0.2) 
y1= (-5.3, 8.2, 7)
vector1=np.array(x1)
vector2=np.array(y1)
print(vector1)
print(vector2)


####2
x2=(6.5, 1.3, 0.3, 16, 2.4, -5.2, 2, -6, -6.3)
y2=(0.5, -1, -7.3, -7, -9.4, 8.2, -9, 6, 6.3)
vector3=np.array(x2)
vector4=np.array(y2)
print(vector3)
print(vector4)


####3
x3=(-0.5, 1, 7.3, 7, 9.4, -8.2)
y3=(1.25, 9.02, -7.3, -7, 15, 12.3)
vector5=np.array(x3)
vector6=np.array(y3)
print(vector5)
print(vector6)

####4
x4=(2, 8, 5.2)
y4=(2, 8, 5.2)
vector7=np.array(x4)
vector8=np.array(y4)
print(vector7)
print(vector8)


#YPOLOGISMOS SYNHMITONOY 1.2
cosine = np.dot(x1,y1)/(norm(x1)*norm(y1))
print("Cosine Similarity:", cosine)

#YPOLOGISMOS SYNHMITONOY 3.4
cosine = np.dot(x2,y2)/(norm(x2)*norm(y2))
print("Cosine Similarity:", cosine)

#YPOLOGISMOS SYNHMITONOY 5.6
cosine = np.dot(x3,y3)/(norm(x3)*norm(y3))
print("Cosine Similarity:", cosine)

#YPOLOGISMOS SYNHMITONOY 7.8
cosine = np.dot(x4,y4)/(norm(x4)*norm(y4))
print("Cosine Similarity:", cosine)

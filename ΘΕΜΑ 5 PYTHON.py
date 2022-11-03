from statistics import *
import math
import numpy as np
from scipy.spatial import distance
from numpy.linalg import norm
#SYNARTHSH SYNHMITONOY
####cosine = np.dot(x,y)/(norm(x)*norm(y))
def cosine_similarity(v1,v2):
    if len(v1)==len(v2):
        sumxx=0
        sumyy=0
        sumxy=0
        for i in range(len(v1)):
            x = v1[i]; y = v2[i]
            sumxx+=x*x
            sumyy+=y*y
            sumxy+=x*y
        return sumxy/math.sqrt(sumxx*sumyy)
#ORISMOS DIANYSMATWN
#1
x1, y1 = [9.32, -8.3, 0.2],[-5.3, 8.2 , 7]
print(x1, y1, cosine_similarity(x1,y1))
#2
x2,y2=[6.5, 1.3, 0.3, 16, 2.4, -5.2, 2, -6, -6.3],[0.5, -1, -7.3, -7, -9.4, 8.2, -9, 6, 6.3]
print(x2, y2, cosine_similarity(x2,y2))
#3
x3,y3,=[-0.5, 1, 7.3, 7, 9.4, -8.2],[1.25, 9.02, -7.3, -7, 15, 12.3]
print(x3, y3, cosine_similarity(x3,y3))
#4
x4,y4=[2, 8, 5.2],[2, 8, 5.2]
print(x4, y4, cosine_similarity(x4,y4))


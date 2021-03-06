import cv2
from numpy import *
def RGBtol(img):
    RGBtoLMS=array([[0.3811,0.5783,0.0402],
          [0.1967,0.7244,0.0782],
          [0.0241,0.1288,0.8444]]);
    temp0=array([[1/sqrt(3),0,0],
                  [0,1/sqrt(6),0],
                  [0,0,1/sqrt(2)]])
    temp1=array([[1,1,1],
                 [1,1,-2],
                 [1,-1,0]])
    LMStol=dot(temp0,temp1)
    temp2=array([[1,1,1],
                 [1,1,-1],
                 [1,-2,0]])
    temp3=array([[sqrt(3)/3,0,0],
                 [0,sqrt(6)/6,0],
                 [0,0,sqrt(2)/2]])
    ltoLMS=dot(temp2,temp3)
    LMStoRGB=array([[4.4679,-3.5873,0.1193],
                    [-1.2186,2.3809,-0.1624],
                    [0.0497,-0.2439,1.2045]])
    Z=array(img.reshape((-1,3)))
    Z=array([Z[:,2],Z[:,1],Z[:,0]])
    LMS=dot(RGBtoLMS,Z)
    LMS=log(LMS+0.001)
    l=dot(LMStol,LMS)
    return l
    

import cv2
from numpy import *
def ltoRGB(l):
    
    temp2=array([[1,1,1],
                 [1,1,-1],
                 [1,-2,0]])
    temp3=array([[sqrt(3)/3,0,0],
                 [0,sqrt(6)/6,0],
                 [0,0,sqrt(2)/2]])
    ltoLMS=dot(temp2,temp3)
    LMStoRGB=array(
        [[4.4679,-3.5873,0.1193],
         [-1.2186,2.3809,-0.1624],
         [0.0497,-0.2439,1.2045]
         ]
        );

    LMS=dot(ltoLMS,l)
    LMS=exp(LMS)
    RGB=dot(LMStoRGB,LMS)
    RGB=array([RGB[2,:],RGB[1,:],RGB[0,:]])
    RGB[RGB>255]=255
    RGB[RGB<0]=0
    RGB=RGB.T
    print RGB.shape
    return RGB


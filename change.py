import cv2
from numpy import *
def change(l_s,l_d):
    row,N=l_s.shape
    ave_s=average(l_s.T,0)
    stdd_s=std(l_s.T,0)
    for i in range(1,N):
        l_s[:,i]=l_s[:,i]-ave_s;
    print N 
    return l_d

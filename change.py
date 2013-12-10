import cv2
from numpy import *
def change(l_s,l_t):
    row,N=l_s.shape
    ave_s=average(l_s.T,0)
    ave_t=average(l_t.T,0)
    std_s=std(l_s.T,0)
    std_t=std(l_t.T,0)
    l_s=l_s-ave_s[:,None]
    trans=(std_t/std_s)
    trans=array([[trans[0],0,0],
                 [0,trans[1],0],
                 [0,0,trans[2]]])
    l_s=dot(trans,l_s)
    l_s=l_s+ave_t[:,None]
    return l_s

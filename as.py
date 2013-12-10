import cv2
from numpy import *
from RGBtol import *
from ltoRGB import *
from change import *
filename_s = '/home/gq/Desktop/dog.jpg'
filename_d = '/home/gq/Desktop/tree.jpg'
img_s= cv2.imread(filename_s)
img_d=cv2.imread(filename_d)
l_s=RGBtol(img_s)
l_d=RGBtol(img_d)
l_d=change(l_s,l_d)
RGB=ltoRGB(l_d)
zz=array(RGB.reshape(img_d.shape))
zz=zz.astype('uint8')
cv2.imshow('f',zz)
cv2.waitKey(0)



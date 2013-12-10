import cv2
from numpy import *
from RGBtol import *
from ltoRGB import *
from change import *
filename_s = '/home/gq/Desktop/car1.jpg'
filename_t = '/home/gq/Desktop/car2.jpg'
img_s= cv2.imread(filename_s)
img_t=cv2.imread(filename_t)

l_s=RGBtol(img_s)
l_t=RGBtol(img_t)
l_s=change(l_s,l_t)
RGB=ltoRGB(l_s)
zz=array(RGB.reshape(img_t.shape))
zz=zz.astype('uint8')
cv2.imshow('f',zz)
cv2.waitKey(0)



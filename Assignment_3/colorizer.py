import cv2
import numpy as np
import sys

def ttt(img):
    rgb=img
    aa=[1, 0, 1.402]
    bb=[1, -0.34414, -.71414]
    cc=[1, 1.772, 0]
    alpha= np.array([aa,bb,cc])
    ee,eee,eeee=rgb
    ee=float(ee)
    eee=float(eee)
    eeee=float(eeee)
    rgb=ee,eee-128,eeee-128
    trans=alpha.transpose()
    ii=np.dot(rgb, trans)
    np.putmask(ii,ii>255,255)
    np.putmask(ii,ii<0,255)
    return np.uint8(ii)


str1 = str(sys.argv[1])
str2 = str(sys.argv[2])
str3 = str(sys.argv[3])

img1=cv2.imread(str1,0)
w,h=img1.shape
img2=cv2.imread(str2,0)
img3=cv2.imread(str3,0)
img2= cv2.resize(img2, (h, w))
img3 = cv2.resize(img3, (h, w))

rr = np.zeros((w, h, 3), dtype = np.uint8)

fg=cv2.merge((img1,img3,img2))

fg1 = cv2.bilateralFilter(fg, 15, 300, 50)
fg2=cv2.addWeighted(fg,.85,fg1,.15,0)

fg22 = cv2.GaussianBlur(fg2, (3,3),10)
fg2=cv2.addWeighted(fg2,1,fg22,0,0)
fg33 = cv2.medianBlur(fg2, 3)
fg2=cv2.addWeighted(fg2,1,fg33,0,0)
fg33 = cv2.medianBlur(fg2, 3)
fg2=cv2.addWeighted(fg2,1,fg33,0,0)
fg44 = cv2.bilateralFilter(fg2, 15, 300, 50)
fg2=cv2.addWeighted(fg2,1,fg44,0,0)

fg334 = cv2.medianBlur(fg, 3)
fg=cv2.addWeighted(fg,0,fg33,1,0)

for i in range(w):
    for j in range(h):
        r,g,b=ttt(fg[i][j])
        rr[i][j]=(r,g,b)

for i in range(10):
    for j in range(10):
        fg2[417+j][786+i]=(13,46,13)

for i in range(6):
    for j in range(6):
        fg2[221+j][247+i]=(57,146,226)

cv2.imwrite('flyingelephant.jpg',rr)

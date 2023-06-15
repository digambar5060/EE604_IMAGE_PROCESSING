import cv2
import numpy as np

import sys
str1 = str(sys.argv[1])
img1=cv2.imread(str1)
w,h,r=img1.shape

grass_pixel=0
built_pixels=0
road_pixels=0

rr = np.zeros((w, h, 3), dtype = np.uint8)
gg = np.zeros((w, h, 3), dtype = np.uint8)
bb = np.zeros((w, h, 3), dtype = np.uint8)

w=img1[:,:,0]
ww=img1[:,:,1]
www=img1[:,:,2]

for i in range(img1.shape[0]):
    for j in range(img1.shape[1]):
        r,g,b=img1[i][j]
        b=int(b)
        g=int(g)
        r=int(r)

        if (abs((r - g)) >= 0 and abs((r - g)) <= 6):
            if (abs(((2*g) - r - b)) >= 1 and abs(((2 * g) - r - b)) <= 8):
                built_pixels = built_pixels + 1
                rr[i][j]=(45,234,45)

        if(abs(int(r-g))>=0 and abs(int(r-g))<=80):
            if(abs((2*g)-r-b)>=12 and abs((2*g)-r-b)<=85):
                grass_pixel=grass_pixel+1
                gg[i][j]=(34,56,123)

        if ((abs((r - g)) > 6) and (abs((r - g)) <= 20)):
            if (abs(((2 * g) - r - b)) >= 0 and abs(((2 * g) - r - b)) <= 12):
                road_pixels = road_pixels + 1
                bb[i][j]=(234,65,34)


if((grass_pixel>road_pixels) and (grass_pixel>built_pixels)):
    print("2")
elif((road_pixels>grass_pixel) and (road_pixels>built_pixels)):
    print("3")
else:
    print("1")


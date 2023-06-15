import cv2
import numpy as np
from PIL import Image
import sys

def medianblur(arr, filtersize):
    t = []
    ind = filtersize // 2
    result = []
    result = numpy.zeros((len(arr),len(arr[0])))
    for i in range(len(arr)):

        for j in range(len(arr[0])):

            for z in range(filtersize):
                if i + z - ind < 0 or i + z - ind > len(arr) - 1:
                    for c in range(filtersize):
                        t.append(0)
                else:
                    if j + z - ind < 0 or j + ind > len(arr[0]) - 1:
                        t.append(0)
                    else:
                        for k in range(filtersize):
                            t.append(arr[i + z - ind][j + k - ind])

            t.sort()
            result[i][j] = t[len(t) // 2]
            t = []
    return result

string = str(sys.argv[1])
img = cv2.imread(string)

b = img[:,:,0]
g = img[:,:,1]
r = img[:,:,2]

alpha=cv2.dilate
beta=cv2.medianBlur
yama=cv2.absdiff

kernel1=np.ones((7,7),np.uint8)
k1=alpha
img1 = k1(b, kernel1,10)
m1=beta
img12 = m1(img1, 77)
a1=yama
img13 = 255 - a1(b, img12)


kernel2=np.ones((7,7),np.uint8)
k2=alpha
img2 = k2(g, kernel2,10)
m2=beta
img22 = m2(img2, 77)
a2=yama
img23 = 255 - a2(g, img22)

kernel3=np.ones((7,7),np.uint8)
k3=alpha
img3 = k3(r, kernel3,10)
m3=beta
img32 = m3(img3, 77)
a3=yama
img33 = 255 - a3(r, img32)

image=cv2.merge
image_m = image([img13,img23,img33])

cv2.imwrite('cleaned-gutter.jpg', image_m)


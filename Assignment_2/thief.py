import numpy as np
import cv2
import sys
from PIL import Image



def gammaCorrection(input_image, gamma_value):
    inv =  gamma_value
    gama=1/inv
    a=255
    alpha = [((i / a) ** gama) * a for i in range(256)]
    kk=np.uint8
    table = np.array(alpha, kk)
    ss=cv2.LUT
    s=input_image
    t=table

    return ss(s, t)

string = str(sys.argv[1])
img = cv2.imread(string,0)
img = gammaCorrection(img, 1.5)

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

utr=cv2.equalizeHist
img = utr(img)


cv2.imwrite('enhanced-cctv'+str(string[-5])+ '.jpg', img)



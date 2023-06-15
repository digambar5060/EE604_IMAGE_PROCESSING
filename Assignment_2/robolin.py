import cv2
import numpy as np
import sys

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
img = cv2.imread(string)


yamma_val=0.6
img1 = gammaCorrection(img, yamma_val)

r1=cv2.cvtColor
r2=cv2.COLOR_BGR2GRAY
img2 = r1(img1, r2)

det=cv2.Canny
th1=120
th2=180
apertureSize=3
black_img = det(img2, th1, th2, apertureSize)


lines_array = []
line_detection=cv2.HoughLinesP
pixels=1
fun1=np.pi
u=180
angle=fun1/u
th=91
len=20
minl=len
maxl=79


resolution= line_detection(
    black_img,
    pixels,
    angle,
    th,
    minl,
    maxLineGap=79
)

for bindu in resolution:
    yy=bindu[0]
    aa, bb, cc, dd = yy
    brac1=(aa,bb)
    brac2=(cc,dd)
    a=255
    colour=(0,a,0)
    line_thickness=2
    func2=cv2.line
    func2(img1, brac1, brac2, colour, line_thickness)
    appendd=lines_array.append
    appendd([brac1, brac2])

cv2.imwrite('robolin-tiles'+ str(string[-5]) + '.jpg', img1)

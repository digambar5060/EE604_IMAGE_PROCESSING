import cv2
import numpy as np
import sys

image = str(sys.argv[1])
alpha=int(image[-5])
image = cv2.imread(image)




img1=image[:,:,0]
img2=image[:,:,1]
img3=image[:,:,2]
img = cv2.merge([img3,img2,img1])

alt=cv2.GaussianBlur
filter1 = alt(img, (3, 3), 10)
filter1=cv2.addWeighted(img,.99,filter1,0.01,0)

for i in range(5):
    filter1 = alt(img, (3, 3), 10)
    filter1=cv2.addWeighted(img,.99,filter1,0.01,0)

alt1=cv2.bilateralFilter
filter2 = alt1(filter1, 3, 75, 75)
filter2 = cv2.addWeighted(filter1, .8, filter2, .1, 0)

for i in range(5):
    filter2 = alt1(filter2, 3, 75, 75)
    filter2 = cv2.addWeighted(filter2, .8, filter2, .1, 0)


alt2=cv2.medianBlur
filter3 = alt2(filter2, 11)
filter3= cv2.addWeighted(filter2, 1, filter3, 0.1, 0)

for i in range(5):
    filter3 = alt2(filter3, 11)
    filter3= cv2.addWeighted(image, 1, filter3, 0.1, 0)

if alpha==1:
    alt3=cv2.fastNlMeansDenoisingColored
    image= alt3(filter3,None,6,9,9,15)
else:
    alt3 = cv2.fastNlMeansDenoisingColored
    image = alt3(filter3, None, 4, 5, 5, 21)

img1=image[:,:,0]
img2=image[:,:,1]
img3=image[:,:,2]
image = cv2.merge([img1,img2,img3])

cv2.imwrite('denoised.jpg', image)
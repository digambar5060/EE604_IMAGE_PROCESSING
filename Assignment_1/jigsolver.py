import cv2
import numpy as np
import sys
s=str(sys.argv[1])
img=cv2.imread(s)

part1=img[200:400,0:190]
part11=img[0:200,0:190,[1,0,2]]
part1=cv2.addWeighted(part11,1,part1,0,0)

part2=img[210:410,0:190]
part2=cv2.flip(part2,0)
part21=img[0:200,0:190]
part2=cv2.addWeighted(part2,1,part21,0,0)


part3=img[150:330,515:700]
part3=cv2.flip(part3,1)
part31=img[150:330,515:700]
part3=cv2.addWeighted(part3,1,part31,0,0)

part4=img[370:421,370:797]
part4=cv2.flip(part4,0)
part41=img[370:421,370:797]
part4=cv2.addWeighted(part4,1,part41,0,0)

part5=img[395:400,0:190]

part6=img[410:415,0:190]
part6=cv2.flip(part6,0)

img[200:400,0:190]=part1
img[0:200,0:190]=part2
img[150:330,515:700]=part3
img[370:421,370:797]=part4
img[400:405,0:190]=part5
img[405:410,0:190]=part6


cv2.imwrite('jigsolved.jpg',img)

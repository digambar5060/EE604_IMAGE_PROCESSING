import numpy as np
import cv2
import sys

def make_image(k):
    img = np.zeros((300, 500), dtype=np.uint8)
    part={}
    part['1'] = [[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]]
    part['2'] = [[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]]

    radious = 25
    dist = 35
    circle_dist = 5

    arr = part['1']
    for i in range(5):
        for j in range(3):
            if arr[i][j]:
                centre = (dist + circle_dist + 2 * circle_dist * (j) + radious + 2 * radious * j,
                          circle_dist + 2 * circle_dist * (i) + radious + 2 * radious * i)
                img1 = cv2.circle(img, centre, radious, (255), -1)

    dist = 6 * radious + 6 * circle_dist + 3 * dist

    arr = part['2']
    for i in range(5):
        for j in range(3):
            if arr[i][j]:
                centre = (dist + circle_dist + 2 * circle_dist * (j) + radious + 2 * radious * j,
                          circle_dist + 2 * circle_dist * (i) + radious + 2 * radious * i)
                img2 = cv2.circle(img1, centre, radious, (255), -1)

    if (int(k) < 10 and len(k)<2):
        first_digit = '0'
        second_digit = k;
    else:
        first_digit = k[0]
        second_digit = k[1]
    p = {}
    p['0'] = [[0, 0, 0], [0, 1, 0], [0, 1, 0], [0, 1, 0], [0, 0, 0]]
    p['1'] = [[1, 0, 1], [1, 0, 1], [1, 0, 1], [1, 0, 1], [1, 0, 1]]
    p['2'] = [[0, 0, 0], [1, 1, 0], [0, 0, 0], [0, 1, 1], [0, 0, 0]]
    p['3'] = [[0, 0, 0], [1, 1, 0], [0, 0, 0], [1, 1, 0], [0, 0, 0]]
    p['4'] = [[0, 1, 0], [0, 1, 0], [0, 0, 0], [1, 1, 0], [1, 1, 0]]
    p['5'] = [[0, 0, 0], [0, 1, 1], [0, 0, 0], [1, 1, 0], [0, 0, 0]]
    p['6'] = [[0, 0, 0], [0, 1, 1], [0, 0, 0], [0, 1, 0], [0, 0, 0]]
    p['7'] = [[0, 0, 0], [1, 1, 0], [1, 1, 0], [1, 1, 0], [1, 1, 0]]
    p['8'] = [[0, 0,0], [0, 1, 0], [0, 0, 0], [0, 1, 0], [0, 0, 0]]
    p['9'] = [[0, 0, 0], [0, 1, 0], [0, 0, 0], [1, 1, 0], [0, 0, 0]]

    dist = 35

    arr = p[first_digit]
    for i in range(5):
        for j in range(3):
            if arr[i][j]:
                centre = (dist + circle_dist + 2 * circle_dist * (j) + radious + 2 * radious * j,
                          circle_dist + 2 * circle_dist * (i) + radious + 2 * radious * i)
                img3 = cv2.circle(img2, centre, radious, (0), -1)

    dist = 6 * radious + 6 * circle_dist + 3 * dist

    arr = p[second_digit]
    for i in range(5):
        for j in range(3):
            if arr[i][j]:
                centre = (dist + circle_dist + 2 * circle_dist * (j) + radious + 2 * radious * j,
                          circle_dist + 2 * circle_dist * (i) + radious + 2 * radious * i)
                img4 = cv2.circle(img3, centre, radious, (0), -1)

    return np.uint8(img4)

number1 = str(sys.argv[1])
image = make_image(number1)

cv2.imwrite('dotmatrix.jpg ',image)

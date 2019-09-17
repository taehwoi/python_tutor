import cv2 as cv
import numpy as np

"""copied from opencv docs & modified to use the simpsons"""
img_rgb = cv.imread('simpsons.jpeg')
img_gray = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)
template = cv.imread('eyes3.jpeg',0)
w, h = template.shape[::-1]

"""cv2 has this match function already implemented"""
res = cv.matchTemplate(img_gray,template,cv.TM_CCOEFF_NORMED)
threshold = 0.8
loc = np.where( res >= threshold)
# draw a rectangle around the result
for pt in zip(*loc[::-1]):
    cv.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)

cv.imwrite('res.png', img_rgb) # save
cv.imshow('res.png',img_rgb) # show result
cv.waitKey(0) # if no wait, result window closes right away
cv.destroyAllWindows()

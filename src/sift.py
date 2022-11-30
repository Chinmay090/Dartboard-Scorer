# Applying the SIFT algorithm. This can be used on the dartboard image to correct offset caused by camera position.
# This method is being tested on a separate image to show that it works. This image is not the dartboard image.
# Again, this code is just here for demonstration purposes and will be added separately to the .ipynb file.

import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

im1 = cv.imread('Neymar1.jfif',0)
im2 = cv.imread('Neymar2.jfif',0)

sift = cv.xfeatures2d.SIFT_create()
kp1, dsc1 = sift.detectAndCompute(im1,None)
kp2, dsc2 = sift.detectAndCompute(im2,None)

matcher = cv.BFMatcher(cv.NORM_L1, True)

matches = matcher.match(dsc1,dsc2)
matches = sorted(matches, key = lambda x:x.distance)

im3 = cv.drawMatches(im1, kp1, im2, kp2, matches[:50], im2, flags=3)

cv.imshow("Difference Matching",im3)
cv.waitKey(0)
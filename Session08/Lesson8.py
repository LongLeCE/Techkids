import cv2
import numpy as np
# read Image
I1 = cv2.imread("D:\\Python\\Lesson 1\\Lesson8\\1.png")
cv2.imshow("Image1", I1)
# compute SIFT
gray1 = cv2.cvtColor(I1, cv2.COLOR_RGB2GRAY)
sift1 = cv2.xfeatures2d.SIFT_create()
kpt1, des1 = sift1.detectAndCompute(gray1, None)
cv2.drawKeypoints(I1, kpt1, I1)
cv2.imshow("keypoint1", I1)
index_good = -1
max_point = -1
for i in range(1, 9):
    file = "D:\\Python\\Lesson 1\\Lesson8\\"+str(i)+".png"
    I2 = cv2.imread(file)
    gray2 = cv2.cvtColor(I2, cv2.COLOR_RGB2GRAY)
    sift2 = cv2.xfeatures2d.SIFT_create()
    kpt2, des2 = sift2.detectAndCompute(gray2, None)
    # Matching Brute force
    bf = cv2.BFMatcher_create()
    matches = bf.knnMatch(des1, des2, 2)  # knn: k nearest neighbor
    OutImg = cv2.drawMatchesKnn(I1, kpt1, I2, kpt2, matches, None)
    cv2.imshow("matching", OutImg)
    # Choose good matches
    good = []
    for m, n in matches:
        if m.distance < 0.2 * n.distance:
            good.append([m])
    if len(good) > max_point:
        max_point = len(good)
        index_good = i
    # OutImg2 = cv2.drawMatchesKnn(I1, kpt1, I2, kpt2, good, None)
    # cv2.imshow("matching good", OutImg2)
    # cv2.waitKey()
file = "D:\\Python\\Lesson 1\\Lesson8\\"+str(index_good)+".png"
I2 = cv2.imread(file)
cv2.imshow("best matching", I2)
cv2.waitKey()

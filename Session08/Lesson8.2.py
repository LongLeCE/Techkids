import cv2
import numpy as np
# read Image
I1 = cv2.imread("D:\\Python\\Lesson 1\\Lesson8\\1.png")
cv2.imshow("Image1", I1)
cv2.waitKey(1)
# anh muon chen
pattern = cv2.imread("D:\\Python\\Lesson 1\\Lesson8\\2.png")
pattern = cv2.resize(pattern, (I1.shape[1], I1.shape[0]))
# tao mask
mask = np.ones_like(I1, dtype=np.float32)
cv2.imshow("mask", mask)
# compute SIFT
gray1 = cv2.cvtColor(I1, cv2.COLOR_RGB2GRAY)
sift1 = cv2.xfeatures2d.SIFT_create()
kpt1, des1 = sift1.detectAndCompute(gray1, None)
# cv2.drawKeypoints(I1, kpt1, I1)
# cv2.imshow("keypoint1", I1)
file = cv2.VideoCapture(0)
while True:
    _, I2 = file.read()
    gray2 = cv2.cvtColor(I2, cv2.COLOR_RGB2GRAY)
    sift2 = cv2.xfeatures2d.SIFT_create()
    kpt2, des2 = sift2.detectAndCompute(gray2, None)
    # Matching Brute force
    bf = cv2.BFMatcher_create()
    matches = bf.knnMatch(des1, des2, 2)  # knn: k nearest neighbor
    # OutImg = cv2.drawMatchesKnn(I1, kpt1, I2, kpt2, matches, None)
    # cv2.imshow("matching", OutImg)
    # Choose good matches
    good = []
    new_good = []
    for m, n in matches:
        if m.distance < 0.4 * n.distance:
            good.append([m])
            new_good.append(m)
    # find Homography
    srcPoints = np.float32([kpt1[m.queryIdx].pt for m in new_good]).reshape(-1, 1, 2)
    dstPoints = np.float32([kpt2[m.trainIdx].pt for m in new_good]).reshape(-1, 1, 2)
    M, H = cv2.findHomography(srcPoints, dstPoints)
    w = gray1.shape[1]
    h = gray1.shape[0]
    n_corners = np.float32([[0, 0], [w - 1, 0], [w - 1, h - 1], [0, h - 1]]).reshape(-1, 1, 2)
    if M is not None:
        # find new corner on Image through homography
        npts = cv2.perspectiveTransform(n_corners, M)
        cv2.polylines(I2, np.int32([npts]), True, (0, 0, 255), 5)
        blend_mask = cv2.warpPerspective(mask, M, (I2.shape[1], I2.shape[0]))
        new_pattern = cv2.warpPerspective(pattern, M, (I2.shape[1], I2.shape[0]))
        im4 = I2 * (1 - blend_mask) + new_pattern
        cv2.imshow("blend", blend_mask)
        im4 = cv2.convertScaleAbs(im4)
        cv2.imshow("insert", im4)
    cv2.imshow("result", I2)
    cv2.waitKey(30)

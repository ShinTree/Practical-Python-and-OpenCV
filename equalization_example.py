import cv2
import numpy as np
oi = cv2.imread('dark.png',0)
ei = cv2.equalizeHist(oi)
result = np.hstack((oi,ei)) #stacking images side-by-side
cv2.imshow("ori-eq",result)
cv2.imwrite('equalize.png',result)

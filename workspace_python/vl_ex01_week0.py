import skimage
from skimage import data
import cv2
image = data.coins()
print("width: {} pixels".format(image.shape[1]))
print("height: {} pixels".format(image.shape[0]))
cv2.imshow("Image", image)
cv2.waitKey(0)

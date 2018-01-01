import cv2
import numpy as np

img = cv2.imread("cat.jpg")

b = np.zeros((img.shape[0], img.shape[1]), dtype=img.dtype)
g = np.zeros((img.shape[0], img.shape[1]), dtype=img.dtype)
r = np.zeros((img.shape[0], img.shape[1]), dtype=img.dtype)

b[:, :] = img[:, :, 0]
g[:, :] = img[:, :, 1]
r[:, :] = img[:, :, 2]

merged = cv2.merge([b, g, r])
print("Merge by OpenCV")
print(merged.strides)
print(merged)

mergedByNp = np.dstack([b, g, r])
print("Merge by NumPy ")

print("mergedByNp.strides")

print("mergedByNp")

cv2.imshow("Merged", merged)
cv2.imshow("MergedByNp", merged)
cv2.imshow("Blue", b)
cv2.imshow("Red", r)
cv2.imshow("Green", g)
cv2.waitKey(0)
cv2.destroyAllWindows()

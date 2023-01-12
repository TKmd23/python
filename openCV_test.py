import cv2
import numpy as np
import matplotlib.pyplot as plt

# cv_img = cv2.imread("foto/checkerboard_18x18.png", 0)
# cv_img = cv2.imread("foto/checkerboard_fuzzy_18x18.jpg", 0)
# cv_img = cv2.imread("foto/coca-cola-logo.png", 1)
# cv_img = cv2.imread("foto/New_Zealand_Lake.jpg", cv2.IMREAD_COLOR)
cv_img = cv2.imread("foto/New_Zealand_Lake.jpg", cv2.COLOR_BGR2RGB)

# b, g, r = cv2.split(cv_img)
h,s,v = cv2.split(cv_img)

# print(cv_img)
# print("Image size", cv_img.shape)
# print("Image size", cv_img.dtype)
# cv_img = cv_img[:, :, ::-1]
# plt.imshow(cv_img, cmap="gray")

plt.figure(figsize=[20, 5])
# plt.subplot(141); plt.imshow(r, cmap="gray"); plt.title("Red")
# plt.subplot(142); plt.imshow(g, cmap="gray"); plt.title("Green")
# plt.subplot(143); plt.imshow(b, cmap="gray"); plt.title("Blue")
plt.subplot(141); plt.imshow(h, cmap="gray"); plt.title("H")
plt.subplot(142); plt.imshow(s, cmap="gray"); plt.title("S")
plt.subplot(143); plt.imshow(v, cmap="gray"); plt.title("V")


# imgMerged = cv2.merge((b,g,r))
# plt.subplot(144); plt.imshow(imgMerged[:,:,::-1]); plt.title("Output")
plt.subplot(144); plt.imshow(cv_img); plt.title("Original")

# plt.imshow(cv_img)
plt.show()
cv2.imwrite("Test foto.png", cv_img)
# cv2.waitKey()
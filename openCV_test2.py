import cv2
import matplotlib.pyplot as plt

cb_img = cv2.imread("foto/checkerboard_color.png")
coke_img = cv2.imread("foto/coca-cola-logo.png")

plt.imshow(cb_img)
plt.title("mat show")
plt.show()

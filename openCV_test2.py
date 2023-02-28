import cv2
import matplotlib.pyplot as plt

cb_img = cv2.imread("foto/checkerboard_color.png")
coke_img = cv2.imread("foto/coca-cola-logo.png")
cokeImg = coke_img.copy()

# flip = cv2.flip(coke_img, -1)

# cv2.line(cokeImg, (100,100), (400, 100), (0, 255, 255), thickness=5, lineType=cv2.LINE_AA)
# cv2.circle(cokeImg, (190,318), 150, (0, 255, 255), thickness=3)
# sText = cv2.putText(cokeImg,
#                     text="Test text",
#                     org=(100, 100),
#                     fontFace=cv2.FONT_HERSHEY_PLAIN,
#                     fontScale=3,
#                     color=(0, 255, 255),
#                     thickness=3,
#                     )

plt.imshow(cokeImg[:,:,::-1])
plt.title("mat show")
plt.show()

import cv2
import matplotlib.pyplot as plt

img_bgr = cv2.imread("foto/coca-cola-logo.png")
img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
plt.imshow(img_rgb)
print(img_rgb.shape)
# plt.show()
logo_w = img_rgb.shape[0]
logo_h = img_rgb.shape[1]

back_bgr = cv2.imread("foto/checkerboard_color.png")
back_rgb = cv2.cvtColor(back_bgr, cv2.COLOR_BGR2RGB)
asp_ratio = logo_w / back_rgb.shape[1]
dim = (logo_w, int(back_rgb.shape[0] * asp_ratio))

back_rgb = cv2.resize(back_rgb, dim, interpolation=cv2.INTER_AREA)

plt.imshow(back_rgb)
print(back_rgb.shape)

img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)
retval, img_mask = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY)
plt.imshow(img_mask, cmap="gray")
print(img_mask.shape)

img_mask_inv = cv2.bitwise_not(img_mask)

img_back = cv2.bitwise_and(back_rgb, back_rgb, mask=img_mask)
plt.imshow(img_back)

img_forw = cv2.bitwise_and(img_rgb, img_rgb, mask=img_mask_inv)
plt.imshow(img_forw)

result = cv2.add(img_back, img_forw)
plt.imshow(result)
cv2.imwrite("foto/logo_final.png", result[:, :, ::-1])
plt.show()

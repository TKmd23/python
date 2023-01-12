import cv2 as cv
from PIL import Image

image_path = "cat4.jpg"
cat_face_cascade = cv.CascadeClassifier("haarcascade_frontalcatface_extended.xml")
img = cv.imread(image_path)
cat_face = cat_face_cascade.detectMultiScale(img)
# print(cat_face)

cat = Image.open(image_path)
glasses = Image.open("glasses.png")

cat = cat.convert("RGBA")
glasses = glasses.convert("RGBA")

for (x,y,w,h) in cat_face:
    # cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)
    glasses = glasses.resize((w, int(h/3)))
    cat.paste(glasses, (x, int(y+h/4)), glasses)
    cat.save("cat_glasses.png")
cat_glasses = cv.imread("cat_glasses.png")
cv.imshow("Cat", cat_glasses)
k = cv.waitKey()
# if k == ord("s"):
#     cv.imwrite("test_img.png", img)



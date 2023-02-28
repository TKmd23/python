import cv2
from PIL import Image

image_path = "1.jpg"
cat_face_cascade = cv2.CascadeClassifier("haarcascade_frontalcatface_extended.xml")
image = cv2.imread(image_path)
cat_face = cat_face_cascade.detectMultiScale(image)

cat = Image.open(image_path)
glasses = Image.open("glasses.png")
cat = cat.convert("RGBA")
glasses = glasses.convert("RGBA")

print(image.shape)
print(cat_face)
for (x, y, w, h) in cat_face:
    glasses = glasses.resize((w, int(h/3)))
    cat.paste(glasses, (x, int(y+h/3.5)), glasses)
    # cv2.rectangle(image, (x, y), (x+w, y+h), (0, 0, 255), 3)
cat.save("test_cat_29.png")





cat_glass = cv2.imread("test_cat_29.png")

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(cat_glass,'Final Work', (0,100), font, 2,(0,0,255),3,cv2.LINE_AA)
cv2.line(cat_glass,(0,120),(320,120),(255,0,0),5)

cv2.imshow("New Cat", cat_glass)
cv2.waitKey()








# cv2.imshow("Cat", image)
# cv2.waitKey()

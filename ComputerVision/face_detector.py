import cv2

haar_file = "N:/PycharmProjects/AI-ML_Internship/assets/haarcascade_frontalface_default.xml"
img = cv2.imread('N:/PycharmProjects/AI-ML_Internship/assets/elon-musk.jpg')
# vid_cap = cv2.VideoCapture(0)

face_detector = cv2.CascadeClassifier(haar_file)

faces = face_detector.detectMultiScale(img, 1.5, 10)
print(faces)

for x, y, w, h in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 255), 2)

cv2.imshow("Image", img)
cv2.waitKey(0)

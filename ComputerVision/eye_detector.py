import cv2

faceDetector = cv2.CascadeClassifier('N:/PycharmProjects/AI-ML_Internship/assets/haarcascade_frontalface_default.xml')
img = cv2.imread('N:/PycharmProjects/AI-ML_Internship/assets/elon-musk.jpg')
faces = faceDetector.detectMultiScale(img, 1.5, 5)
eyeDetector = cv2.CascadeClassifier("N:/PycharmProjects/AI-ML_Internship/assets/haarcascade_eye.xml")

for x, y, w, h in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    roi_img = img[y:y+h, x:x+w]

    eyes = eyeDetector.detectMultiScale(roi_img, 1.5, 1)
    for p, q, r, s in eyes:
        cv2.rectangle(roi_img, (p, q), (p+r, q+s), (255, 255, 255), 2)
    cv2.imshow("ROI Image", roi_img)

cv2.imshow("Eye Detection", img)
cv2.waitKey(0)


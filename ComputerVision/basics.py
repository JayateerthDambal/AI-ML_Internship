# Importing Libraries
import cv2

img = cv2.imread('N:/PycharmProjects/InternshipAI-ML/assets/rohit-sharma.jpg')
# To get the arrays of the pixels of the img
# print(img)

# To show the image in a window
# cv2.imshow('Image', img)
# cv2.waitKey(5000)

# How to read a Video

# video_src = cv2.VideoCapture('N:/PycharmProjects/InternshipAI-ML/assets/Cars.mp4')
#
# while video_src:
#     _, img = video_src.read()
#     cv2.imshow("Image", img)
#     cv2.waitKey(10)


# How to get feed using a Camera
# video_src = cv2.VideoCapture(0)
# while video_src:
#     _, img = video_src.read()
#     cv2.imshow("Image", img)
#     key = cv2.waitKey(10)
#     if key == ord('q'):
#         print('Window Closed...')
#         break
#
# cv2.destroyAllWindows()
# video_src.release()


# Image Processing

# cv2.imshow('Imafge', img)
#
# gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# cv2.imshow('Gray Scale Image', gray_img)


# Cropping a Image
# cropped_img = img[260:330, 260:330]
#
# cv2.imshow('Cropped Image', cropped_img)

# Draw on Image

cv2.rectangle(img, (290, 80), (360, 200), (0,0,255), 3)
cv2.imshow('Image', img)
cv2.waitKey(0)



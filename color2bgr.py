import cv2
import numpy

input = cv2.imread('./images/sumreen/1.jpg')
cv2.imshow('original' , input)
cv2.waitKey()
gray_scale_img = cv2.cvtColor(input, cv2.COLOR_BGR2GRAY)
cv2.imshow('gray-scale-img', gray_scale_img)
cv2.imwrite("my-image.png", gray_scale_img)
cv2.waitKey()
cv2.destroyAllWindows()
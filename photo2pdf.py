from PIL import Image
import cv2
import numpy as np
import os

#im1 = Image.open(r'E:\\Important Docs\\Photo.jpg')
#im1.save(r'E:\\photo.pdf')

cap = cv2.VideoCapture(0)
counter = 1

while True:
	ret, frame = cap.read()
	

	gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	#retval2, threshold = cv2.threshold(gray,12,255,cv2.THRESH_BINARY)
	gaus = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,61,20)

	k = cv2.waitKey(1)
	if k%256==32:

		image_name = "Page{}.png".format(counter)
		cv2.imwrite(os.path.join('E:\\pydoc',image_name),gaus)
		print('{} saved'.format(image_name))
		counter+=1

	elif k%256==27:
		break

	cv2.imshow('frame',frame)
	cv2.imshow('gaus',gaus)
cv2.destroyAllWindows()
cap.release()


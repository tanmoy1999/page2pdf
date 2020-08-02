from PIL import Image
import cv2
import numpy as np
import os
from fpdf import FPDF
#im1 = Image.open(r'E:\\Important Docs\\Photo.jpg')
#im1.save(r'E:\\photo.pdf')

def convert_pdf():
	pdf = FPDF(orientation='L')
	directory = r'E:\Output'
	m=0
	files =[]
	for filename in os.listdir(directory):
		if filename.endswith(".jpg") or filename.endswith(".png"):
			files.append(os.path.join(directory, filename))
	pages = len(files)
	print('Pages: ',pages+1)
	for images in files:
		pdf.add_page()
		pdf.image(images,0,0,300,215)
	pdf_name = str(input('Enter File Name: '))
	pdf.output('E:\Output\ '+pdf_name+".pdf","F")
	print('Covertind to PDF....')
	print('Converted!!')

cap = cv2.VideoCapture(0)
counter = 1

print(' Press "Space bar": Click Picture \n Press "a": Covert to PDF \n Press "ESC": Exit')

while True:
	ret, frame = cap.read()
	gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	#retval2, threshold = cv2.threshold(gray,12,255,cv2.THRESH_BINARY)
	gaus = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,61,20)

	k = cv2.waitKey(1)
	if k%256==32:

		image_name = "Page{}.png".format(counter)
		cv2.imwrite(os.path.join('E:\\Output',image_name),gaus)
		print('{} saved'.format(image_name))
		counter+=1

	elif k%256==27:
		break
	
	elif k%256 == 97:
		print('PDF Converter')
		convert_pdf()

	cv2.imshow('frame',frame)
	cv2.imshow('gaus',gaus)
cv2.destroyAllWindows()
cap.release()


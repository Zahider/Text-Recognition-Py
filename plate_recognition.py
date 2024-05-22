# Importing libraries
import numpy as np #library for working with numerical data
import cv2 #opencv library
import easyocr #EasyOCR library

reader = easyocr.Reader(['en']) #read in english language

# reads our image, passes it through a model and stores the results in ocr_results
ocr_results = reader.readtext("./car.png")

print(ocr_results)

# creates a bounding box around the recognized text using indexing
top_left = ocr_results[0][0][0]
bottom_right = ocr_results[0][0][2]

# extracts the recognized text from the ocr_results corresponding to the bounding box
text = ocr_results[0][1]

# reads image, creates box around recognied text, prints text on top of box
img = cv2.imread("./car.png")
img = cv2.rectangle(img, top_left, bottom_right, (0,0,255), 5)
img = cv2.putText(img, text, top_left, cv2.FONT_HERSHEY_SIMPLEX, 2, (0,0,255), 2, cv2.LINE_AA)

# open image in a new window using imshow and keep the window open indefinitely using waitKey
cv2.imshow('im', img)
cv2.waitKey(0)
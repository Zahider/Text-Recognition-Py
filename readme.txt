This project demonstrates a simple OCR (Optical Character Recognition) application using EasyOCR and OpenCV in Python. 

Steps taken to complete project: 
1. Open command prompt and install EasyOCR by using the command 'pip install easyocr'
2. Now install OpenCV using the command 'pip install opencv-python'
3. Create a python file and import numpy, cv2 and easyocr libraries for data, file functions and reading/scanning objects.
4. Create a variable that will use EasyOCR to read within files in English.
5. Create a variable that will read our uploaded image, pass it through our model and then store it in that variable. Name the variable ocr_results. This should be enough for now to get the text location, model's guess of what the text is, and the accuracy in percentage. Next, add a line to print the answers.
6. Run the command and see the results. In the screenshot below, green is the text guess, and pink is the accuracy. Below that is the picture "car.png" that was used for the scan. As we can see, the model is fairly accurate with the exception of one letter error per text.
7. Next we will create a bounding box around our image so we can point out and print the detected text with our image in a new window. Start by declaring two variables that will use indexing to bound the top left and bottom right corners of the ocr_results  where the text was detected.
8. Extract the recognized text from ocr_results corresponding to the bounding box.
9. Create a variable named 'img' and read the previously used "car.png" image into it using cv2, then use rectangle function to draw a box with the top_left and bottom_right variables. Now print the recognized text inside 'img' and to make it more visually appealing, change the font, size and thickness of the box.
10. Create a new window using the cv2.imshow function that shows our new modified image with the detected results printed on top, and use the cv2.waitKey function to  keep the window open.
11. Run the code and see the results.

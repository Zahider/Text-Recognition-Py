License plate recognition application with EasyOCR in Pyhton and OpenCV

1. Open command prompt and install EasyOCR by using the command 'pip install easyocr'
2. Now install OpenCV using the command 'pip install opencv-python'
3. Create a python file and import numpy, cv2 and easyocr libraries for data, file functions and reading/scanning objects.
4. Create a variable that will use EasyOCR to read within files in English.
5. Create a variable that will read our uploaded image, pass it through our model and then store it in that variable. Name the variable ocr_results. This should be enough for now to get the text location, model's guess of what the text is, and the accuracy in percentage. Next, add a line to print the answers.
6. Run the command and see the results. In the screenshot below, green is the text guess, and pink is the accuracy. Below that is the picture "car.png" that was used for the scan. As we can see, the model is fairly accurate with the exception of one letter error per text.
7. 
8. 
9. 
10. 
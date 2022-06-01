This file contains the step-by step- explanation of the code.

Task: We are given with few images which contain checkbox along with some noise. Our task is to write a code which can identify the checkbox and remove the noise by croping the checkbox and display the boxes as it is after croping. For more understanding, a sample image (named: Raw_Image) and its expected output (named: Clean_Image) is given in the Files folder.

Approach:

1.  First, all the necessary libraries have been imported.(Lines 2-4)

2.  Now, a for loop has been used to read the files from the Raw_Dataset folder using glob function of glob library. (Line 13-14)

2a. An object is created to read the file and it is updated with a larger size image using resize() fucntion, as the original size is very small. (Line 15-16) 

2b. Using imshow() function, the given image is displayed in a window named 'Original'.(Line 17)

3.  Now, since some of the images are blurred, we have to separate them an first sharpen them before working on them further. 

3a. for this laplacian function is used and variance is calculated. It is then passed in a condition that if it comes less than 5, then the image is blurry and it has been passed to user defined function - sharpen() and its return value is assigned to a variable 'new_img'.Otherwise the 'new_ing' variable is assigned the same 'img' variable (Lines 20-24)

3b. In defining Sharpen(), it takes an image object as an argument. Now, image can be sharpened by the formula: (sharpened image = alpha * image +  beta * blurred image + gamma) in the addWeighted function. Here alpha + beta = 1. Gaussian blur has been used for blurring the image. (Lines 7-10)

4.  Now, to identify the checkbox and remove noise, following tasks have been done:

4a. Grayscale: to identify the intensity of colours on each pixel of the image

4b. Blur: low kernel blur has been applied so that edge detection becomes easy

4c. Thresholding: To binarize the image with a threshold of 200. (obtained by hit and trial)

4d. Now contours were found by using findContours function and list of contours was assigned to 'contours' variable. 

4e. for loop was applied to run through each contour and the coordinates of rectange was found using boundingRect function. 

4f. 2 variables (width and height) were defined which were used later to compare the width and height of bounding rectangewith them. 

4g. After that the rectange with coordinates (y,y+h) and (x,x+w) in the img was cropped and the reslut was displyed in new window named 'final'.

4h. waitKey(0) and destroyAllWindows() weer used to exit.
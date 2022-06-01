# importing essential libraries
import cv2 as cv
import numpy as np
import glob

# creating a function to sharpen the blurred images
def sharpen(image):
    gauss_blur = cv.GaussianBlur(image, (5, 5), 2)
    sharpened = cv.addWeighted(image, 15.5, gauss_blur, -14.5, 3)
    return sharpened

# creating loop for running all files in folder
path = glob.glob('C:/Users/MANAN/Desktop/DOCS/HW saver LLP/OpenCV/Files/Files/Raw_Dataset/*.jpg')
for file in path:
    img = cv.imread(file)
    img = cv.resize(img, (500,500))
    cv.imshow('Original', img)

    # blur detection
    laplacian_var = cv.Laplacian(img, cv.CV_64F).var()
    if laplacian_var < 5:
        new_img = sharpen(img)
    else:
        new_img = img

    # identifying and croping the checkboxes
    gray = cv.cvtColor(new_img, cv.COLOR_BGR2GRAY)
    blur = cv.blur(gray, (2,2))
    thresh = cv.threshold(blur, 200, 255, cv.THRESH_BINARY)[1]
    contours, hier = cv.findContours(thresh, 1,2)
    width = new_img.shape[1]*0.4
    height = new_img.shape[0]*0.3
    for cnt in contours:
        x,y,w,h = cv.boundingRect(cnt)
        if (w>width and h>height):
            break
    cropped = img[y:y+h, x:x+w]

    # displaying final cropped image
    cv.imshow('final', cropped)
    cv.waitKey(0)
    cv.destroyAllWindows()
import cv2
#the function below is for finding the boldest edges of the image by diving the graysacle image by the image_smoothing and giving the proper result.
def dodgeV2(x, y):
    return cv2.divide(x, 255 - y, scale=256)

img = cv2.imread('imagetest.jpg') #loading up the image
img_grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #convert the image to greyscale
img_invert = cv2.bitwise_not(img_grayscale) #this is needed because it will make the lighter parts darker and vice versa.
img_blur = cv2.GaussianBlur(img_invert, (21,21), sigmaX=0, sigmaY=0) #this is used to smoothen the image and apply the lines in our photo

final_image = dodgeV2(img_grayscale, img_blur) #here we are using the function to find the boldest edges of the image and apply the sketch lines.
final_image2 = cv2.resize(final_image, (900, 500))
cv2.imshow('img', final_image2)
cv2.waitKey()
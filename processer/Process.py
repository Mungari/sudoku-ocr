
import cv2
import numpy as np

image = ""
def findBiggest(cont):
    biggest = np.array([]) # Init empty array of biggest points
    max_area = 0
    for i in cont:
        area = cv2.contourArea(i) # Get area of cont
        if area > 50:
            # Is big enough to be considered
            peri = cv2.arcLength(i, True)
            approx = cv2.approxPolyDP(i, 0.02*peri, True) # Approximates perimeter
            if area > max_area and len(approx) == 4: # if the segment we're considering is bigger than the current and it's rectangular/square
                biggest = approx
                max_area = area
    return biggest, max_area

def reoder(cont):
    
def contours(image_neg):
    # find all contours
    contours, hierarchy = cv2.findContours(image_neg, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) # Find all external contours
    biggest, max_area = findBiggest(contours)
    if biggest.size != 0:
        biggest = reorder(biggest)

def clean(image_path: str):
    # Set image path 
    try:
        image = cv2.imread(image_path)
    except FileNotFoundError:
        print(f"File {image_path} not found, double check")
        exit(1)
    # Grayscale
    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    img_blur = cv2.GaussianBlur(img_gray, (5,5), 1) # Radius?
    image = cv2.adaptiveThreshold(img_blur, 255, 1, 1, 11, 2) # Negative of starting immy with noise reduced, numbers are white and bg is black
    return image
import cv2
import imutils
import numpy as np


def processImage(image):
    resized = imutils.resize(image, width=400, height=400) # resizing image
    gray = cv2.cvtColor(resized, cv2.COLOR_RGB2GRAY) #applying grayscale
    adaptiveThresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 125, 1) #thresholding
    return adaptiveThresh


def initialize_mask(adaptiveThresh, img):
    '''
    Finds border of chessboard and blacks out all unneeded pixels
    '''

    # Find contours (closed polygons)
    contours, hierarchy = cv2.findContours(adaptiveThresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Create copy of original image
    imgContours = img.copy()

    for c in range(len(contours)):
        # Area
        area = cv2.contourArea(contours[c])
        # Perimenter
        perimeter = cv2.arcLength(contours[c], True)
        # Filtering the chessboard edge / Error handling as some contours are so small so as to give zero division
        # For test values are 70-40, for Board values are 80 - 75 - will need to recalibrate if change
        # the largest square is always the largest ratio
        if c == 0:
            Lratio = 0
        if perimeter > 0:
            ratio = area / perimeter
            if ratio > Lratio:
                largest = contours[c]
                Lratio = ratio
                Lperimeter = perimeter
                Larea = area
        else:
            pass

    # Draw contours
    cv2.drawContours(imgContours, [largest], -1, (0, 0, 0), 1)

    # Epsilon parameter needed to fit contour to polygon
    epsilon = 0.1 * Lperimeter
    # Approximates a polygon from chessboard edge
    chessboardEdge = cv2.approxPolyDP(largest, epsilon, True)

    # Create new all black image
    mask = np.zeros((img.shape[0], img.shape[1]), 'uint8') * 125
    # Copy the chessboard edges as a filled white polygon size of chessboard edge
    cv2.fillConvexPoly(mask, chessboardEdge, 255, 1)
    # Assign all pixels that are white (i.e the polygon, i.e. the chessboard)
    extracted = np.zeros_like(img)
    extracted[mask == 255] = img[mask == 255]
    # remove strip around edge
    extracted[np.where((extracted == [125, 125, 125]).all(axis=2))] = [0, 0, 20]
    return extracted





    #following tutorial https://www.youtube.com/watch?v=JOxebvuRpyo
    # #create canvas
    # canvas = np.zeros(img.shape, np.uint8)
    # canvas.fill(255)
    #
    # #create background mask
    # mask = np.zeros(img.shape, np.uint8)
    # mask.fill(255)
    #
    # #get contours
    # contours_draw, hierarchy  = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

   # return canvas


import math
import cv2
import numpy as np
import Line
import Square
import my_functions


def processImage(image):
    frame_BGR_resized = my_functions.resize_image(image, 10) #resizing image
    gray = cv2.cvtColor(frame_BGR_resized, cv2.COLOR_RGB2GRAY) #applying grayscale
    blurred = cv2.GaussianBlur(gray, (5, 5), 0) # applying blur
    adaptiveThresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 125, 1) #thresholding

    contours, hierarchy = cv2.findContours(adaptiveThresh, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_NONE)
    largest_contour_index = my_functions.get_contour_max_area(contours)[0]

    largest_contoured_polygon = cv2.approxPolyDP(contours[largest_contour_index],
                                0.05 * cv2.arcLength(contours[largest_contour_index], True), True)

    frame_BGR_cropped = my_functions.crop_image(frame_BGR_resized, largest_contoured_polygon)
    return frame_BGR_cropped

def findEdges(image):

    # Find edges
    edges = cv2.Canny(image, 100, 200, None, 3)
    # Convert edges image to grayscale
    colorEdges = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)

    return colorEdges, edges

def findLines(edges, colorEdges):
    # Infer lines based on edges
    lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 100, np.array([]), 100, 80)

    # Draw lines
    a, b, c = lines.shape
    for i in range(a):
        cv2.line(colorEdges, (lines[i][0][0], lines[i][0][1]), (lines[i][0][2], lines[i][0][3]), (0, 255, 0), 2,
                 cv2.LINE_AA)

    # Create line objects and sort them by orientation (horizontal or vertical)
    horizontal = []
    vertical = []
    for l in range(a):
        [[x1, y1, x2, y2]] = lines[l]
        newLine = Line.Line(x1, x2, y1, y2)
        if newLine.orientation == 'horizontal':
            horizontal.append(newLine)
        else:
            vertical.append(newLine)

    return horizontal, vertical

def findCorners(horizontal, vertical, colorEdges):
    '''
    Finds corners at intersection of horizontal and vertical lines.
    '''

    # Find corners (intersections of lines)
    corners = []
    for v in vertical:
        for h in horizontal:
            s1, s2 = v.find_intersection(h)
            corners.append([s1, s2])

    # remove duplicate corners
    dedupeCorners = []
    for c in corners:
        matchingFlag = False
        for d in dedupeCorners:
            if math.sqrt((d[0] - c[0]) * (d[0] - c[0]) + (d[1] - c[1]) * (d[1] - c[1])) < 20:
                matchingFlag = True
                break
        if not matchingFlag:
            dedupeCorners.append(c)

    for d in dedupeCorners:
        cv2.circle(colorEdges, (d[0], d[1]), 10, (0, 0, 255))

    return dedupeCorners

def findSquares(corners, colorEdges):
    '''
    Finds the squares of the chessboard
    '''

    # sort corners by row
    corners.sort(key=lambda x: x[0])
    rows = [[], [], [], [], [], [], [], [], []]
    r = 0
    for c in range(0, 81):
        if c > 0 and c % 9 == 0:
            r = r + 1

        rows[r].append(corners[c])

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8']
    Squares = []

    # sort corners by column
    for r in rows:
        r.sort(key=lambda y: y[1])

    # initialize squares
    for r in range(0, 8):
        for c in range(0, 8):
            c1 = rows[r][c]
            c2 = rows[r][c + 1]
            c3 = rows[r + 1][c]
            c4 = rows[r + 1][c + 1]

            position = letters[r] + numbers[7 - c]
            newSquare = Square.Square(colorEdges, c1, c2, c3, c4, position)
            newSquare.draw(colorEdges, (0, 0, 255), 2)
            newSquare.drawROI(colorEdges, (255, 0, 0), 2)
            newSquare.classify(colorEdges)
            Squares.append(newSquare)

    return Squares, colorEdges


import cv2
import my_functions


def processImage(image):
    frame_BGR_resized = my_functions.resize_image(image, 10) #resizing image
    gray = cv2.cvtColor(frame_BGR_resized, cv2.COLOR_RGB2GRAY) #applying grayscale
    blurred = cv2.GaussianBlur(gray, (5, 5), 0) # applying blur
    adaptiveThresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 125, 1) #thresholding

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

    return  colorEdges















    # #following tutorial https://www.youtube.com/watch?v=JOxebvuRpyo
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
    #
    # return canvas


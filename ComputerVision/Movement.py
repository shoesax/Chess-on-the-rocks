import cv2
import numpy as np
import math

debug = False


class Board:
    """
    Holds all the Square instances and updates changes to board after moves
    """

    def __init__(self, squares):

        self.squares = squares
        # self.boardMatrix = []
        # self.promotion = 'q'
        # self.promo = False
        self.move = "e2e4"

    def draw(self, image):
        """
        Draws the board and classifies the squares (draws the square state on the image).
        """
        for square in self.squares:
            square.draw(image, (0, 0, 255))
            square.classify(image)

    def determineChanges(self, previous, current):
        '''
        Determines the change in color values within squares from picture to picture
        to infer piece movement
        '''

        copy = current.copy()

        largestSquare = 0
        secondLargestSquare = 0
        largestDist = 0
        secondLargestDist = 0
        stateChange = []

        # check for differences in color between the photos
        for sq in self.squares:
            colorPrevious = sq.roiColor(previous)
            colorCurrent = sq.roiColor(current)

            # distance in bgr values
            sum = 0
            for i in range(0, 3):
                sum += (colorCurrent[i] - colorPrevious[i]) ** 2

            distance = math.sqrt(sum)

            if distance > 25:
                stateChange.append(sq)

            if distance > largestDist:
                # update squares with largest change in color
                secondLargestSquare = largestSquare
                secondLargestDist = largestDist
                largestDist = distance
                largestSquare = sq

            elif distance > secondLargestDist:
                # update second change in color
                secondLargestDist = distance
                secondLargestSquare = sq


        # regular move two squares change state
        squareOne = largestSquare
        squareTwo = secondLargestSquare


        # get colors for each square from each photo
        oneCurr = squareOne.roiColor(current)
        twoCurr = squareTwo.roiColor(current)

        # calculate distance from empty square color value
        sumCurr1 = 0
        sumCurr2 = 0
        for i in range(0, 3):
            sumCurr1 += (oneCurr[i] - squareOne.emptyColor[i]) ** 2
            sumCurr2 += (twoCurr[i] - squareTwo.emptyColor[i]) ** 2

        distCurr1 = math.sqrt(sumCurr1)
        distCurr2 = math.sqrt(sumCurr2)

        if distCurr1 < distCurr2:
            # square 1 is closer to empty color value thus empty
            squareTwo.state = squareOne.state
            squareOne.state = '.'
            # check for promotion of a pawn
            if squareTwo.state.lower() == 'p':
                if squareOne.position[1:2] == '2' and squareTwo.position[1:2] == '1':
                    self.promo = True
                if squareOne.position[1:2] == '7' and squareTwo.position[1:2] == '8':
                    self.promo = True

            self.move = squareOne.position + squareTwo.position

        else:
            # square 2 is currently empty
            squareOne.state = squareTwo.state
            squareTwo.state = '.'

            self.move = squareTwo.position + squareOne.position

        return self.move
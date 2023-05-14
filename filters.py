import numpy as np
import cv2

def remove_small_blobs(fg_mask, min_area):
    # Perform morphological closing to fill in holes in blobs
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    closed_mask = cv2.morphologyEx(fg_mask, cv2.MORPH_CLOSE, kernel)

    # Find contours in the binary image
    contours, _ = cv2.findContours(closed_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Create a copy of the foreground mask to draw on
    fg_mask_copy = fg_mask.copy()

    # Loop over the contours and remove small blobs
    for contour in contours:
        area = cv2.contourArea(contour)
        if area < min_area:
            cv2.drawContours(fg_mask_copy, [contour], 0, 0, -1)

    return fg_mask_copy

def drawRectangle(fg_mask,pt1,side):
    cv2.rectangle(fg_mask,pt1,((pt1 + side),(pt1+side)),0,255,1)
    return fg_mask

    # Find contours in the foreground mask
    contours, _ = cv2.findContours(fg_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Create a black image with the same size as the input foreground mask
    filled_fg_mask = np.zeros_like(fg_mask)

    # Fill in each contour with white
    for contour in contours:
        area = cv2.contourArea(contour)
        if area >= above_area:
            cv2.drawContours(filled_fg_mask, [contour], 0, 255, -1)
        else:
            cv2.drawContours(filled_fg_mask, [contour], 0, 0, -1) #black

    return filled_fg_mask
    # Convert the image to grayscale
    # gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Threshold the image
    thresh = cv2.threshold(mask, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

    # Find contours in the thresholded image
    contours, _ = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    # Initialize list of blobs
    blobs = []

    # Loop over the contours
    for contour in contours:
        # Compute the area of the contour
        area = cv2.contourArea(contour)

        # Ignore small contours
        if area < 100:
            continue

        # Compute the center of mass of the contour
        M = cv2.moments(contour)
        if M["m00"] != 0:
            cx = int(M["m10"] / M["m00"])
            cy = int(M["m01"] / M["m00"])
        else:
            cx, cy = 0, 0

        # Add the blob to the list
        blobs.append((cx, cy, area))

    return blobs


def apply_filters(fg_mask):

    # create a kernel for erosion
    # erode the mask
    shape = (3,1)
    kernel = np.ones(shape, np.uint8)   
    fg_mask = cv2.erode(fg_mask, kernel, iterations=2)
    shape = (1,3)
    kernel = np.ones(shape, np.uint8)   
    fg_mask = cv2.erode(fg_mask, kernel, iterations=1)

    shape = (2,2)
    kernel = np.ones(shape, np.uint8)   
    fg_mask = cv2.erode(fg_mask, kernel, iterations=2)

    #dilate mask
    shape = (7,2)
    kernel = np.ones(shape, np.uint8)   
    fg_mask = cv2.dilate(fg_mask, kernel, iterations=5)

    fg_mask = remove_small_blobs(fg_mask,2000)

    # dilate
    shape = (2,2)
    kernel = np.ones(shape,np.uint8)
    fg_mask = cv2.dilate(fg_mask, kernel, iterations=3)

    return fg_mask

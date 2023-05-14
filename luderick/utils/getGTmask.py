import numpy as np
import cv2
import ast
from csv_utils import findCsvRowsByFilename
def generate_fg_mask(pointsArray, shape):
    """
    Generate a foreground mask from an array of points.

    Parameters:
    - points: An array of points in the format [x, y, x1, y1, ...].
    - shape: A tuple specifying the shape of the output mask (e.g., (height, width)).

    Returns:
    - A binary mask with the same shape as the input shape, where the polygon defined
      by the input points is filled in with white (255) and everything else is black (0).
    """
    # Create a blank image to draw the polygon on
    mask = np.zeros(shape, dtype=np.uint8)
    
    for points in pointsArray:
        # Reshape the points array into a 2D array of shape (num_points/2, 2) 
        pts = np.array(points, np.int32).reshape((-1, 2))

        # Fill the polygon defined by the points with white (255)
        cv2.fillPoly(mask, [pts], (255,255,255))

    return mask
def compare_images(image1, image2):

    cv2.namedWindow('Comparison', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('Comparison', 800, 600)

    show_image = 1  # 1 to show first image, 2 to show second image
    #cv2.getWindowProperty('Comparison',0) >= 0 
    while True:
        if show_image == 1:
            img = image1.copy()
            cv2.putText(img, 'Original Image', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
        else:
            img = image2.copy()
            cv2.putText(img, 'Foreground Mask', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)

        cv2.imshow('Comparison', img)
        key = cv2.waitKey(0)

        if key == ord('q'):
            break
        elif key == ord(' '):
            if show_image == 1:
                show_image = 2
            else:
                show_image = 1
    
    cv2.destroyAllWindows()
    """
    Save a foreground mask as an image file.
    
    Args:
    - fg_mask: NumPy array representing the foreground mask
    - filename: string specifying the output filename, e.g. 'fg_mask.jpg'
    """
    # Convert the NumPy array to an 8-bit unsigned integer format
    fg_mask = fg_mask.astype('uint8') * 255
    
    # Save the foreground mask as an image file using OpenCV's imwrite function
    cv2.imwrite(filename+"_mask", fg_mask)
    
    print(f"Foreground mask saved as {filename}_mask")
def getPolygonPointsFromCSV(filename,csv_file):
    points = []
    rows = findCsvRowsByFilename(filename,csv_file)
    for row in rows:
        array = ast.literal_eval(row['segmentation'])
        points.append(array[0]) #is 2d array in csv
    return points
    """
    Draws a white rectangle on the input foreground mask.

    Parameters:
        - fg_mask: numpy array representing the foreground mask (binary image)
        - area: tuple containing the top-left and bottom-right coordinates of the rectangle
                (e.g. (x1, y1, x2, y2))

    Returns:
        - fg_mask: updated foreground mask with rectangle drawn on it
    """
    # Create a blank mask with the same dimensions as the foreground mask
    rect_mask = np.zeros_like(fg_mask)

    # Draw a white rectangle on the blank mask using the input coordinates
    cv2.rectangle(rect_mask, (area[0], area[1]), (area[2], area[3]), (255, 255, 255), -1)

    # Combine the rectangle mask with the foreground mask using bitwise OR
    fg_mask = cv2.bitwise_or(fg_mask, rect_mask)

    return fg_mask

    # Perform connected components labeling on the foreground mask
    num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(fg_mask)

    # Iterate over the labels and stats to filter blobs above the specified area
    for label in range(1, num_labels):
        if stats[label, cv2.CC_STAT_AREA] > min_area:
            # Fill the blob by setting all pixels with the same label to white
            fg_mask[labels == label] = 255
    
    return fg_mask
# def get_fg_mask(filename,csv_file):
#     #Gets the fg mask using the above functions 
#     img = cv2.imread('./data/'+ filename)
#     points = getPolygonPointsFromCSV(filename,csv_file)
#     mask = generate_fg_mask(points,img.shape)
#     return mask







    





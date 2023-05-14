import os
import cv2
from getGTmask import getPolygonPointsFromCSV, generate_fg_mask

def save_video(filenames, directory, output_path):
    """
    Saves a video from a list of image files in a directory.

    Parameters:
        - filenames: list of image filenames (strings)
        - directory: path to the directory containing the images
        - output_path: path to the output video file (string)

    Returns:
        - None
    """
    print(output_path)
    # Get the shape of the first image in the list
    first_image = cv2.imread(os.path.join(directory, filenames.iloc[0]))
    height, width, channels = first_image.shape

    # Create the video writer object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    video_writer = cv2.VideoWriter(output_path, fourcc, 5.0, (width, height))
    # Iterate over the image filenames and add each frame to the video writer
    for filename in filenames:
        # Load the image and add it to the video writer
        image = cv2.imread(os.path.join(directory, filename))
        video_writer.write(image)

    # Release the video writer and close the video file
    video_writer.release()
def save_fg_video(filenames, directory, output_path,csv_file):
    """
    Saves a video from a list of image files in a directory.

    Parameters:
        - filenames: list of image filenames (strings)
        - directory: path to the directory containing the images
        - output_path: path to the output video file (string)

    Returns:
        - None
    """
    # Get the shape of the first image in the list
    first_image = cv2.imread(os.path.join(directory, filenames.iloc[0]))
    height, width, channels = first_image.shape

    # Create the video writer object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    video_writer = cv2.VideoWriter(output_path, fourcc, 5.0, (width, height))

    # Iterate over the image filenames and add each frame to the video writer
    for filename in filenames:
        # Load the image and add it to the video writer
        image = cv2.imread(os.path.join(directory, filename))
        points = getPolygonPointsFromCSV(filename,csv_file)
        fg_mask = generate_fg_mask(points,image.shape)
        video_writer.write(fg_mask)

    # Release the video writer and close the video file
    video_writer.release()
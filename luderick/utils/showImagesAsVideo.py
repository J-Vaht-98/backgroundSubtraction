import os
import cv2

def showImagesAsVideo(folder_path):
    # Get list of image files in folder
    image_files = [f for f in os.listdir(folder_path) if f.endswith('.jpg')]

    # Sort image files by filename
    image_files.sort()

    # Open first image to get dimensions
    first_image_path = os.path.join(folder_path, image_files[0])
    first_image = cv2.imread(first_image_path)
    height, width, channels = first_image.shape

    # Create video writer object
    video_path = os.path.join(folder_path, 'video.mp4')
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    video_writer = cv2.VideoWriter(video_path, fourcc, 25.0, (width, height))

    # Loop through image files and write to video
    for image_file in image_files:
        image_path = os.path.join(folder_path, image_file)
        image = cv2.imread(image_path)

        # Write image to video
        video_writer.write(image)

        # Show image on screen
        cv2.imshow('Image', image)
        cv2.waitKey(40)  # 25fps = 40ms delay per frame

    # Release video writer object and close window
    video_writer.release()
    cv2.destroyAllWindows()

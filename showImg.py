import cv2

def display_frames_side_by_side(video1_path, video2_path, frame_number, output_path):
    # Open the first video capture object
    cap1 = cv2.VideoCapture(video1_path)

    # Set the frame position for the first video capture object
    cap1.set(cv2.CAP_PROP_POS_FRAMES, frame_number)

    # Read the frame from the first video capture object
    ret1, frame1 = cap1.read()

    # Open the second video capture object
    cap2 = cv2.VideoCapture(video2_path)

    # Set the frame position for the second video capture object
    cap2.set(cv2.CAP_PROP_POS_FRAMES, frame_number)

    # Read the frame from the second video capture object
    ret2, frame2 = cap2.read()

    # Check if the frames were read successfully
    if not ret1:
        print(f"Error reading frame {frame_number} from {video1_path}")
        return

    if not ret2:
        print(f"Error reading frame {frame_number} from {video2_path}")
        return

    # Resize the frames to have the same height
    height = max(frame1.shape[0], frame2.shape[0])
    width1 = int(frame1.shape[1] * height / frame1.shape[0])
    width2 = int(frame2.shape[1] * height / frame2.shape[0])
    frame1 = cv2.resize(frame1, (width1, height))
    frame2 = cv2.resize(frame2, (width2, height))

    # Concatenate the frames horizontally
    concatenated_frame = cv2.hconcat([frame1, frame2])
    # Save the concatenated frame
    cv2.imwrite(output_path, concatenated_frame)

    # Display the concatenated frame
    # cv2.imshow("Frames", concatenated_frame)
    # cv2.waitKey(0)


    # Release the video capture objects
    cap1.release()
    cap2.release()

    # Destroy all windows
    # cv2.destroyAllWindows()

def concatenate_images_vertically(image1_path, image2_path, output_path):
    # Read the two input images
    image1 = cv2.imread(image1_path)
    image2 = cv2.imread(image2_path)

    # Check if the images were read successfully
    if image1 is None:
        print(f"Error reading {image1_path}")
        return

    if image2 is None:
        print(f"Error reading {image2_path}")
        return

    # Resize the images to have the same width
    width = max(image1.shape[1], image2.shape[1])
    height1 = int(image1.shape[0] * width / image1.shape[1])
    height2 = int(image2.shape[0] * width / image2.shape[1])
    image1 = cv2.resize(image1, (width, height1))
    image2 = cv2.resize(image2, (width, height2))

    # Concatenate the images vertically
    concatenated_image = cv2.vconcat([image1, image2])

    # Display the concatenated image
    # cv2.imshow("Images", concatenated_image)
    # cv2.waitKey(0)

    # Save the concatenated image
    cv2.imwrite(output_path, concatenated_image)

    # Destroy all windows
    # cv2.destroyAllWindows()

display_frames_side_by_side("./luderick/videos/04C1_Luderick_1.mov","./luderick/masks/04C1_Luderick_1.mov",8,"./a.jpg")
display_frames_side_by_side("./luderick/videos/04C1_Luderick_1.mov","./luderick/masks/04C1_Luderick_1.mov",10,"./b.jpg")
display_frames_side_by_side("./luderick/videos/04C1_Luderick_1.mov","./luderick/masks/04C1_Luderick_1.mov",12,"./c.jpg")
display_frames_side_by_side("./luderick/videos/04C1_Luderick_1.mov","./luderick/masks/04C1_Luderick_1.mov",14,"./d.jpg")
display_frames_side_by_side("./luderick/videos/04C1_Luderick_1.mov","./luderick/masks/04C1_Luderick_1.mov",16,"./e.jpg")

concatenate_images_vertically("./a.jpg","./b.jpg","a.jpg")
concatenate_images_vertically("./a.jpg","./c.jpg","a.jpg")
concatenate_images_vertically("./a.jpg","./d.jpg","a.jpg")
concatenate_images_vertically("./a.jpg","./e.jpg","a.jpg")
# display_frames_side_by_side("./deepfish/videos/7117_Chaetodon_vagabundus_3_f000030.mp4","./deepfish/masks/7117_Chaetodon_vagabundus_3_f000030.mp4",2,"./b.jpg")
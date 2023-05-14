import cv2
import os
import pandas as pd

def save_video(input_path, output_path,output_file):
    # Get a list of all the image filenames in the input folder
    image_filenames = os.listdir(input_path)

    # Read the first image to get the frame dimensions
    first_image = cv2.imread(f'{input_path}/{image_filenames[0]}')
    height, width, channels = first_image.shape

    # Define the video codec and create a VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    output_file = os.path.join(output_path, output_file)
    out = cv2.VideoWriter(output_file, fourcc, 5.0, (width, height))

    # Loop through the images and write them to the video
    for image_filename in image_filenames:
        image = cv2.imread(f'{input_path}/{image_filename}')
        out.write(image)

    # Release the VideoWriter object and print a message
    out.release()
    print(f"Video saved to {output_file}")
video_path = "./frames"

video_frames_and_masks = os.listdir(video_path)


for nr in video_frames_and_masks:
    #Get video frames and masks
    video_frames = os.listdir(f'{video_path}/{nr}/video')
    mask_frames = os.listdir(f'{video_path}/{nr}/mask')

    #confirm that every video frame has mask frame
    if len(video_frames) != len(mask_frames):
        print("Frames and masks dont have same length")
        continue
    #confirm that isnt empty folder
    if len(video_frames) <= 0:
        continue
    
    video_name = video_frames[0].replace(".jpg",".mp4")
    
    for i in range(len(video_frames)):
       
        video_frame = video_frames[i]
        mask_frame = mask_frames[i]
        #confirm that the names are the same (remove extension)
        if video_frame.split(".")[0] != mask_frame.split(".")[0]:
            print("Frame mismatch in video",i,"frame", video_frame,"!=", mask_frame)
            break
    save_video(f'./frames/{nr}/video', "./v/",video_name)
    save_video(f'./frames/{nr}/mask', "./m/",video_name)





    
        

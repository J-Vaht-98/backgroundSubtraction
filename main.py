import os
import numpy as np
import cv2
from metrics import calculate_iou
from datetime import datetime
import time
from filters import *
import pandas as pd

#Open video and mask streams
#Trailing '/' is important

def perform_bg_subtraction(subtractor_name,video_path, mask_path, dataset_name,vizualize=False):
    print(f'Using model {subtractor_name}')
  
    # Get current date and time
    now = datetime.now()
    timestamp = now.strftime("%Y%m%d_%H%M%S")


    # Open/create the log file in append mode
    log_file = open(f"./logs/log_{timestamp}_{subtractor_name}_{dataset_name}.txt", "w")
    csv_file = open(f"./logs/df_{timestamp}_{subtractor_name}_{dataset_name}.csv", "w")

    #Video names and mask names are the same
    video_names = os.listdir(video_path)
    global_avg_iou = 0
    analyzed_files = 0

    #initialize pandas dataframe for dataset
    df = pd.DataFrame(columns=["model","video_name", "video_length", "iou","dataset","processing_time","frames_analyzed_rate"])

    start_time = time.time()
    for filename in video_names:
        video_capture = cv2.VideoCapture(video_path+filename)
        mask_capture = cv2.VideoCapture(mask_path+filename)


        if(not video_capture.isOpened() or not mask_capture.isOpened()):
            print(f'Couldnt open video {filename}')
            log_file.write("FAIL \n")
            continue #skip iteration
        
        avg_iou = 0
        frames = 0
    

        if vizualize:
            #Initialize video player
            window_name = "Video Player"
            cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
            cv2.resizeWindow(window_name, 960, 540)
        
        #read in frames multiple times
        nrOfFramesInVideo = 0
        processing_time_start = time.time()
        while True:

            ret, frame = video_capture.read()
            if not ret:
                break
            nrOfFramesInVideo += 1
        
        #reset video capture
        video_capture = cv2.VideoCapture(video_path+filename)

        video_frames = []
        
        #Initialize model 
        subtractors = {
            "GMM":cv2.createBackgroundSubtractorMOG2(detectShadows=False),
            "KNN":cv2.createBackgroundSubtractorKNN(detectShadows=False),
            "CNT":cv2.bgsegm.createBackgroundSubtractorCNT(),
            "GMG":cv2.bgsegm.createBackgroundSubtractorGMG(),
            "GSOC":cv2.bgsegm.createBackgroundSubtractorGSOC(),
            "LSBP":cv2.bgsegm.createBackgroundSubtractorLSBP()
            }
        subtractor = subtractors[subtractor_name]

       
        
        ##Example on how to set specific params
        # if subtractor_name == "GMM":
        #     subtractor.setComplexityReductionThreshold(0.9)
        #     subtractor.setNMixtures(10)
        #     subtractor.setBackgroundRatio(0.7)
        #     subtractor.setVarThresholdGen(51.0)

        while True:

            ret, frame = video_capture.read()
            if not ret:
                break
            video_frames.append(frame)
            ret, gt_frame = mask_capture.read()
            if not ret:
                break

            #apply background subtraction model

            #create a background model
            fg_mask = subtractor.apply(frame) #default learningRate=-1

            #apply model to first(or more) frames i  times
            # i = 0
            # while (len(video_frames) == 2 and i <= 10):
            #     for frame in video_frames:
            #         subtractor.apply(frame)
            #     i+= 1
            
            # fg_mask = apply_filters(fg_mask)
            
            #Convert ground truth to grayscale
            gt_mask = cv2.cvtColor(gt_frame,cv2.COLOR_BGR2GRAY)
            iou = calculate_iou(gt_mask,fg_mask)
            avg_iou += iou
            frames += 1
            #print(f'IoU = {iou} for frame {frames}')

            if(vizualize) :
                # resize the video frame and mask frame
                calculated_mask_frame = cv2.resize(fg_mask, (480, 270))
                mask_frame = cv2.resize(gt_frame, (480, 270))
                
                # add the filename to the frame
                cv2.putText(
                    calculated_mask_frame,
                    f'{filename} frame: {frames}',
                    (5, 10), cv2.FONT_HERSHEY_SIMPLEX,0.4, color=(255,255,255), thickness=1)

                # display the frames side by side
                mask_frame = cv2.cvtColor(mask_frame,cv2.COLOR_BGR2GRAY)
                # combined_frame = cv2.hconcat([video_frame, mask_frame])
                combined_frame = cv2.vconcat([calculated_mask_frame, mask_frame])
                cv2.imshow(window_name, combined_frame)

                cv2.waitKey(1) #200 ms = 5fps

        processing_time = time.time() - processing_time_start
        frames_analyzed_rate = processing_time/frames
        
        print(f'{analyzed_files}  Average IoU for {filename} = {avg_iou/frames} in {processing_time:.2f} seconds')  
        log_file.write(f'Average IoU for {filename} = {avg_iou/frames} in {processing_time:.2f} seconds \n')
        global_avg_iou += (avg_iou/frames)
        df.loc[analyzed_files] = (subtractor_name,filename, nrOfFramesInVideo, avg_iou/frames,dataset_name,processing_time, frames_analyzed_rate)
        analyzed_files += 1


    end_time = time.time()
    csv_file.write(df.to_csv())
    print(f' Using model {subtractor_name} Average IoU for {dataset_name} = {(global_avg_iou/analyzed_files)} with time {end_time - start_time}\n')
    log_file.write(f'Using model {subtractor_name} Average IoU for dataset {dataset_name} = {(global_avg_iou/analyzed_files)} with time {end_time - start_time}\n')
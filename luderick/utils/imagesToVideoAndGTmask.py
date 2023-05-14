import pandas as pd
import os
from saveImagesAsMp4 import *
csv_file = "../annotations/luderick_seagrass_jack_evans_a.csv"
data_dir = "../data/"

#Load csv into pandas dataframe
df = pd.read_csv(csv_file)

#Path to the .mov files in the luderic dataset
video_dir = '../../../datasets/Luderick Seagrass Jack Evans A/Wvo7U_76t/'
video_names = os.listdir(video_dir)
nrOfVideosSaved = 0

output_video_path = "../videos2"
output_mask_path = "../masks2"
for videoname in video_names:
    if videoname in os.listdir(output_video_path):
        print(f'Video {videoname} already exists')
        continue
    #Set of results that contain this filename
    results = df[df['image'].str.contains(videoname)]
    #Skip non annotated videos
    if len(results) <= 0:
        continue
    
    #Save set of images at 5fps 

    save_video(results['image'],data_dir,f'{output_video_path}/{videoname}')
    save_fg_video(results['image'],data_dir,f'{output_mask_path}/{videoname}',csv_file=csv_file)

    nrOfVideosSaved += 1
    print(f'saved mask and video for {videoname}')   
 
    
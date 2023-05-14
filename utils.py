import os
import csv
def findCsvAnnotation(video_name,csv_path):
    
    video_name = video_name.split('.')[0]
    
    csv_path = './luderick_seagrass_jack_evans_a.csv'

    # Open the CSV file
    with open(csv_path, 'r') as f:
        reader = csv.DictReader(f)

        # Loop through the rows and filter based on the 'image' field
        filtered_rows = []
        for row in reader:
            if video_name in row['image']:
                filtered_rows.append(row)
    return filtered_rows
def findBoundingBox(video_name,csv_path):
    
    video_name = video_name.split('.')[0]
    
    csv_path = './luderick_seagrass_jack_evans_a.csv'

    # Open the CSV file
    with open(csv_path, 'r') as f:
        reader = csv.DictReader(f)

        # Loop through the rows and filter based on the 'image' field
        filtered_bbs = {}
        for row in reader:
            if video_name in row['image']:
                filtered_bbs[row['image_id']] = {"x":row['bbox_x'],"y":row['bbox_y'],"w":row['bbox_w'],"h":row["bbox_h"]}
    return filtered_bbs
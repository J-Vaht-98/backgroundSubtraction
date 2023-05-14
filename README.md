# Usage
Main functionality is used by running `python multipleModels.py`

The main.py file contains a function `perform_bg_subraction`
This function takes the following arguments:

   * `subtractor_name` : name of the subtractor to use (i.e "GMM", "KNN")\n
   * `video_path`      : path to videos of a dataset
   * `mask_path`        : path to ground truth masks for a dataset 
  *  `vizualize`        : boolean that tells the function wheter to visualize the model output and mask
   * `dataset_name`    : name of the dataset for logging purposes

NB! The mask and video must be in sync i.e frame 23 of the video must correspond to frame 23 of the ground truth mask for the code to work properly. 

The function maps the subtractor_name to the map below and uses the model defined for the key
`subtractors = {
            "GMM":cv2.createBackgroundSubtractorMOG2(detectShadows=False),
            "KNN":cv2.createBackgroundSubtractorKNN(detectShadows=False),
            "CNT":cv2.bgsegm.createBackgroundSubtractorCNT(),
            "GMG":cv2.bgsegm.createBackgroundSubtractorGMG(),
            "GSOC":cv2.bgsegm.createBackgroundSubtractorGSOC(),
            "LSBP":cv2.bgsegm.createBackgroundSubtractorLSBP()
        }`

"filters.py" - the "apply_filters" function is used to use erosion, dilation etc on a generated mask
"metrics.py" - contains function to calculate IoU


In this project 2 datasets were analyzed, DeepFish(https://alzayats.github.io/DeepFish/) and Luderick (https://github.com/globalwetlands/luderick-seagrass)

Directories by the same name (luderick, deepfish)in the repository contain utility functions to convert the images and segmentation data from these datasets into the required format and to check the results of converting them. 


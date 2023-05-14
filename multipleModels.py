from main import perform_bg_subtraction


subtractor_names = [
            "GMM",
            "KNN",
            "CNT",
            "GMG",
            "GSOC",
            "LSBP",
            ]

deepfish_video_path = "./deepfish/videos/"
deepfish_mask_path = "./deepfish/masks/"
luderick_video_path = "./luderick/videos/"
luderick_mask_path = "./luderick/masks/"


#Deepfish 

for model_name in subtractor_names:
    perform_bg_subtraction(model_name,
                           video_path=deepfish_video_path,
                            mask_path=deepfish_mask_path,
                            dataset_name="Deepfish"
                            )

#Luderick

for model_name in subtractor_names:
    perform_bg_subtraction(model_name,
                           video_path=luderick_video_path,
                            mask_path=luderick_mask_path,
                            dataset_name="Luderick"
                            )
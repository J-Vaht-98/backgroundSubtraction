import cv2
import os

def play_videos_in_sync(video_dir, mask_dir):
    filenames = os.listdir(video_dir)
    index = 0
    window_name = "Video Player"
    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(window_name, 1600, 600)

    while True:
        # read the video and mask frames
        video_file = os.path.join(video_dir, filenames[index])
        mask_file = os.path.join(mask_dir, filenames[index])
        video_frame = cv2.imread(video_file)
        mask_frame = cv2.imread(mask_file, cv2.IMREAD_GRAYSCALE)

        # resize the video frame and mask frame
        video_frame = cv2.resize(video_frame, (800, 600))
        mask_frame = cv2.resize(mask_frame, (800, 600))

        # add the filename to the frame
        cv2.putText(video_frame, filenames[index], (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

        # display the frames side by side
        combined_frame = cv2.hconcat([video_frame, cv2.cvtColor(mask_frame, cv2.COLOR_GRAY2BGR)])
        cv2.imshow(window_name, combined_frame)

        # wait for user input
        key = cv2.waitKey(0) & 0xFF

        # handle user input
        if key == ord(' '):  # pause with spacebar
            cv2.waitKey(-1)
        elif key == 27:  # exit with escape key
            break
        elif key == 81 or key == 82:  # previous or next video with arrow keys
            if key == 81:
                index -= 1
            elif key == 82:
                index += 1

            if index < 0:
                index = len(filenames) - 1
            elif index >= len(filenames):
                index = 0

    cv2.destroyAllWindows()

play_videos_in_sync('./videos','./masks')
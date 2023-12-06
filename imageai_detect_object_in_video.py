# import the necessary packages
import sys
import cv2
import numpy as np
from imageai.Detection import ObjectDetection

# read the video file name and confidence threshold from the command line arguments
video_file = sys.argv[1]
confidence_threshold = float(sys.argv[2])

detector = ObjectDetection()
detector.setModelTypeAsYOLOv3()
detector.setModelPath("yolov3.pt")
detector.loadModel()

# create a video capture object to read the video file
cap = cv2.VideoCapture(video_file)

# get the video frame width and height
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

# create a video writer object to write the output video file
video_out = cv2.VideoWriter(video_file[:-4] + "-imageai.mp4", cv2.VideoWriter_fourcc(*"mp4v"), 30, (frame_width, frame_height))

# loop over the frames of the video
while True:
    # read a frame from the video
    ret, img = cap.read()
    # check if the frame is valid
    if not ret:
        break
    
    out_img, detections = detector.detectObjectsFromImage(input_image=img, output_type='array',minimum_percentage_probability=confidence_threshold)
    
    # get the frame dimensions
    height, width, channels = img.shape


    # write the frame to the output video file
    video_out.write(out_img)

    # show the frame
    cv2.imshow("Frame", out_img)
    # wait for a key press or 1 ms
    key = cv2.waitKey(1)
    # if the 'q' key is pressed, break the loop
    if key == ord("q"):
        break

# release the video capture and writer objects
cap.release()
video_out.release()
# destroy all the windows
cv2.destroyAllWindows()

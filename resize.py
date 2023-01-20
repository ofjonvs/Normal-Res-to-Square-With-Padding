#!/usr/bin/env python
#

import imageio as ffmpeg
import cv2
import numpy as np
import os



def square_video(input_path, output_path):
    # Create a new video writer
    
    # Open the input video
    reader = ffmpeg.get_reader(input_path)
    meta = reader.get_meta_data()
    fps = meta['fps']
    writer = ffmpeg.get_writer(output_path, fps=fps)
    # cont = True
    for im in reader:
        # Add black padding to the top and bottom of the video
        h, w, _ = im.shape
        top = 420
        bottom = 420
        
        im = cv2.copyMakeBorder(im, top, bottom, 0, 0, cv2.BORDER_CONSTANT, None, (0,0,0))
        
        # Write the frame to the output video
        writer.append_data(im.astype(np.uint8))
    # Close the writer and reader
    writer.close()
    reader.close()



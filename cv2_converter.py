# © 2023 Karan Mirajkar - Some Rights Reserved

# This work is licensed under the Creative Commons Attribution-ShareAlike 4.0 License.
# To view a copy of this license, visit https://creativecommons.org/licenses/.

# You are free to:
#   - Share: Copy and redistribute the material in any medium or format
#   - Adapt: Remix, transform, and build upon the material

# Under the following terms:
#   - Attribution: You must give appropriate credit, provide a link to the license, and indicate if changes were made. You may do so in any reasonable manner, but not in any way that suggests the licensor endorses you or your use.
#   - ShareAlike: If you remix, transform, or build upon the material, you must distribute your contributions under the same license as the original.

import cv2
import os


def seq_converter(seq_path,out_path,fps,res=[1280,720]):
    
    # Sort the file names in ascending order if necessary
    # images = [img for img in os.listdir(seq_path) if img.endswith(".jpg")]
    images = os.listdir(seq_path)
    images.sort()  
    #print(images)


    # Create a VideoWriter object
    # fourcc = cv2.VideoWriter_fourcc(*'MJPG')
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')

    video_writer = cv2.VideoWriter(out_path,fourcc, fps,res)
    # Resize 
    #cv2.resize(image,res)

    #prepare text properties
    text = text
    font = cv2.FONT_HERSHEY_PLAIN
    print(res)
    print((int(res[0]/2),int(res[1]/2)))
    orgin = (int(res[0]/4),int(res[1]/4))
    # orgin = (100,200)
    color = (255,255,255)
    fontScale = 1
    thickness = 1

    # Writing the images to the VideoWriter object
    for image in images:
        
        # print(image)
        # print(os.path.join(seq_path, image))

        image = cv2.imread(os.path.join(seq_path, image))
        image = cv2.resize(image,res)
             
        
        #Put Text on sequence
        image = cv2.putText(image,text,orgin,font,fontScale,color,thickness,cv2.LINE_AA ,False)


        video_writer.write(image)

    # Release the VideoWriter object
    video_writer.release()

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


def seq_converter(seq_path,out_path,fps,text,res=[1280,720]):
    
    # Sorting file names in ascending order
    images = os.listdir(seq_path)
    images.sort()  
    #print(images)


    # Create a VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')

    video_writer = cv2.VideoWriter(out_path,fourcc, fps,res)
    

    #Prepare text properties
    font = cv2.FONT_HERSHEY_PLAIN
    #set relative text position
    #bottom_right
    orgin = (int(res[0] - (res[0]/4)),int(res[1]-(res[1]/5)))
    # orgin = (50,50)
    print(orgin)
    color = (255,255,255)
    fontScale = 1
    thickness = 1

    # Writing the images to the VideoWriter object
    for image in images:
        
        # print(image)
        print(os.path.join(seq_path, image))

        image = cv2.imread(os.path.join(seq_path, image))
        #resize image
        image = cv2.resize(image,res)
             
        
        #Add burn-in Text on Sequence
        offset = 35
        for idx,txt in enumerate(text.split("\n")):
            
            image = cv2.putText(image,txt,(orgin[0],orgin[1]+offset*idx),font,fontScale,color,thickness,cv2.LINE_AA ,False)


        video_writer.write(image)

    # Release the VideoWriter object
    video_writer.release()

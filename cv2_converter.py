import cv2
import os


def seq_converter(seq_path,out_path,fps,res=[1280,720]):
    
    # Sort the file names in ascending order if necessary
    images = [img for img in os.listdir(seq_path) if img.endswith(".png")]
    images.sort()  
    print(images)

    #get seq resolution
    # frame = cv2.imread(os.path.join(seq_path, images[0]))
    # height, width, _ = frame.shape
    # res = [height,width]

    # Create a VideoWriter object
    # fourcc = cv2.VideoWriter_fourcc(*'MJPG')
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')

    video_writer = cv2.VideoWriter(out_path,fourcc, fps,res)
    # Resize 
    #cv2.resize(image,res)



    # Write the images to the VideoWriter object
    for image in images:
        
        print(image)
        print(os.path.join(seq_path, image))

        image = cv2.imread(os.path.join(seq_path, image))
        image = cv2.resize(image,res)

        # # Split the image into color channels and alpha channel
        # b, g, r, a = cv2.split(image)

        # # Normalize the color channels from 0-255 to 0-1
        # b = b / 255.0
        # g = g / 255.0
        # r = r / 255.0

        # # Premultiply the color channels by the alpha channel
        # b *= a
        # g *= a
        # r *= a

        # # Combine the premultiplied color channels and alpha channel
        # image = cv2.merge((b, g, r, a))

        
        video_writer.write(image)

    # Release the VideoWriter object
    video_writer.release()

# seq_converter('D:/Houdini_FX_Training/404_pyro/explo_flipbook/v002','D:/Work/python_dev/converted_seq/test_video13.mp4',24,[1920,1080])
#seq_converter('D:/Work/freelance/stride_vfx_studio_work/2023_05_26_001_firework_shot/houdini/flipbooks/v007/','D:/Work/python_dev/converted_seq/test_video13.mp4',24,[1920,1080])
# seq_converter('D:/Work/freelance/stride_vfx_studio_work/2023_05_26_001_firework_shot/houdini/flipbooks/v007/','D:/Work/python_dev/converted_seq/test_video13.mp4',24)
import cv2
import os

seq_path = "D:/Work/python_dev/test_seq/"
out_path = "D:/Work/python_dev/opencv_video_converter/test_vid.mp4"

vid_ext = ".mp4"

def seq_converter(seq_path,out_path,fps,res=[1080,720]):
    imgs = os.listdir(seq_path)
    #print(imgs)
    img_path = []

    for i in imgs:
        i = seq_path+i
        #print(i)
        #i.replace("j","k")
        img_path.append(i)
    #print(img_path[0])

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    #print(img_path[0])

    vid_size = list(cv2.imread(img_path[0]).shape)
    del vid_size[2]
    vid_size.reverse()
    print(vid_size)

    # get_size = list(frame.shape)
    # print(get_size)

    vid = cv2.VideoWriter(out_path,fourcc,24,vid_size)

    for i in range(len(img_path)):
        vid.write(cv2.imread(img_path[i]))
        print(i+1)

    vid.release()
    # frame = cv2.imread("C:/Users/PERMAN/Downloads/Crater_credit_post.png")
    # cv2.imshow('image',frame)
    # cv2.waitKey(0)

seq_converter(seq_path,out_path,24)
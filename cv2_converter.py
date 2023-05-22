import cv2
import os


def seq_converter(seq_path,out_path,fps,res=[1280,720]):
    imgs = os.listdir(seq_path)
    
    
    img_path = []

    for i in imgs:
        i = os.path.join(seq_path,i)
        #i = str(seq_path+i)
        i = i.replace('\\','/')
        print(i)
        img_path.append(i)

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')

    # res = list(cv2.imread(img_path[0]).shape)
    # del res[2]
    # res.reverse()
    # print(res)

    vid = cv2.VideoWriter(out_path,fourcc,24,res)

    for i in range(len(img_path)):
        vid.write(cv2.imread(img_path[i]))
        print(i+1)

    #vid.release()
    
# seq_converter('D:\Work\python_dev\opencv_video_converter','',21)
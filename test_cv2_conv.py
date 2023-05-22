import cv2
import os


# def seq_converter(seq_path,out_path,fps,res=[1080,720]):
#     imgs = os.listdir(seq_path)
#     img_path = []

#     for i in imgs:
#         i = seq_path+i
#         img_path.append(i)

#     fourcc = cv2.VideoWriter_fourcc(*'mp4v')

#     def_res = list(cv2.imread(img_path[0]).shape)
#     del def_res[2]
#     def_res.reverse()
#     print(def_res)

#     vid = cv2.VideoWriter(out_path,fourcc,24,res)

#     for i in range(len(img_path)):
#         vid.write(cv2.imread(img_path[i]))
#         print(i+1)

#     vid.release()
#     return def_res
# seq_path = 'D:/Work/python_dev/test_seq/'

# seq_path = seq_path.replace('\\','/')
# seq_path += '/'
# img_path = os.path.join(seq_path,os.listdir(seq_path)[0])
# print(img_path)


# repath = seq_path.replace('/','\\')
# print(repath)

# img_path = os.path.join(seq_path,os.listdir(seq_path)[0])
# img = cv2.imread(img_path)
# img_res = img.shape
# res = list(cv2.imread(img_path).shape)
# del res[2]
# res.reverse()
# print(res)
# print(img_path)
# print(img_res)
def testfun():
    if True:
        i = 10
        return i
    

print(testfun())

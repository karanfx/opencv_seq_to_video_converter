import cv2
import os


img_path = "D:/Work/freelance/stride_vfx_studio_work/2023_05_26_001_firework_shot/houdini/flipbooks/v007/firework_opengl_v007.307044.jpg"

img_path2 = "D:/Houdini_FX_Training/404_pyro/explo_flipbook/v002/explo_flipbook_0014.png"
image = cv2.imread(img_path)

cv2.imshow("image",image)
cv2.waitKey(0)
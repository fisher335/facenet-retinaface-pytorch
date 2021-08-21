# coding:utf-8
import os

import cv2
import numpy as np

from retinaface import Retinaface


def rec_pic(file_path):
    retinaface = Retinaface()
    image = cv2.imread(file_path)
    if image is None:
        print('Open Error! Try again!')
    else:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        r_image = retinaface.rec_image(image)



if __name__ == '__main__':
    rec_pic("img/img_0190.jpg")
    # files = []
    # for rt, dirs, files in os.walk("E:\\test"):
    #     for i in files:
    #         print(os.path.join(rt,i))
    #         files.append(os.path.join(rt,i))
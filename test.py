# coding:utf-8
import cv2

from retinaface import Retinaface


def rec_pic(file_path):
    retinaface = Retinaface()
    image = cv2.imread(file_path)
    if image is None:
        print('Open Error! Try again!')
    else:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        r_image = retinaface.detect_image(image)
        r_image = cv2.cvtColor(r_image, cv2.COLOR_RGB2BGR)
        cv2.imshow("after", r_image)
        cv2.waitKey(0)


if __name__ == '__main__':
    rec_pic("img/fengshaomin.jpg")
